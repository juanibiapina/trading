#!/usr/bin/env node
/*
 * init6-gate-denom-test.js — Initiative 6 gate sensitivity test (LOG-ONLY).
 *
 * Question: the continuation gate holds R+1/R+2 closes against the running
 * *high* of the ignition window. On wick-then-rebuild PM-only gappers (WVVIP
 * 08-25 +344%, RDIB 08-26 +67%) the ignition bar prints a tall wick, so its
 * HIGH sets a denominator the immediate next bar cannot hold, and the gate
 * rejects a name that in fact BUILDS to a plateau. Both were real holdables
 * skipped by the gate — a systematic false-negative on the biggest gappers.
 *
 * This test re-runs the exact gate with two hold-denominator modes and compares:
 *   - high  : running max of bar HIGHS (current gate)
 *   - close : running max of bar CLOSES (wick-tolerant variant)
 * over ALL footprint=none names, splitting admits by classification so we can
 * see whether relaxing to close-denominator (a) recovers holdable BUILDs
 * (WVVIP/RDIB) AND (b) does NOT start admitting the uninvestable wick-fades
 * (SXTC/LICN/ZCMD/DXST) the current gate correctly rejects.
 *
 * No orders. No change to the live pilot (init6-pm-pilot.js) or any trading
 * logic. Evidence only, to decide whether the gate's denominator should change.
 */

const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const TRACKER = path.join(__dirname, "..", "log", "pm-open-scan.csv");
const TRADES_MIN = 3000;
const HOLD_FRAC = 0.8;
const LIMIT_GAIN = 10;
const PM_END = "T13:30:00Z";

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

// Continuation gate parameterised by the hold denominator ("high" | "close").
function gate(bars5, date, denom) {
  const pm = bars5.filter((b) => b.t >= `${date}T08:00:00Z` && b.t < `${date}${PM_END}`);
  const rIdx = pm.findIndex((b) => b.trades >= TRADES_MIN);
  if (rIdx < 0) return { admit: false };
  if (rIdx + 3 >= pm.length) return { admit: false };
  const R = pm[rIdx], b1 = pm[rIdx + 1], b2 = pm[rIdx + 2];
  const lvl = (b) => (denom === "close" ? b.c : b.h);
  const hi1 = Math.max(lvl(R), lvl(b1));
  const hi2 = Math.max(hi1, lvl(b2));
  if (b1.c < HOLD_FRAC * hi1) return { admit: false };
  if (b2.c < HOLD_FRAC * hi2) return { admit: false };
  if (b2.vwap < b1.vwap * 0.98) return { admit: false };
  return { admit: true, entry: pm[rIdx + 3].o, entryTime: pm[rIdx + 3].t };
}

function limitExit(min, entry, gainPct) {
  const target = entry * (1 + gainPct / 100);
  for (const b of min) if (b.h >= target) return { ret: gainPct, filled: true };
  const last = min[min.length - 1];
  return { ret: pct(entry, last.c), filled: false };
}

function sim(sym, date, denom) {
  const bars5 = fetchBars(sym, date, "5Min");
  if (bars5.length === 0) return { admit: false, error: true };
  const g = gate(bars5, date, denom);
  if (!g.admit) return { admit: false };
  const bars1 = fetchBars(sym, date, "1Min").filter((b) => b.t >= g.entryTime && b.t < `${date}${PM_END}`);
  if (bars1.length === 0) return { admit: false, error: true };
  const exit = limitExit(bars1, g.entry, LIMIT_GAIN);
  return { admit: true, entry: g.entry, entryEt: etOf(g.entryTime), ret: exit.ret, filled: exit.filled };
}

function etOf(t) {
  const [hh, mm] = t.slice(11, 16).split(":").map(Number);
  return `${String((hh - 4 + 24) % 24).padStart(2, "0")}:${String(mm).padStart(2, "0")}`;
}

function loadNone() {
  const lines = fs.readFileSync(TRACKER, "utf8").trim().split("\n").slice(1);
  const rows = [];
  for (const l of lines) {
    const f = l.split(",");
    if (f[3] === "none") rows.push({ date: f[0], sym: f[1], cls: f[9] });
  }
  return rows;
}

const mean = (a) => (a.length ? a.reduce((s, x) => s + x, 0) / a.length : NaN);
const sum = (a) => a.reduce((s, x) => s + x, 0);
const wins = (a) => a.filter((x) => x > 0).length;
const sign = (x) => (x >= 0 ? "+" : "");

function run(denom, rows) {
  const holdRets = [], badRets = [];
  const admittedHold = [], admittedBad = [];
  for (const r of rows) {
    const s = sim(r.sym, r.date, denom);
    if (!s.admit) continue;
    if (r.cls === "holdable") { holdRets.push(s.ret); admittedHold.push(`${r.sym}(${sign(s.ret)}${s.ret.toFixed(0)}%)`); }
    else { badRets.push(s.ret); admittedBad.push(`${r.sym}/${r.cls}(${sign(s.ret)}${s.ret.toFixed(0)}%)`); }
  }
  console.log(`\n## denom=${denom}`);
  console.log(`  holdable admitted (n=${holdRets.length}): lim10 SUM ${sign(sum(holdRets))}${sum(holdRets).toFixed(1)}% mean ${sign(mean(holdRets))}${mean(holdRets).toFixed(1)}% pos ${wins(holdRets)}/${holdRets.length}`);
  console.log(`    ${admittedHold.join(" ")}`);
  console.log(`  NON-holdable admitted (false positives, n=${badRets.length}): lim10 SUM ${sign(sum(badRets))}${sum(badRets).toFixed(1)}% mean ${badRets.length ? sign(mean(badRets)) + mean(badRets).toFixed(1) + "%" : "-"}`);
  console.log(`    ${admittedBad.join(" ") || "(none — gate still rejects every uninvestable/thin wick-fade)"}`);
}

function main() {
  const rows = loadNone();
  console.log("# Initiative 6 gate hold-denominator sensitivity (LOG-ONLY, no orders)");
  console.log(`# footprint=none universe n=${rows.length}; entry gate ignition >= ${TRADES_MIN} trades, R+1&R+2 hold >= ${HOLD_FRAC * 100 | 0}% of running denom, VWAP non-declining; exit resting +${LIMIT_GAIN}% lim`);
  console.log("# GOAL: does close-denominator recover wick-then-rebuild holdables (WVVIP/RDIB) WITHOUT admitting uninvestable wick-fades?");
  run("high", rows);
  run("close", rows);
}

main();
