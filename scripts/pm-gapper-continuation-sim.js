#!/usr/bin/env node
/*
 * pm-gapper-continuation-sim.js — Initiative 6, PM-only-gapper entry with a
 * CONTINUATION GATE.
 *
 * LOG-ONLY. Places NO orders and changes no trading logic.
 *
 * Motivation (Juan, 2026-07-23, re SXTC +223%): "catch the winner of today."
 * The plain pm-gapper-sim (buy at a fixed pulse time, hold) closed NEGATIVE —
 * SXTC-type single-bar wicks drag the mean down. This script tests whether a
 * mechanical CONTINUATION GATE (enter only after price holds near the ignition
 * high for 2 consecutive bars, NOT on the opening wick) separates the holdable
 * gappers (INLF, MIMI, ...) from the wick-fades (SXTC, LICN, ZCMD) using only
 * bars available at decision time (no lookahead).
 *
 * Gate (real-time, causal):
 *   1. Ramp-start bar R = first PM bar (>=04:00 ET) with trades >= TRADES_MIN
 *      (the volume ignition; skips the thin pre-ramp drift on LICN/ZCMD).
 *   2. Continuation: bars R+1 and R+2 must EACH close >= HOLD_FRAC of the
 *      running high through that bar (price holds, does not roll over off a
 *      wick). VWAP must also be non-declining across R+1 -> R+2.
 *   3. If both hold -> ENTER at the open of R+3 (2 confirmed holding bars).
 *      If either fails -> SKIP (wick / fade detected, no entry).
 *
 * Exits measured from the gated entry: PM-last (09:25 ET), RegOpen (09:30 ET),
 * RegHigh (best-case), RegClose (16:00 ET).
 *
 * Data: SIP 5-min bars via `node scripts/broker.js bars SYM --start ISO`.
 * Bars are UTC; EDT (summer) ET = UTC-4, so 08:00Z = 04:00 ET.
 *
 * Usage:
 *   node scripts/pm-gapper-continuation-sim.js          # all footprint=none gappers
 *   node scripts/pm-gapper-continuation-sim.js SYM DATE # one ad-hoc case
 */

const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const TRACKER = path.join(__dirname, "..", "log", "pm-open-scan.csv");
const TRADES_MIN = 3000; // ignition volume floor (trades in the 5-min bar)
const HOLD_FRAC = 0.8; // close must stay >= 80% of running high to "hold"

function fetchBars(sym, date) {
  const start = `${date}T08:00:00Z`;
  let out;
  try {
    out = execFileSync(
      "node",
      [path.join(__dirname, "broker.js"), "bars", sym, "--tf", "5Min", "--start", start, "--limit", "300"],
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
    bars.push({
      t: m[1], o: +m[2], h: +m[3], l: +m[4], c: +m[5],
      vol: +m[6], vwap: +m[7], trades: +m[8],
    });
  }
  return bars;
}

function barAt(bars, date, hhmm) {
  const target = `${date}T${hhmm}:00Z`;
  return bars.find((b) => b.t >= target) || null;
}

function regularSession(bars, date) {
  const open = `${date}T13:30:00Z`;
  const close = `${date}T20:00:00Z`;
  return bars.filter((b) => b.t >= open && b.t <= close);
}

const pct = (from, to) => ((to - from) / from) * 100;

// Apply the continuation gate. Returns { admit, entry, entryTime, reason, rIdx }.
function gate(bars, date) {
  // Restrict to premarket bars (04:00-09:30 ET = 08:00Z-13:30Z) for the decision.
  const pm = bars.filter((b) => b.t >= `${date}T08:00:00Z` && b.t < `${date}T13:30:00Z`);
  const rIdx = pm.findIndex((b) => b.trades >= TRADES_MIN);
  if (rIdx < 0) return { admit: false, reason: "no ignition bar (volume never >= " + TRADES_MIN + " trades)" };
  if (rIdx + 3 >= pm.length) return { admit: false, reason: "not enough bars after ignition to confirm+enter" };

  const R = pm[rIdx];
  const b1 = pm[rIdx + 1];
  const b2 = pm[rIdx + 2];
  const entryBar = pm[rIdx + 3];

  const hi1 = Math.max(R.h, b1.h);
  const hi2 = Math.max(hi1, b2.h);
  const hold1 = b1.c >= HOLD_FRAC * hi1;
  const hold2 = b2.c >= HOLD_FRAC * hi2;
  const vwapOk = b2.vwap >= b1.vwap * 0.98; // allow tiny slip

  if (!hold1) return { admit: false, reason: `R+1 rolled over (C ${b1.c} < ${(HOLD_FRAC*100)|0}% of hi ${hi1.toFixed(2)})`, rIdx };
  if (!hold2) return { admit: false, reason: `R+2 rolled over (C ${b2.c} < ${(HOLD_FRAC*100)|0}% of hi ${hi2.toFixed(2)})`, rIdx };
  if (!vwapOk) return { admit: false, reason: `VWAP declining R+1 ${b1.vwap} -> R+2 ${b2.vwap}`, rIdx };

  return { admit: true, entry: entryBar.o, entryTime: entryBar.t, rIdx, rTime: R.t };
}

function sim(sym, date, cls) {
  const bars = fetchBars(sym, date);
  if (bars.length === 0) return { sym, date, cls, error: "no bars" };
  const g = gate(bars, date);
  const res = { sym, date, cls, admit: g.admit, reason: g.reason, entryTime: g.entryTime, rTime: g.rTime };
  if (!g.admit) return res;

  const entry = g.entry;
  res.entry = entry;
  const pmLastBar = barAt(bars, date, "13:25");
  const regOpenBar = barAt(bars, date, "13:30");
  const reg = regularSession(bars, date);
  const pmLastPx = pmLastBar && pmLastBar.t < `${date}T13:30:00Z` ? pmLastBar.c : null;
  const regOpenPx = regOpenBar ? regOpenBar.o : null;
  const hi = reg.length ? Math.max(...reg.map((b) => b.h)) : null;
  const cl = reg.length ? reg[reg.length - 1].c : null;
  if (!reg.length) res.pending = true;

  // PMHigh-after-entry: the best reachable PM exit if you scalp the peak instead
  // of holding (max high from the entry bar through 09:25 ET / 13:25Z).
  const pmAfter = bars.filter((b) => b.t >= g.entryTime && b.t < `${date}T13:30:00Z`);
  const pmHi = pmAfter.length ? Math.max(...pmAfter.map((b) => b.h)) : null;
  res.pmHigh = pmHi != null ? { px: pmHi, ret: pct(entry, pmHi) } : null;

  res.pmLast = pmLastPx != null ? { px: pmLastPx, ret: pct(entry, pmLastPx) } : null;
  res.regOpen = regOpenPx != null ? { px: regOpenPx, ret: pct(entry, regOpenPx) } : null;
  res.regHigh = hi != null ? { px: hi, ret: pct(entry, hi) } : null;
  res.regClose = cl != null ? { px: cl, ret: pct(entry, cl) } : null;
  return res;
}

function loadPmOnly() {
  const lines = fs.readFileSync(TRACKER, "utf8").trim().split("\n").slice(1);
  const rows = [];
  for (const l of lines) {
    // CSV has quoted notes fields; split only the leading fixed columns.
    const f = l.split(",");
    if (f[3] === "none") rows.push({ date: f[0], sym: f[1], gap: f[2], cls: f[9] });
  }
  return rows;
}

function fmt(x) {
  if (!x) return "     -  ";
  const s = (x.ret >= 0 ? "+" : "") + x.ret.toFixed(1) + "%";
  return `$${x.px.toFixed(2)} ${s.padStart(7)}`;
}

function main() {
  const argv = process.argv.slice(2);
  let cases;
  if (argv.length >= 2) cases = [{ sym: argv[0], date: argv[1], gap: "?", cls: "?" }];
  else cases = loadPmOnly();

  console.log("# PM-only-gapper CONTINUATION-GATE sim (Init 6, LOG-ONLY)");
  console.log(`# gate: ignition >= ${TRADES_MIN} trades, R+1 & R+2 hold >= ${HOLD_FRAC*100|0}% of running high, VWAP non-declining, enter R+3 open\n`);
  console.log("date        sym    gap    cls          gate    entry   PMHigh(scalp)    PM-last          RegOpen          RegHigh");

  const admitted = { pmHigh: [], pmLast: [], regOpen: [], regHigh: [], regClose: [] };
  const confusion = { admitHoldable: 0, admitBad: 0, rejectHoldable: 0, rejectBad: 0 };
  for (const c of cases) {
    const r = sim(c.sym, c.date, c.cls);
    if (r.error) { console.log(`${c.date}  ${c.sym.padEnd(5)}  ${String(c.gap).padStart(5)}  ${(c.cls||"").padEnd(11)}  ERROR: ${r.error}`); continue; }
    const holdable = c.cls === "holdable";
    if (r.admit) {
      console.log(
        `${r.date}  ${r.sym.padEnd(5)}  ${String(c.gap).padStart(5)}  ${(c.cls||"").padEnd(11)}  ADMIT   $${r.entry.toFixed(2).padStart(5)}  ` +
        `${fmt(r.pmHigh)}  ${fmt(r.pmLast)}  ${fmt(r.regOpen)}  ${fmt(r.regHigh)}` + (r.pending ? "  (reg pending)" : "")
      );
      if (r.pmHigh) admitted.pmHigh.push(r.pmHigh.ret);
      if (r.pmLast) admitted.pmLast.push(r.pmLast.ret);
      if (r.regOpen) admitted.regOpen.push(r.regOpen.ret);
      if (r.regHigh) admitted.regHigh.push(r.regHigh.ret);
      if (r.regClose) admitted.regClose.push(r.regClose.ret);
      if (holdable) confusion.admitHoldable++; else confusion.admitBad++;
    } else {
      console.log(`${r.date}  ${r.sym.padEnd(5)}  ${String(c.gap).padStart(5)}  ${(c.cls||"").padEnd(11)}  reject  — ${r.reason}`);
      if (holdable) confusion.rejectHoldable++; else confusion.rejectBad++;
    }
  }

  const mean = (a) => (a.length ? a.reduce((s, x) => s + x, 0) / a.length : NaN);
  const med = (a) => { if (!a.length) return NaN; const s=[...a].sort((x,y)=>x-y); const m=s.length>>1; return s.length%2? s[m] : (s[m-1]+s[m])/2; };
  const show = (a) => (a.length ? `mean ${mean(a)>=0?"+":""}${mean(a).toFixed(1)}%  median ${med(a)>=0?"+":""}${med(a).toFixed(1)}%  (n=${a.length})` : "n=0");
  console.log("\n# Return on ADMITTED names (gated entry at R+3 open):");
  console.log(`  PMHigh (scalp the peak)    : ${show(admitted.pmHigh)}`);
  console.log(`  PM-last (hold to 09:25 ET) : ${show(admitted.pmLast)}`);
  console.log(`  RegOpen (sell 09:30 ET)    : ${show(admitted.regOpen)}`);
  console.log(`  RegHigh (best-case hold)   : ${show(admitted.regHigh)}`);
  console.log(`  RegClose (sell 16:00 ET)   : ${show(admitted.regClose)}`);
  if (!argv.length || argv.length < 2) {
    console.log("\n# Gate vs human classification (does it keep holdables, drop wicks?):");
    console.log(`  ADMIT  holdable = ${confusion.admitHoldable}   ADMIT  non-holdable = ${confusion.admitBad}`);
    console.log(`  REJECT holdable = ${confusion.rejectHoldable}   REJECT non-holdable = ${confusion.rejectBad}`);
  }
}

main();
