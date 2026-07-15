#!/usr/bin/env node
// volume-lead.js — Initiative 1 research (log-only, no orders).
//
// Question: does the VOLUME surge lead the PRICE explosion on our AH->PM
// winners? If volume crosses a threshold measurably *before* price crosses
// +20%, a volume-first trigger could front-run the current price-first entry
// and catch the move earlier (Juan: "we catch spikes late, once +50-100%").
//
// Method: for a given ticker + AH-evening date D, pull real Alpaca SIP 5-min
// bars across the AH session (D 20:00Z–24:00Z = 16:00–20:00 ET) and the next
// morning's premarket (D+1 08:00Z–13:30Z = 04:00–09:30 ET). Baseline = the
// regular-session close on D (from the daily bar). Walk the bars and record:
//   - t_p20 / t_p50: first bar whose price >= +20% / +50% vs prior close
//   - t_vol: first bar whose per-bar volume >= K x the median of the first
//            N "quiet" bars (a relative-volume surge), K/N configurable
//   - lead  = t_p20 - t_vol  (positive => volume led price)
//
// Usage: node scripts/volume-lead.js SYM YYYY-MM-DD [--k 5] [--n 4]
//   (multiple SYM:DATE pairs may be passed; one line summary each)
// Requires ALPACA_API_KEY / ALPACA_SECRET_KEY in env (via broker.js path).

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
    // 2026-06-25T20:00:00Z  O $1.47 H $1.50 L $1.45 C $1.48  vol 331 ... trades 5
    const m = line.match(
      /^(\S+)\s+O \$([\d.]+) H \$([\d.]+) L \$([\d.]+) C \$([\d.]+)\s+vol (\d+).*?trades (\d+)/
    );
    if (!m) continue;
    rows.push({
      t: m[1],
      o: +m[2],
      h: +m[3],
      l: +m[4],
      c: +m[5],
      vol: +m[6],
      trades: +m[7],
    });
  }
  return rows;
}

function priorClose(sym, dateD) {
  // Daily bars are regular-session only; the D daily bar's close is our baseline.
  const start = new Date(new Date(dateD + "T00:00:00Z").getTime() - 5 * 864e5)
    .toISOString()
    .slice(0, 10);
  const rows = bars(sym, "1Day", start, 10);
  const target = rows.find((r) => r.t.slice(0, 10) === dateD);
  return target ? target.c : null;
}

function fmt(t) {
  // UTC ISO -> ET HH:MM (ET = UTC-4 in summer). Label session.
  const d = new Date(t);
  const et = new Date(d.getTime() - 4 * 3600e3);
  const hh = String(et.getUTCHours()).padStart(2, "0");
  const mm = String(et.getUTCMinutes()).padStart(2, "0");
  const h = et.getUTCHours();
  let sess = "reg";
  if (h >= 16 && h < 20) sess = "AH";
  else if (h >= 4 && h < 9.5) sess = "PM";
  else if (h >= 20 || h < 4) sess = "closed";
  return `${hh}:${mm}ET(${sess})`;
}

function analyze(sym, dateD, K, N) {
  const base = priorClose(sym, dateD);
  if (!base) return `${sym} ${dateD}: NO prior-close (daily bar missing)`;

  // AH of D (20:00Z) through PM of D+1 (13:30Z) — ~17.5h window.
  const startISO = `${dateD}T20:00:00Z`;
  const all = bars(sym, "5Min", startISO, 400).filter((r) => {
    const ms = new Date(r.t).getTime();
    const endMs = new Date(startISO).getTime() + 17.5 * 3600e3;
    return ms >= new Date(startISO).getTime() && ms <= endMs;
  });
  if (all.length < 5) return `${sym} ${dateD}: too few bars (${all.length})`;

  // Volume baseline = median of the first N bars with any volume.
  const quiet = all.filter((r) => r.vol > 0).slice(0, N).map((r) => r.vol);
  const med = quiet.length ? quiet.slice().sort((a, b) => a - b)[Math.floor(quiet.length / 2)] : 0;
  const volThresh = med * K;

  let tP20 = null, tP50 = null, tVol = null, peak = 0, tPeak = null;
  for (const r of all) {
    const pct = ((r.h - base) / base) * 100;
    if (pct > peak) { peak = pct; tPeak = r.t; }
    if (tP20 === null && pct >= 20) tP20 = r.t;
    if (tP50 === null && pct >= 50) tP50 = r.t;
    if (tVol === null && med > 0 && r.vol >= volThresh) tVol = r.t;
  }

  const leadMin = (a, b) => {
    if (!a || !b) return null;
    return Math.round((new Date(a).getTime() - new Date(b).getTime()) / 60000);
  };
  const lead20 = leadMin(tP20, tVol); // + => vol led price+20%

  return [
    `${sym} ${dateD}  base=$${base.toFixed(2)}  peak=+${peak.toFixed(0)}% @${tPeak ? fmt(tPeak) : "-"}`,
    `  volSurge(>=${K}x med ${med})  first@ ${tVol ? fmt(tVol) : "NONE"}`,
    `  price+20%   first@ ${tP20 ? fmt(tP20) : "NONE"}   price+50% first@ ${tP50 ? fmt(tP50) : "NONE"}`,
    `  LEAD(vol->+20%) = ${lead20 === null ? "n/a" : (lead20 >= 0 ? "+" : "") + lead20 + " min"}`,
  ].join("\n");
}

function main() {
  const args = process.argv.slice(2);
  let K = 5, N = 4;
  const pairs = [];
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--k") { K = +args[++i]; continue; }
    if (args[i] === "--n") { N = +args[++i]; continue; }
    // SYM DATE  OR  SYM:DATE
    if (args[i].includes(":")) {
      const [s, d] = args[i].split(":");
      pairs.push([s.toUpperCase(), d]);
    } else if (/^\d{4}-\d{2}-\d{2}$/.test(args[i + 1] || "")) {
      pairs.push([args[i].toUpperCase(), args[++i]]);
    }
  }
  if (!pairs.length) {
    console.error("usage: node scripts/volume-lead.js SYM YYYY-MM-DD [SYM YYYY-MM-DD ...] [--k 5] [--n 4]");
    process.exit(1);
  }
  console.log(`# volume-lead backtest  (K=${K}x, N=${N} quiet bars)  positive LEAD => volume leads price`);
  for (const [s, d] of pairs) {
    try {
      console.log(analyze(s, d, K, N));
    } catch (e) {
      console.log(`${s} ${d}: ERROR ${e.message.split("\n")[0]}`);
    }
    console.log("");
  }
}

main();
