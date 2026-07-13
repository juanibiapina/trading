#!/usr/bin/env node
/*
 * trailing-sim.js — Init 6 (b): simulate a trailing-stop partial hold.
 *
 * The exit-signal.js test (2026-07-10) proved no at-exit signal separates the
 * IVF-type regular-session runners from the DCX-type open-dumpers. So the pilot
 * lets a TRAILING STOP do the sorting: on every green premarket exit, hold a
 * partial into the regular session under a trailing stop, and let the stop cut
 * the faders while the runners keep running.
 *
 * This script quantifies that. For every closed round-trip, it takes the
 * premarket exit as the hypothetical hold-start, walks the exit-day
 * regular-session (09:30-16:00 ET) 5-min SIP bars, and simulates a trailing
 * stop of each candidate width. It reports what the held partial would have
 * captured vs the actual premarket exit, so the pilot proposal carries a real
 * expected-added-return number instead of a hand-wave.
 *
 * Log-only research. Places no orders. Reads fills via broker.js.
 *
 * Stop model per bar (chronological, after the exit time):
 *   - peak starts at the premarket exit price.
 *   - if bar.open <= stop  -> exit filled at bar.open (gap through the stop).
 *   - else if bar.low <= stop -> exit filled at stop.
 *   - else update peak = max(peak, bar.high); stop = peak * (1 - width).
 *   - if never stopped, exit at the session close.
 * Only positions GREEN at the premarket exit are eligible (the pilot's gate).
 *
 * Usage: node scripts/trailing-sim.js
 */
const { execFileSync } = require("child_process");

const WIDTHS = [8, 12, 15, 20];
const HOLD_FRACTION = 0.5; // pilot holds a half-partial into the regular session

function broker(args) {
  return execFileSync("node", [`${__dirname}/broker.js`, ...args], { encoding: "utf8" });
}

function getFills() {
  return JSON.parse(broker(["orders", "all", "--json"]))
    .filter((o) => o.status === "filled")
    .map((o) => ({ sym: o.symbol, side: o.side, qty: +o.filled_qty, px: +o.filled_avg_price, t: new Date(o.filled_at) }))
    .sort((a, b) => a.t - b.t);
}

function roundTrips(fills) {
  const open = {}, trips = [];
  for (const f of fills) {
    const q = (open[f.sym] = open[f.sym] || []);
    if (f.side === "buy") q.push(f);
    else if (f.side === "sell" && q.length) trips.push({ sym: f.sym, entry: q.shift(), exit: f });
  }
  return trips;
}

// exit-day 5-min SIP bars covering the regular session (13:30-20:00 UTC).
function regularBars(sym, dateISO) {
  let out;
  try { out = broker(["bars", sym, "--tf", "5Min", "--feed", "sip", "--start", `${dateISO}T13:30:00Z`, "--limit", "90"]); }
  catch { return []; }
  const bars = [];
  for (const line of out.split("\n")) {
    const m = line.match(/^(\d{4}-\d{2}-\d{2}T[\d:]+Z)\s+O \$([\d.]+) H \$([\d.]+) L \$([\d.]+) C \$([\d.]+)/);
    if (m) {
      const t = new Date(m[1]);
      const hhmm = t.getUTCHours() * 100 + t.getUTCMinutes();
      if (hhmm >= 1330 && hhmm < 2000) bars.push({ t, o: +m[2], h: +m[3], l: +m[4], c: +m[5] });
    }
  }
  return bars;
}

const pct = (a, b) => ((a - b) / b) * 100;
const mean = (a) => (a.length ? a.reduce((x, y) => x + y, 0) / a.length : 0);

// Simulate a trailing stop starting at `start` price over regular-session bars.
function trail(bars, start, width) {
  let peak = start;
  let stop = peak * (1 - width / 100);
  for (const b of bars) {
    if (b.o <= stop) return { px: b.o, reason: "gap" };
    if (b.l <= stop) return { px: stop, reason: "stop" };
    if (b.h > peak) { peak = b.h; stop = peak * (1 - width / 100); }
  }
  const last = bars[bars.length - 1];
  return { px: last.c, reason: "close" };
}

function main() {
  const trips = roundTrips(getFills());
  const rows = [];
  for (const t of trips) {
    const exd = t.exit.t.toISOString().slice(0, 10);
    const green = pct(t.exit.px, t.entry.px);
    const bars = regularBars(t.sym, exd);
    if (bars.length < 2) continue; // regular session not formed yet
    const eligible = green > 0; // pilot gate: only hold green exits
    const verdictHigh = pct(Math.max(...bars.map((b) => b.h)), t.exit.px);
    const sims = {};
    for (const w of WIDTHS) sims[w] = trail(bars, t.exit.px, w);
    rows.push({ sym: t.sym, exd, green, eligible, exit: t.exit.px, vsHigh: verdictHigh, sims });
  }

  const hdr = ["sym", "exit_day", "green%", "exitPx", "regHigh%"].concat(WIDTHS.map((w) => `ts${w}%`));
  console.log(hdr.join("\t"));
  for (const r of rows) {
    const cols = [r.sym, r.exd, r.green.toFixed(1), r.exit.toFixed(2), r.vsHigh.toFixed(1)];
    for (const w of WIDTHS) {
      const cap = pct(r.sims[w].px, r.exit); // added return of the held partial vs premarket exit
      cols.push(`${cap >= 0 ? "+" : ""}${cap.toFixed(1)}${r.sims[w].reason === "close" ? "c" : ""}`);
    }
    console.log(cols.join("\t") + (r.eligible ? "" : "\t(red-skip)"));
  }

  // Aggregate over ELIGIBLE (green-at-exit) trades only — the pilot's population.
  const elig = rows.filter((r) => r.eligible);
  console.log(`\nEligible (green at premarket exit): ${elig.length} of ${rows.length} round-trips.`);
  console.log("Trailing-stop capture vs premarket exit, averaged over eligible trades:");
  console.log("  width  avgCapture%  medianCapture%  addedReturn/trade@50%partial");
  for (const w of WIDTHS) {
    const caps = elig.map((r) => pct(r.sims[w].px, r.exit)).sort((a, b) => a - b);
    if (!caps.length) continue;
    const avg = mean(caps);
    const med = caps[Math.floor(caps.length / 2)];
    const added = avg * HOLD_FRACTION; // holding a half-partial
    console.log(`  ${String(w).padStart(2)}%    ${avg >= 0 ? "+" : ""}${avg.toFixed(1)}        ${med >= 0 ? "+" : ""}${med.toFixed(1)}         ${added >= 0 ? "+" : ""}${added.toFixed(1)}%`);
  }
  // Also aggregate over ALL trades (hold-all, no green gate) — since the
  // exit-signal test showed runners are often RED at exit, the green gate may
  // be excluding the very runners we want.
  console.log(`\nHold-ALL (no green gate): ${rows.length} round-trips.`);
  console.log("  width  avgCapture%  medianCapture%  addedReturn/trade@50%partial");
  for (const w of WIDTHS) {
    const caps = rows.map((r) => pct(r.sims[w].px, r.exit)).sort((a, b) => a - b);
    if (!caps.length) continue;
    const avg = mean(caps);
    const med = caps[Math.floor(caps.length / 2)];
    const added = avg * HOLD_FRACTION;
    console.log(`  ${String(w).padStart(2)}%    ${avg >= 0 ? "+" : ""}${avg.toFixed(1)}        ${med >= 0 ? "+" : ""}${med.toFixed(1)}         ${added >= 0 ? "+" : ""}${added.toFixed(1)}%`);
  }

  console.log(`\nInterpretation: addedReturn/trade is the extra P&L per round-trip from`);
  console.log(`holding a ${HOLD_FRACTION * 100}% partial under the trailing stop instead of exiting all in`);
  console.log(`premarket. Positive => the pilot beats the all-out-premarket baseline.`);
}

main();
