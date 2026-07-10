#!/usr/bin/env node
/*
 * exit-signal.js — Init 6 (b): find the signal that separates runners from dumpers.
 *
 * exit-cost.js proved the premarket-exit rule clips ~+30% runners (LEFT) while
 * dodging dumps (SAVED). A blanket "hold everything" is wrong (it bleeds
 * faders). So the pilot needs an ENTRY signal, checkable AT the premarket-exit
 * moment, that flags the IVF-type regular-session runners without holding the
 * DCX-type open-dumpers.
 *
 * This script pulls the exit-day premarket 5-min SIP bars up to each exit and
 * measures candidate signals at the exit check, then tabulates them against the
 * LEFT/SAVED verdict from exit-cost.js. Log-only research, no orders.
 *
 * Candidate signals measured at exit time T:
 *   green%    = exit price vs entry (still green at exit?)
 *   momo%     = last-bar high vs the high ~30m earlier (rising into the exit?)
 *   offHigh%  = exit vs the PM session high so far (0 = fresh high, negative = faded off it)
 *   volTrend  = mean trades/bar last 3 bars vs prior 3 (volume building into exit?)
 *
 * Usage: node scripts/exit-signal.js
 */
const { execFileSync } = require("child_process");

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

function dailyBars(sym, dateISO) {
  let out;
  try { out = broker(["bars", sym, "--tf", "1Day", "--start", `${dateISO}T00:00:00Z`, "--limit", "3"]); }
  catch { return []; }
  const bars = [];
  for (const line of out.split("\n")) {
    const m = line.match(/^(\d{4}-\d{2}-\d{2})T[\d:]+Z\s+O \$([\d.]+) H \$([\d.]+) L \$([\d.]+) C \$([\d.]+)/);
    if (m) bars.push({ date: m[1], o: +m[2], h: +m[3], l: +m[4], c: +m[5] });
  }
  return bars;
}

// exit-day intraday 5-min SIP bars from 08:00Z (04:00 ET premarket) up to exit.
function intradayBars(sym, dateISO) {
  let out;
  try { out = broker(["bars", sym, "--tf", "5Min", "--feed", "sip", "--start", `${dateISO}T08:00:00Z`, "--limit", "60"]); }
  catch { return []; }
  const bars = [];
  for (const line of out.split("\n")) {
    const m = line.match(/^(\d{4}-\d{2}-\d{2}T[\d:]+Z)\s+O \$([\d.]+) H \$([\d.]+) L \$([\d.]+) C \$([\d.]+)\s+vol (\d+).*trades (\d+)/);
    if (m) bars.push({ t: new Date(m[1]), o: +m[2], h: +m[3], l: +m[4], c: +m[5], vol: +m[6], trades: +m[7] });
  }
  return bars;
}

const pct = (a, b) => ((a - b) / b) * 100;
const mean = (a) => (a.length ? a.reduce((x, y) => x + y, 0) / a.length : 0);

function main() {
  const trips = roundTrips(getFills());
  const rows = [];
  for (const t of trips) {
    const exd = t.exit.t.toISOString().slice(0, 10);
    const daily = dailyBars(t.sym, exd);
    const same = daily.find((b) => b.date === exd);
    if (!same) continue; // regular session not formed yet (today's exits)
    const verdict = pct(same.h, t.exit.px) >= 8 ? "LEFT" : pct(same.c, t.exit.px) <= -5 ? "SAVED" : "flat";

    const bars = intradayBars(t.sym, exd).filter((b) => b.t <= t.exit.t);
    let momo = null, offHigh = null, volTrend = null;
    if (bars.length >= 2) {
      const pmHigh = Math.max(...bars.map((b) => b.h));
      offHigh = pct(t.exit.px, pmHigh); // <=0; near 0 = exiting at a fresh high
      const last = bars[bars.length - 1];
      // high ~30m (6 bars) earlier, or the earliest available
      const ref = bars[Math.max(0, bars.length - 7)];
      momo = pct(last.h, ref.h);
      if (bars.length >= 6) {
        const last3 = mean(bars.slice(-3).map((b) => b.trades));
        const prev3 = mean(bars.slice(-6, -3).map((b) => b.trades));
        volTrend = prev3 ? pct(last3, prev3) : null;
      }
    }
    rows.push({
      sym: t.sym, exd, green: pct(t.exit.px, t.entry.px),
      momo, offHigh, volTrend, verdict, nbars: bars.length,
    });
  }

  const h = ["sym", "exit_day", "green%", "momo%", "offHigh%", "volTrend%", "nbars", "verdict"];
  console.log(h.join("\t"));
  for (const r of rows) {
    console.log([
      r.sym, r.exd, r.green.toFixed(1),
      r.momo == null ? "-" : r.momo.toFixed(1),
      r.offHigh == null ? "-" : r.offHigh.toFixed(1),
      r.volTrend == null ? "-" : r.volTrend.toFixed(0),
      r.nbars, r.verdict,
    ].join("\t"));
  }

  // Group means by verdict to see which signal separates.
  console.log("\nMeans by verdict:");
  for (const v of ["LEFT", "SAVED", "flat"]) {
    const g = rows.filter((r) => r.verdict === v);
    if (!g.length) continue;
    const f = (k) => { const xs = g.map((r) => r[k]).filter((x) => x != null); return xs.length ? mean(xs).toFixed(1) : "-"; };
    console.log(`  ${v} (n=${g.length}): green%=${f("green")}  momo%=${f("momo")}  offHigh%=${f("offHigh")}  volTrend%=${f("volTrend")}`);
  }
}

main();
