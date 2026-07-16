#!/usr/bin/env node
// ignition-timing.js — Initiative 3 research (log-only, no orders).
//
// Question: how often does our fixed AH scan grid fire *before* a winner's
// ignition minute (so we see it flat and catch it late once it's already
// +50-100%)? Init 1 found ignition is a single-minute price+volume co-spike
// (IVF 16:53 ET); this quantifies the ignition-vs-scan-grid gap across winners
// to justify a retimed/added AH observation scan (a trading-scan timing change
// -> propose to Juan for veto).
//
// Method: for a ticker + AH-evening date D, pull real Alpaca SIP 1-min bars for
// the AH session (D 16:00-20:00 ET). Baseline = the D regular-session daily
// close. Ignition = the first 1-min bar that BOTH (a) closes/highs >= +IGN_PCT%
// vs base AND (b) carries a real volume co-spike (trades >= MIN_TRADES and
// >= K x the running median trades of prior active bars). Report the ignition
// ET minute, then map it onto the current AH scan grid and report which scan is
// the first to fire at/after ignition and the lag in minutes.
//
// Usage: node scripts/ignition-timing.js SYM:YYYY-MM-DD [SYM:YYYY-MM-DD ...]
//                                         [--ignpct 15] [--mintrades 20] [--k 5]
// Requires ALPACA_API_KEY / ALPACA_SECRET_KEY (via broker.js).

const { execFileSync } = require("child_process");
const path = require("path");
const BROKER = path.join(__dirname, "broker.js");

// Current AH scan grid, Europe/Berlin local (summer CET = ET + 6h).
// 21:30,22:00,22:30,23:00,23:30,00:00,00:30 CET => 15:30..18:30 ET (30-min).
const SCAN_GRID_ET = [
  "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30",
];

function bars(sym, tf, startISO, limit, feed = "sip") {
  const out = execFileSync(
    "node",
    [BROKER, "bars", sym, "--tf", tf, "--start", startISO, "--limit", String(limit), "--feed", feed],
    { encoding: "utf8" }
  );
  const rows = [];
  for (const line of out.split("\n")) {
    const m = line.match(
      /^(\S+)\s+O \$([\d.]+) H \$([\d.]+) L \$([\d.]+) C \$([\d.]+)\s+vol (\d+).*?trades (\d+)/
    );
    if (!m) continue;
    rows.push({ t: m[1], o: +m[2], h: +m[3], l: +m[4], c: +m[5], vol: +m[6], trades: +m[7] });
  }
  return rows;
}

function priorClose(sym, dateD) {
  const start = new Date(new Date(dateD + "T00:00:00Z").getTime() - 6 * 864e5)
    .toISOString().slice(0, 10);
  const rows = bars(sym, "1Day", start, 12);
  const target = rows.find((r) => r.t.slice(0, 10) === dateD);
  return target ? target.c : null;
}

function etHM(t) {
  const et = new Date(new Date(t).getTime() - 4 * 3600e3); // summer ET = UTC-4
  return `${String(et.getUTCHours()).padStart(2, "0")}:${String(et.getUTCMinutes()).padStart(2, "0")}`;
}
function etMinutes(hm) { const [h, m] = hm.split(":").map(Number); return h * 60 + m; }

function firstScanAtOrAfter(ignHM) {
  const ign = etMinutes(ignHM);
  for (const s of SCAN_GRID_ET) if (etMinutes(s) >= ign) return s;
  return null; // ignition after the last scan (18:30 ET)
}

function analyze(sym, dateD, IGN, MINTR, K) {
  const base = priorClose(sym, dateD);
  if (!base) return `${sym} ${dateD}: NO prior-close (daily bar missing)`;

  const startISO = `${dateD}T20:00:00Z`; // 16:00 ET
  const endMs = new Date(startISO).getTime() + 4 * 3600e3; // through 20:00 ET
  const all = bars(sym, "1Min", startISO, 500).filter((r) => {
    const ms = new Date(r.t).getTime();
    return ms >= new Date(startISO).getTime() && ms < endMs;
  });
  if (all.length < 3) return `${sym} ${dateD}: too few AH 1-min bars (${all.length})`;

  const priorTrades = [];
  let ign = null;
  for (const r of all) {
    const pct = ((r.h - base) / base) * 100;
    const med = priorTrades.length
      ? priorTrades.slice().sort((a, b) => a - b)[Math.floor(priorTrades.length / 2)]
      : 0;
    const volSpike = r.trades >= MINTR && (med === 0 || r.trades >= med * K);
    if (!ign && pct >= IGN && volSpike) {
      ign = { hm: etHM(r.t), pct, trades: r.trades, vol: r.vol, med };
    }
    if (r.trades > 0) priorTrades.push(r.trades);
  }

  let peak = 0, peakHM = "-";
  for (const r of all) { const p = ((r.h - base) / base) * 100; if (p > peak) { peak = p; peakHM = etHM(r.t); } }

  if (!ign) {
    return `${sym} ${dateD}  base=$${base.toFixed(2)}  peak +${peak.toFixed(0)}% @${peakHM}ET  IGNITION: none met (>= +${IGN}% + volspike in AH)`;
  }

  const scan = firstScanAtOrAfter(ign.hm);
  const lag = scan ? etMinutes(scan) - etMinutes(ign.hm) : null;
  const beforeGridEnd = etMinutes(ign.hm) <= etMinutes("18:30");
  let coverage;
  if (!scan) coverage = "AFTER last scan (18:30 ET) — grid never sees ignition";
  else if (scan === SCAN_GRID_ET[0] && etMinutes(ign.hm) < etMinutes("15:30"))
    coverage = `before grid opens; first scan ${scan}ET lags +${lag}m`;
  else coverage = `first scan at/after = ${scan}ET (lag +${lag}m)`;

  return [
    `${sym} ${dateD}  base=$${base.toFixed(2)}  peak +${peak.toFixed(0)}% @${peakHM}ET`,
    `  IGNITION ${ign.hm}ET  +${ign.pct.toFixed(0)}%  ${ign.trades} trades / ${ign.vol} sh  (med prior ${ign.med})`,
    `  scan-grid: ${coverage}`,
    `  ${beforeGridEnd ? "" : "IGNITION IN AH TAIL (past 18:30 ET grid end) — "}`.trimEnd(),
  ].filter(Boolean).join("\n");
}

function main() {
  const args = process.argv.slice(2);
  let IGN = 15, MINTR = 20, K = 5;
  const pairs = [];
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--ignpct") { IGN = +args[++i]; continue; }
    if (args[i] === "--mintrades") { MINTR = +args[++i]; continue; }
    if (args[i] === "--k") { K = +args[++i]; continue; }
    if (args[i].includes(":")) { const [s, d] = args[i].split(":"); pairs.push([s.toUpperCase(), d]); }
  }
  if (!pairs.length) {
    console.error("usage: node scripts/ignition-timing.js SYM:YYYY-MM-DD [...] [--ignpct 15] [--mintrades 20] [--k 5]");
    process.exit(1);
  }
  console.log(`# ignition-timing audit  (IGN>=+${IGN}%, MINTR=${MINTR}, K=${K}x)  scan grid ET: ${SCAN_GRID_ET.join(",")}`);
  console.log("");
  for (const [s, d] of pairs) {
    try { console.log(analyze(s, d, IGN, MINTR, K)); }
    catch (e) { console.log(`${s} ${d}: ERROR ${e.message.split("\n")[0]}`); }
    console.log("");
  }
}

main();
