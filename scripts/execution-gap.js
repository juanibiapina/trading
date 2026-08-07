#!/usr/bin/env node
/*
 * execution-gap.js — Initiative 3 pivot (2026-08-07): quantify how much of the
 * detected AH->PM edge is lost to EXECUTION rather than SELECTION.
 *
 * Across three-plus live CONFIRM-3 sessions the third-bar selection gate did not
 * cleanly separate next-PM winners from fades, while the biggest edges were lost
 * to unfillable AH books, broker blocks, or premature exits. This tallies the
 * loss by cause so we can rank the real bottleneck.
 *
 * Log-only research. Places no orders. Reads log/execution-gap.csv.
 *
 * Cause buckets:
 *   fill          = detected a real PM winner but never got filled (no AH ask /
 *                   AH fade) -> broker/data constraint (Initiative 2 territory)
 *   exit_timing   = we HELD the name but our exit pulse fired before the PM
 *                   spike -> self-inflicted, fixable without a broker change
 *   blocked_saved = broker block/no-fill that avoided a loss (net positive)
 *   selection     = we filled it and the gate/selection was the deciding factor
 *   none          = no gap (avoided a small loss or genuine fade)
 *
 * Usage: node scripts/execution-gap.js
 */
const fs = require("fs");
const path = require("path");

const csv = fs.readFileSync(path.join(__dirname, "..", "log", "execution-gap.csv"), "utf8");
const rows = csv
  .split("\n")
  .filter((l) => l.trim() && !l.startsWith("#") && !l.startsWith("date,"))
  .map((l) => {
    const [date, ticker, confirm3, fill_status, captured, available, cause, gap] = l.split(",");
    return {
      date,
      ticker,
      confirm3,
      fill_status,
      captured: parseFloat(captured),
      available: parseFloat(available),
      cause,
      gap: parseFloat(gap),
    };
  });

const byCause = {};
for (const r of rows) {
  (byCause[r.cause] ||= []).push(r);
}

console.log(`Execution-gap tally — n=${rows.length} qualified/held rows\n`);
console.log("By cause (lost PM upside not captured):");
const order = ["fill", "exit_timing", "blocked_saved", "selection", "none"];
let totalGap = 0;
for (const cause of order) {
  const rs = byCause[cause] || [];
  if (!rs.length) continue;
  const sum = rs.reduce((a, r) => a + r.gap, 0);
  totalGap += sum;
  const names = rs.map((r) => `${r.ticker}${r.gap ? ` +${r.gap}%` : ""}`).join(", ");
  console.log(`  ${cause.padEnd(13)} n=${rs.length}  lost=${sum.toFixed(1)}%  [${names}]`);
}
console.log(`\n  TOTAL lost PM upside: ${totalGap.toFixed(1)}%`);

const fillLost = (byCause.fill || []).reduce((a, r) => a + r.gap, 0);
const exitLost = (byCause.exit_timing || []).reduce((a, r) => a + r.gap, 0);
console.log("\nMoney-fast reading:");
console.log(`  Broker/data (fill) gap:  ${fillLost.toFixed(1)}%  -> Initiative 2 (feed/broker), needs Juan's fix call`);
console.log(`  Self-inflicted (exit-timing) gap: ${exitLost.toFixed(1)}%  -> fixable in our own process (exit-pulse timing)`);
const excl = (byCause.fill || []).filter((r) => r.gap > 100).map((r) => r.ticker);
if (excl.length) {
  const fillExOutlier = (byCause.fill || [])
    .filter((r) => r.gap <= 100)
    .reduce((a, r) => a + r.gap, 0);
  console.log(`  (fill gap ex-${excl.join("/")} outlier: ${fillExOutlier.toFixed(1)}%)`);
}
