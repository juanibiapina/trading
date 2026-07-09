#!/usr/bin/env node
/*
 * exit-cost.js — quantify the cost of the premarket-exit rule.
 *
 * For every closed round-trip in the Alpaca paper account, compare the
 * premarket exit price to what the SAME regular session did AFTER the exit
 * (Alpaca daily bars are regular-session-only, so the daily High/Close bound
 * the "what if we had held through the open" outcome). Also pulls the next
 * regular session to gauge overnight-hold outcomes.
 *
 * This is Initiative 6, rollout problem (b): "let winners run vs premarket
 * exit". Log-only research. It places no orders. It reads fills via broker.js.
 *
 * Output columns:
 *   sym  entry->exit  P&L%  regHigh  vsExit%(high)  regClose  vsExit%(close)  verdict
 *
 * verdict:
 *   LEFT  = regular-session high was >=+8% above our exit (rule clipped a runner)
 *   SAVED = regular close was <=-5% below our exit (rule dodged a dump)
 *   flat  = neither (exit near the day's outcome)
 *
 * Usage: node scripts/exit-cost.js
 */
const { execFileSync } = require("child_process");

function broker(args) {
  return execFileSync("node", [`${__dirname}/broker.js`, ...args], {
    encoding: "utf8",
  });
}

function getFills() {
  const raw = broker(["orders", "all", "--json"]);
  const orders = JSON.parse(raw)
    .filter((o) => o.status === "filled")
    .map((o) => ({
      sym: o.symbol,
      side: o.side,
      qty: +o.filled_qty,
      px: +o.filled_avg_price,
      t: new Date(o.filled_at),
    }))
    .sort((a, b) => a.t - b.t);
  return orders;
}

// Pair buys->sells FIFO per symbol into round-trips.
function roundTrips(fills) {
  const openBySym = {};
  const trips = [];
  for (const f of fills) {
    const q = (openBySym[f.sym] = openBySym[f.sym] || []);
    if (f.side === "buy") {
      q.push(f);
    } else if (f.side === "sell" && q.length) {
      const entry = q.shift();
      trips.push({ sym: f.sym, entry, exit: f });
    }
  }
  return trips;
}

function dailyBar(sym, dateISO) {
  // dateISO = YYYY-MM-DD of the exit; pull that day + next few.
  let out;
  try {
    out = broker(["bars", sym, "--tf", "1Day", "--start", `${dateISO}T00:00:00Z`, "--limit", "3"]);
  } catch {
    return [];
  }
  const bars = [];
  for (const line of out.split("\n")) {
    const m = line.match(/^(\d{4}-\d{2}-\d{2})T[\d:]+Z\s+O \$([\d.]+) H \$([\d.]+) L \$([\d.]+) C \$([\d.]+)/);
    if (m) bars.push({ date: m[1], o: +m[2], h: +m[3], l: +m[4], c: +m[5] });
  }
  return bars;
}

function pct(a, b) {
  return ((a - b) / b) * 100;
}

function main() {
  const trips = roundTrips(getFills());
  const rows = [];
  for (const t of trips) {
    const exd = t.exit.t.toISOString().slice(0, 10);
    const bars = dailyBar(t.sym, exd);
    const same = bars.find((b) => b.date === exd);
    const next = bars.filter((b) => b.date > exd)[0];
    if (!same) continue;
    const pnl = pct(t.exit.px, t.entry.px);
    const vsHigh = pct(same.h, t.exit.px);
    const vsClose = pct(same.c, t.exit.px);
    const nextHigh = next ? pct(next.h, t.exit.px) : null;
    let verdict = "flat";
    if (vsHigh >= 8) verdict = "LEFT";
    else if (vsClose <= -5) verdict = "SAVED";
    rows.push({
      sym: t.sym,
      exd,
      entry: t.entry.px,
      exit: t.exit.px,
      pnl,
      regHigh: same.h,
      vsHigh,
      regClose: same.c,
      vsClose,
      nextHigh,
      verdict,
    });
  }

  const h = ["sym", "exit_day", "entry", "exit", "P&L%", "regHigh", "vsExit%H", "regClose", "vsExit%C", "nextH%", "verdict"];
  console.log(h.join("\t"));
  let left = 0, saved = 0, flat = 0, sumLeftUpside = 0;
  for (const r of rows) {
    console.log(
      [
        r.sym,
        r.exd,
        r.entry.toFixed(2),
        r.exit.toFixed(2),
        r.pnl.toFixed(1),
        r.regHigh.toFixed(2),
        r.vsHigh.toFixed(1),
        r.regClose.toFixed(2),
        r.vsClose.toFixed(1),
        r.nextHigh == null ? "-" : r.nextHigh.toFixed(1),
        r.verdict,
      ].join("\t")
    );
    if (r.verdict === "LEFT") { left++; sumLeftUpside += r.vsHigh; }
    else if (r.verdict === "SAVED") saved++;
    else flat++;
  }
  console.log(
    `\n${rows.length} round-trips: ${left} LEFT (clipped runner), ${saved} SAVED (dodged dump), ${flat} flat.`
  );
  if (left) console.log(`Avg upside missed on LEFT trades: +${(sumLeftUpside / left).toFixed(1)}% (regular-session high vs exit).`);
}

main();
