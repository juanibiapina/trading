#!/usr/bin/env node
/*
 * init6-catastrophe-stop.js — LOG-ONLY analysis of adding a wide ~-15%
 * catastrophe-stop to the Initiative 6 pilot / Initiative 3 exit rule.
 *
 * The converged exit rule is a resting +10% sell-limit with a PM-last-close
 * fallback (init6-pm-pilot.js, peak-seeking-exit-sim.js). The +10% limit cannot
 * dodge the FADE tail: names that never reach +10% and bleed to a deep PM-last
 * (BIVI -27%, AEHL -33%). Juan's exit proposal lists an "optional wide ~-15%
 * catastrophe-stop"; this script quantifies whether promoting it from optional
 * to recommended improves the entered set NET, and — the decisive risk — whether
 * the stop prematurely exits any name that later filled the +10% limit.
 *
 * It reuses the EXACT pilot gate + universe (holdable footprint=none PM-only
 * gappers, plus holiday no-session unknowns) and walks 1-min SIP bars in time
 * order. Same-bar ambiguity (a bar whose HIGH>=+10% and LOW<=-15%) is resolved
 * conservatively to the STOP (worse case), so the stop's benefit is not
 * overstated.
 *
 * LOG-ONLY: no orders, no ledger writes, no live-pulse or strategy change.
 *
 * Usage: node scripts/init6-catastrophe-stop.js
 */

const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const TRACKER = path.join(__dirname, "..", "log", "pm-open-scan.csv");
const TRADES_MIN = 3000;
const HOLD_FRAC = 0.8;
const LIMIT_GAIN = 10;   // resting sell-limit width
let STOP_LOSS = 15;      // catastrophe-stop width (below entry); overridable via argv
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

// lim10-only: resting +10% sell-limit, PM-last fallback (current rule).
function exitLim10(min, entry) {
  const target = entry * (1 + LIMIT_GAIN / 100);
  for (const b of min) if (b.h >= target) return { ret: LIMIT_GAIN, kind: "limit" };
  return { ret: pct(entry, min[min.length - 1].c), kind: "pmlast" };
}

// lim10 + catastrophe-stop: whichever triggers first in time order. Same-bar
// ambiguity resolves to the stop (conservative) unless OPTIMISTIC (limit wins).
const OPTIMISTIC = process.argv.includes("--optimistic");
function exitLim10Stop(min, entry) {
  const target = entry * (1 + LIMIT_GAIN / 100);
  const floor = entry * (1 - STOP_LOSS / 100);
  for (const b of min) {
    const hitTarget = b.h >= target;
    const hitStop = b.l <= floor;
    if (hitTarget && hitStop) return OPTIMISTIC ? { ret: LIMIT_GAIN, kind: "limit" } : { ret: -STOP_LOSS, kind: "stop" };
    if (hitStop) return { ret: -STOP_LOSS, kind: "stop" };
    if (hitTarget) return { ret: LIMIT_GAIN, kind: "limit" };
  }
  return { ret: pct(entry, min[min.length - 1].c), kind: "pmlast" };
}

function loadHoldablePmOnly() {
  const lines = fs.readFileSync(TRACKER, "utf8").trim().split("\n").slice(1);
  const rows = [];
  for (const l of lines) {
    const f = l.split(",");
    const holidayPmOnly = f[3] === "unknown" && /holiday/i.test(l);
    if ((f[3] === "none" || holidayPmOnly) && f[9] === "holdable") rows.push({ date: f[0], sym: f[1] });
  }
  return rows;
}

const mean = (a) => (a.length ? a.reduce((s, x) => s + x, 0) / a.length : NaN);
const med = (a) => { if (!a.length) return NaN; const s = [...a].sort((x, y) => x - y); const m = s.length >> 1; return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };
const wins = (a) => a.filter((x) => x > 0).length;
const sum = (a) => a.reduce((s, x) => s + x, 0);
const sign = (x) => (x >= 0 ? "+" : "");

function main() {
  const arg = process.argv.slice(2).find((a) => /^\d+$/.test(a));
  if (arg) STOP_LOSS = +arg;
  const cases = loadHoldablePmOnly();
  console.log("# Init 6 pilot — catastrophe-stop analysis (LOG-ONLY, no orders)");
  console.log(`# entered = holdable footprint=none/holiday PM-only gappers passing the same continuation gate`);
  console.log(`# compare: lim10-only (current) vs lim10 + ${STOP_LOSS}% catastrophe-stop (stop wins same-bar ties)\n`);
  console.log("date        sym    entry   lim10     +stop15   note");

  const base = [], stop = [];
  let flipped = 0; // names the stop pulls out of a would-be +10% win
  for (const c of cases) {
    const bars5 = fetchBars(c.sym, c.date, "5Min");
    if (!bars5.length) continue;
    const g = gate(bars5, c.date);
    if (!g.admit) continue;
    const min = fetchBars(c.sym, c.date, "1Min").filter((b) => b.t >= g.entryTime && b.t < `${c.date}${PM_END}`);
    if (!min.length) continue;
    const a = exitLim10(min, g.entry);
    const b = exitLim10Stop(min, g.entry);
    base.push(a.ret);
    stop.push(b.ret);
    let note = "";
    if (a.kind === "limit" && b.kind === "stop") { note = "STOP PRE-EMPTS a +10% win (false stop)"; flipped++; }
    else if (a.ret < -STOP_LOSS && b.kind === "stop") note = `capped ${a.ret.toFixed(0)}% -> -${STOP_LOSS}%`;
    console.log(
      `${c.date}  ${c.sym.padEnd(5)}  $${g.entry.toFixed(2).padStart(5)}  ${(sign(a.ret) + a.ret.toFixed(1) + "%").padStart(7)}  ${(sign(b.ret) + b.ret.toFixed(1) + "%").padStart(7)}   ${note}`
    );
  }

  const n = base.length;
  console.log(`\n# n=${n} entered holdable names`);
  console.log(`  lim10-only : SUM ${sign(sum(base))}${sum(base).toFixed(1)}%  mean ${sign(mean(base))}${mean(base).toFixed(1)}%  median ${sign(med(base))}${med(base).toFixed(1)}%  positive ${wins(base)}/${n}`);
  console.log(`  lim10+stop : SUM ${sign(sum(stop))}${sum(stop).toFixed(1)}%  mean ${sign(mean(stop))}${mean(stop).toFixed(1)}%  median ${sign(med(stop))}${med(stop).toFixed(1)}%  positive ${wins(stop)}/${n}`);
  console.log(`  false stops (pulled a +10% win to -${STOP_LOSS}%): ${flipped}`);
  console.log(`\n# Net of ~2% micro-cap spread: lim10 ${sign(mean(base) - 2)}${(mean(base) - 2).toFixed(1)}%/name  vs  lim10+stop ${sign(mean(stop) - 2)}${(mean(stop) - 2).toFixed(1)}%/name`);
}

main();
