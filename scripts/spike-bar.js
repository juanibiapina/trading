#!/usr/bin/env node
// spike-bar.js — Initiative 3 / Initiative 1 instrumentation (log-only, no orders).
//
// Juan's 2026-07-16 ask: "I wonder if we can catch the first volume spike bar.
// That would be a great entry point." Init 1 falsified the volume-*lead* idea:
// ignition is a single-minute price+volume co-spike (IVF 16:53 ET), not a quiet
// ramp to front-run. So the tradeable signal is the *first co-spike bar itself*,
// and its absence is a negative filter (Juan: "LVLU is clearly terrible: no
// volume spike").
//
// This is the live counterpart of ignition-timing.js. Where that script audits
// a full past AH session against the scan grid, this one answers, for a live
// candidate at a given scan moment: HAS the first co-spike bar fired yet, and if
// so, when / at what price? It is meant to be called per candidate during the
// AH scans (now 15-min-spaced 22:00-23:00 CET after the 2026-07-17 cadence
// change) to LOG the ignition bar — a log-only column, no entry rule.
//
// Detection mirrors ignition-timing.js: co-spike = a 1-min SIP bar whose high is
// >= +IGN_PCT% vs the regular-session close AND that carries a real volume spike
// (trades >= MIN_TRADES and >= K x the running median trades of prior active
// bars). Output is one line per ticker:
//   SPIKE  16:53ET  +19%  $1.48  72 trades / 25k sh   (first co-spike bar)
//   NO-SPIKE  peak +8% @16:20ET  (no bar cleared +15% on a volume co-spike)
//
// Usage:
//   node scripts/spike-bar.js SYM:YYYY-MM-DD [SYM:YYYY-MM-DD ...]
//        [--now HH:MM]      # ET cutoff; only consider bars up to this minute
//        [--ignpct 15] [--mintrades 20] [--k 5]
// Requires ALPACA_API_KEY / ALPACA_SECRET_KEY (via broker.js).

const { execFileSync } = require("child_process");
const path = require("path");
const BROKER = path.join(__dirname, "broker.js");

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
function fmtK(n) { return n >= 1000 ? `${Math.round(n / 1000)}k` : String(n); }

function analyze(sym, dateD, IGN, MINTR, K, nowHM) {
  const base = priorClose(sym, dateD);
  if (!base) return `${sym} ${dateD}: NO prior-close (daily bar missing)`;

  const startISO = `${dateD}T20:00:00Z`; // 16:00 ET (summer). AH session start.
  const endMs = new Date(startISO).getTime() + 4 * 3600e3; // through 20:00 ET
  let all = bars(sym, "1Min", startISO, 500).filter((r) => {
    const ms = new Date(r.t).getTime();
    return ms >= new Date(startISO).getTime() && ms < endMs;
  });
  // Apply the "now" cutoff so this reflects what a scan at HH:MM ET could see.
  if (nowHM) all = all.filter((r) => etMinutes(etHM(r.t)) <= etMinutes(nowHM));
  if (all.length < 1) return `${sym} ${dateD}  NO-SPIKE  no AH bars yet${nowHM ? ` (as-of ${nowHM}ET)` : ""}`;

  const priorTrades = [];
  let ign = null, peak = 0, peakHM = "-";
  for (const r of all) {
    const pct = ((r.h - base) / base) * 100;
    if (pct > peak) { peak = pct; peakHM = etHM(r.t); }
    const med = priorTrades.length
      ? priorTrades.slice().sort((a, b) => a - b)[Math.floor(priorTrades.length / 2)]
      : 0;
    const volSpike = r.trades >= MINTR && (med === 0 || r.trades >= med * K);
    if (!ign && pct >= IGN && volSpike) {
      ign = { hm: etHM(r.t), pct, price: r.h, trades: r.trades, vol: r.vol };
    }
    if (r.trades > 0) priorTrades.push(r.trades);
  }

  const asof = nowHM ? ` (as-of ${nowHM}ET)` : "";
  if (!ign) {
    const peakStr = peak > 0 ? `peak +${peak.toFixed(0)}% @${peakHM}ET` : `flat/faded (peak <= base)`;
    return `${sym} ${dateD}  NO-SPIKE  ${peakStr}`
      + `  (no bar cleared +${IGN}% on a volume co-spike)${asof}`;
  }
  return `${sym} ${dateD}  SPIKE  ${ign.hm}ET  +${ign.pct.toFixed(0)}%  $${ign.price.toFixed(2)}`
    + `  ${ign.trades} trades / ${fmtK(ign.vol)} sh  (first co-spike bar)${asof}`;
}

function main() {
  const args = process.argv.slice(2);
  let IGN = 15, MINTR = 20, K = 5, nowHM = null;
  const pairs = [];
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--ignpct") { IGN = +args[++i]; continue; }
    if (args[i] === "--mintrades") { MINTR = +args[++i]; continue; }
    if (args[i] === "--k") { K = +args[++i]; continue; }
    if (args[i] === "--now") { nowHM = args[++i]; continue; }
    if (args[i].includes(":") && /\d{4}-\d{2}-\d{2}/.test(args[i])) {
      const [s, d] = args[i].split(":"); pairs.push([s.toUpperCase(), d]);
    }
  }
  if (!pairs.length) {
    console.error("usage: node scripts/spike-bar.js SYM:YYYY-MM-DD [...] [--now HH:MM] [--ignpct 15] [--mintrades 20] [--k 5]");
    process.exit(1);
  }
  console.log(`# spike-bar detector  (IGN>=+${IGN}%, MINTR=${MINTR}, K=${K}x)${nowHM ? `  now<=${nowHM}ET` : ""}`);
  for (const [s, d] of pairs) {
    try { console.log(analyze(s, d, IGN, MINTR, K, nowHM)); }
    catch (e) { console.log(`${s} ${d}: ERROR ${e.message.split("\n")[0]}`); }
  }
}

main();
