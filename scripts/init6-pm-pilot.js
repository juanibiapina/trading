#!/usr/bin/env node
/*
 * init6-pm-pilot.js — Initiative 6 early-PM hypothetical-entry PILOT.
 *
 * GREENLIT by Juan 2026-08-21 ("Go ahead", re: 08-20 email). This is the active
 * serialized pilot slot. LOG-ONLY: places NO orders, changes no trading logic,
 * touches no live pulse. It measures the converged mechanism (continuation-gate
 * entry near the ~04:00-04:21 ET PM ignition + a resting +10% sell-limit exit)
 * against the current live baseline, which enters NONE of these PM-only gappers
 * (the AH scanner is structurally blind to them), so the baseline P&L is $0.
 *
 * Why this restricts to holdable: pm-gapper-exit-sim-1min.js runs the same gate
 * over ALL footprint=none names and the gate admits thin/uninvestable
 * false-positives (WLDS, SDEV, EHGO-2) that we could never fill at size and
 * that drag the mean. A real pilot only "enters" names we could actually fill,
 * so this runner restricts to classification=holdable — the investable universe.
 *
 * Mechanism (identical gate + exit as the converged studies):
 *   - Entry: 5-min continuation gate. Ignition = first PM 5-min bar with
 *     >= 3000 trades; require R+1 and R+2 each close >= 80% of the running high
 *     and VWAP non-declining; enter at the R+3 bar open (near ignition, not
 *     after the full run). Else skip (no pilot trade).
 *   - Exit: resting +10% sell-limit at entry*1.10, fills intrabar on the first
 *     1-min bar whose HIGH reaches it; fallback = PM-last close (09:25 ET) if
 *     never filled. Both studies (Init 6 1-min sim + Init 3 overnight holds)
 *     converged on +10% as the robust width.
 *
 * Baseline = do-nothing (current live cycle never trades PM-only gappers) = 0%.
 * Pilot edge = mean lim10 return across entered (admitted) holdable names.
 *
 * Writes a shadow ledger to log/init6-pm-pilot.csv for out-of-sample
 * accumulation across runs (one row per admitted holdable name).
 *
 * Data: SIP bars via `node scripts/broker.js bars SYM --tf TF --start ISO`.
 * Bars are UTC; EDT (summer) ET = UTC-4, so 08:00Z = 04:00 ET.
 *
 * Usage:
 *   node scripts/init6-pm-pilot.js            # all holdable footprint=none gappers
 *   node scripts/init6-pm-pilot.js SYM DATE   # one ad-hoc case
 */

const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const TRACKER = path.join(__dirname, "..", "log", "pm-open-scan.csv");
const LEDGER = path.join(__dirname, "..", "log", "init6-pm-pilot.csv");
const TRADES_MIN = 3000;
const HOLD_FRAC = 0.8;
const LIMIT_GAIN = 10; // the converged resting sell-limit width
const PM_END = "T13:30:00Z"; // 09:30 ET cap

function fetchBars(sym, date, tf) {
  const start = `${date}T08:00:00Z`;
  let out;
  try {
    out = execFileSync(
      "node",
      [path.join(__dirname, "broker.js"), "bars", sym, "--tf", tf, "--start", start, "--limit", "1000"],
      { encoding: "utf8" }
    );
  } catch (e) {
    return [];
  }
  const bars = [];
  const re = /^(\S+)\s+O \$([\d.]+) H \$([\d.]+) L \$([\d.]+) C \$([\d.]+)\s+vol (\d+)\s+vwap \$([\d.]+)\s+trades (\d+)/;
  for (const line of out.split("\n")) {
    const m = line.match(re);
    if (!m) continue;
    bars.push({ t: m[1], o: +m[2], h: +m[3], l: +m[4], c: +m[5], vol: +m[6], vwap: +m[7], trades: +m[8] });
  }
  return bars;
}

const pct = (from, to) => ((to - from) / from) * 100;

// 5-min continuation gate — identical to pm-gapper-exit-sim-1min.js.
function gate(bars5, date) {
  const pm = bars5.filter((b) => b.t >= `${date}T08:00:00Z` && b.t < `${date}${PM_END}`);
  const rIdx = pm.findIndex((b) => b.trades >= TRADES_MIN);
  if (rIdx < 0) return { admit: false };
  if (rIdx + 3 >= pm.length) return { admit: false };
  const R = pm[rIdx], b1 = pm[rIdx + 1], b2 = pm[rIdx + 2];
  const hi1 = Math.max(R.h, b1.h);
  const hi2 = Math.max(hi1, b2.h);
  if (b1.c < HOLD_FRAC * hi1) return { admit: false };
  if (b2.c < HOLD_FRAC * hi2) return { admit: false };
  if (b2.vwap < b1.vwap * 0.98) return { admit: false };
  return { admit: true, entry: pm[rIdx + 3].o, entryTime: pm[rIdx + 3].t };
}

// Resting +10% sell-limit; fills intrabar on the first 1-min bar reaching it,
// else PM-last close fallback.
function limitExit(min, entry, gainPct) {
  const target = entry * (1 + gainPct / 100);
  for (const b of min) {
    if (b.h >= target) return { px: target, ret: gainPct, at: b.t, filled: true };
  }
  const last = min[min.length - 1];
  return { px: last.c, ret: pct(entry, last.c), at: last.t, filled: false };
}

function sim(sym, date, cls) {
  const bars5 = fetchBars(sym, date, "5Min");
  if (bars5.length === 0) return { sym, date, cls, error: "no 5m bars" };
  const g = gate(bars5, date);
  if (!g.admit) return { sym, date, cls, admit: false };
  const bars1 = fetchBars(sym, date, "1Min").filter((b) => b.t >= g.entryTime && b.t < `${date}${PM_END}`);
  if (bars1.length === 0) return { sym, date, cls, error: "no 1m bars" };
  const entry = g.entry;
  const pmLast = bars1[bars1.length - 1].c;
  const exit = limitExit(bars1, entry, LIMIT_GAIN);
  return {
    sym, date, cls, admit: true,
    entry, entryTime: g.entryTime,
    exitPx: exit.px, exitRet: exit.ret, filled: exit.filled, exitAt: exit.at,
    pmLastRet: pct(entry, pmLast),
  };
}

function loadHoldablePmOnly() {
  const lines = fs.readFileSync(TRACKER, "utf8").trim().split("\n").slice(1);
  const rows = [];
  for (const l of lines) {
    const f = l.split(",");
    if (f[3] === "none" && f[9] === "holdable") rows.push({ date: f[0], sym: f[1], cls: f[9] });
  }
  return rows;
}

const mean = (a) => (a.length ? a.reduce((s, x) => s + x, 0) / a.length : NaN);
const med = (a) => { if (!a.length) return NaN; const s = [...a].sort((x, y) => x - y); const m = s.length >> 1; return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };
const wins = (a) => a.filter((x) => x > 0).length;
const sum = (a) => a.reduce((s, x) => s + x, 0);
const sign = (x) => (x >= 0 ? "+" : "");

function main() {
  const argv = process.argv.slice(2);
  let cases;
  if (argv.length >= 2) cases = [{ sym: argv[0], date: argv[1], cls: "holdable" }];
  else cases = loadHoldablePmOnly();

  console.log("# Initiative 6 early-PM hypothetical-entry PILOT (LOG-ONLY, no orders)");
  console.log(`# universe: holdable footprint=none PM-only gappers from pm-open-scan.csv (n=${cases.length} candidates)`);
  console.log(`# entry: 5-min continuation gate (ignition >= ${TRADES_MIN} trades, R+1&R+2 hold >= ${HOLD_FRAC * 100 | 0}% high, VWAP non-declining), enter R+3 open`);
  console.log(`# exit: resting +${LIMIT_GAIN}% sell-limit (intrabar fill on 1-min bars), PM-last fallback; baseline = do-nothing = 0%\n`);
  console.log("date        sym    entry   entry_et  exit    fill    lim10   PM-last");

  const rets = [];
  const pmLastRets = [];
  const ledgerRows = [];
  let skipped = 0;
  for (const c of cases) {
    const r = sim(c.sym, c.date, c.cls);
    if (r.error) { console.log(`${c.date}  ${c.sym.padEnd(5)}  (${r.error})`); continue; }
    if (r.admit === false) { skipped++; continue; }
    // entry_et from UTC bar time (EDT = UTC-4)
    const hhmm = r.entryTime.slice(11, 16);
    const [hh, mm] = hhmm.split(":").map(Number);
    const etH = (hh - 4 + 24) % 24;
    const entryEt = `${String(etH).padStart(2, "0")}:${String(mm).padStart(2, "0")}`;
    console.log(
      `${r.date}  ${r.sym.padEnd(5)}  $${r.entry.toFixed(2).padStart(5)}  ${entryEt}     $${r.exitPx.toFixed(2).padStart(5)}  ${(r.filled ? "LIMIT" : "pmlast").padEnd(6)}  ${(sign(r.exitRet) + r.exitRet.toFixed(1) + "%").padStart(7)}  ${(sign(r.pmLastRet) + r.pmLastRet.toFixed(1) + "%").padStart(7)}`
    );
    rets.push(r.exitRet);
    pmLastRets.push(r.pmLastRet);
    ledgerRows.push([r.date, r.sym, r.entry.toFixed(4), entryEt, r.exitPx.toFixed(4), r.exitRet.toFixed(2), r.filled ? "limit" : "pmlast", r.pmLastRet.toFixed(2)].join(","));
  }

  const n = rets.length;
  console.log(`\n# Pilot result on ENTERED holdable names (n=${n}, ${skipped} candidates skipped by the gate):`);
  console.log(`  lim10 exit : SUM ${sign(sum(rets))}${sum(rets).toFixed(1)}%  mean ${sign(mean(rets))}${mean(rets).toFixed(1)}%  median ${sign(med(rets))}${med(rets).toFixed(1)}%  positive ${wins(rets)}/${n}`);
  console.log(`  PM-last    : SUM ${sign(sum(pmLastRets))}${sum(pmLastRets).toFixed(1)}%  mean ${sign(mean(pmLastRets))}${mean(pmLastRets).toFixed(1)}%  positive ${wins(pmLastRets)}/${n}  (hold-to-open floor, no peak-seek)`);
  console.log(`  baseline   : 0.0% (current live cycle enters none of these)`);
  console.log(`\n# Spread note: micro-cap PM round-trip ~1-3% (buy@ask/sell@bid). Net of ~2% the lim10 pilot edge is mean ${sign(mean(rets) - 2)}${(mean(rets) - 2).toFixed(1)}%/name.`);

  // Write the shadow ledger (overwrite; deterministic from the tracker).
  const header = "date,ticker,entry,entry_et,exit_px,exit_ret,exit_type,pm_last_ret";
  fs.writeFileSync(LEDGER, header + "\n" + ledgerRows.join("\n") + "\n");
  console.log(`\n# Shadow ledger written: ${path.relative(path.join(__dirname, ".."), LEDGER)} (${ledgerRows.length} entered rows)`);
}

main();
