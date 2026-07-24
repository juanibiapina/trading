#!/usr/bin/env node
/*
 * pm-gapper-exit-sim.js — Initiative 6, mechanical-exit test for the
 * continuation-gated PM-only-gapper scalp.
 *
 * LOG-ONLY. Places NO orders and changes no trading logic.
 *
 * Context (2026-07-23): pm-gapper-continuation-sim.js showed the continuation
 * gate admits the holdable gappers and the PMHigh reachable after a gated entry
 * is strongly positive (mean +31% on the admitted set), but holding to a fixed
 * PM-last / RegOpen exit gives most of it back (near flat / slightly negative).
 * The open question: how much of the PMHigh ceiling does a *mechanical, causal*
 * exit actually capture? This script answers it.
 *
 * It reuses the exact continuation gate (same TRADES_MIN / HOLD_FRAC / VWAP
 * rule) to fix the entry bar (R+3 open), then walks the premarket 5-min bars
 * from entry forward and applies several mechanical exits that use ONLY
 * information available at each bar (no lookahead):
 *
 *   - Trailing stop (close-based) at 8/12/15/20%: peak = max close since entry;
 *     exit at a bar's close once it closes <= peak*(1-width). Checking on closes
 *     avoids 5-min intrabar high/low ordering ambiguity and matches a bot that
 *     re-checks every 5 min.
 *   - N-bars hold (1/2/3): exit at the close of entry+N bars.
 *   - First-lower-high: exit at the close of the first bar whose high < the
 *     prior bar's high (momentum rollover).
 *
 * Benchmarks printed alongside: PMHigh (perfect-exit ceiling) and PM-last
 * (hold-to-09:25 floor), same as the continuation sim.
 *
 * Data: SIP 5-min bars via `node scripts/broker.js bars SYM --start ISO`.
 * Bars are UTC; EDT (summer) ET = UTC-4, so 08:00Z = 04:00 ET.
 *
 * Usage:
 *   node scripts/pm-gapper-exit-sim.js           # all footprint=none gappers
 *   node scripts/pm-gapper-exit-sim.js SYM DATE  # one ad-hoc case
 */

const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const TRACKER = path.join(__dirname, "..", "log", "pm-open-scan.csv");
const TRADES_MIN = 3000;
const HOLD_FRAC = 0.8;
const TRAIL_WIDTHS = [8, 12, 15, 20];
const NBARS = [1, 2, 3];

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

const pct = (from, to) => ((to - from) / from) * 100;

// Continuation gate — identical to pm-gapper-continuation-sim.js.
// Returns the premarket bar array and the entry index within it.
function gate(bars, date) {
  const pm = bars.filter((b) => b.t >= `${date}T08:00:00Z` && b.t < `${date}T13:30:00Z`);
  const rIdx = pm.findIndex((b) => b.trades >= TRADES_MIN);
  if (rIdx < 0) return { admit: false };
  if (rIdx + 3 >= pm.length) return { admit: false };
  const R = pm[rIdx], b1 = pm[rIdx + 1], b2 = pm[rIdx + 2];
  const hi1 = Math.max(R.h, b1.h);
  const hi2 = Math.max(hi1, b2.h);
  if (b1.c < HOLD_FRAC * hi1) return { admit: false };
  if (b2.c < HOLD_FRAC * hi2) return { admit: false };
  if (b2.vwap < b1.vwap * 0.98) return { admit: false };
  return { admit: true, pm, entryIdx: rIdx + 3 };
}

// Mechanical exits. Each returns { px, ret, at } from a causal walk of pmBars
// starting at entryIdx (entry price = open of entryIdx). `tail` is the last PM
// bar close used when a rule never triggers.
function trailingStop(pm, entryIdx, entry, widthPct) {
  const frac = 1 - widthPct / 100;
  let peak = pm[entryIdx].c; // peak of closes since entry
  for (let i = entryIdx; i < pm.length; i++) {
    const b = pm[i];
    // Update peak on this bar's close first, then test the stop on the close.
    if (b.c > peak) peak = b.c;
    if (b.c <= peak * frac && i > entryIdx) {
      return { px: b.c, ret: pct(entry, b.c), at: b.t };
    }
  }
  const last = pm[pm.length - 1];
  return { px: last.c, ret: pct(entry, last.c), at: last.t, held: true };
}

function nBars(pm, entryIdx, entry, n) {
  const i = Math.min(entryIdx + n, pm.length - 1);
  const b = pm[i];
  return { px: b.c, ret: pct(entry, b.c), at: b.t };
}

function firstLowerHigh(pm, entryIdx, entry) {
  let prevHigh = pm[entryIdx].h;
  for (let i = entryIdx + 1; i < pm.length; i++) {
    const b = pm[i];
    if (b.h < prevHigh) return { px: b.c, ret: pct(entry, b.c), at: b.t };
    prevHigh = b.h;
  }
  const last = pm[pm.length - 1];
  return { px: last.c, ret: pct(entry, last.c), at: last.t, held: true };
}

function sim(sym, date, cls) {
  const bars = fetchBars(sym, date);
  if (bars.length === 0) return { sym, date, cls, error: "no bars" };
  const g = gate(bars, date);
  if (!g.admit) return { sym, date, cls, admit: false };
  const { pm, entryIdx } = g;
  const entry = pm[entryIdx].o;
  // Benchmarks.
  const pmAfter = pm.slice(entryIdx);
  const pmHigh = Math.max(...pmAfter.map((b) => b.h));
  const pmLast = pm[pm.length - 1].c;
  const out = { sym, date, cls, admit: true, entry, entryTime: pm[entryIdx].t };
  out.pmHigh = { px: pmHigh, ret: pct(entry, pmHigh) };
  out.pmLast = { px: pmLast, ret: pct(entry, pmLast) };
  out.trail = {};
  for (const w of TRAIL_WIDTHS) out.trail[w] = trailingStop(pm, entryIdx, entry, w);
  out.nbar = {};
  for (const n of NBARS) out.nbar[n] = nBars(pm, entryIdx, entry, n);
  out.flh = firstLowerHigh(pm, entryIdx, entry);
  return out;
}

function loadPmOnly() {
  const lines = fs.readFileSync(TRACKER, "utf8").trim().split("\n").slice(1);
  const rows = [];
  for (const l of lines) {
    const f = l.split(",");
    if (f[3] === "none") rows.push({ date: f[0], sym: f[1], gap: f[2], cls: f[9] });
  }
  return rows;
}

const mean = (a) => (a.length ? a.reduce((s, x) => s + x, 0) / a.length : NaN);
const med = (a) => { if (!a.length) return NaN; const s = [...a].sort((x, y) => x - y); const m = s.length >> 1; return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };
const wins = (a) => a.filter((x) => x > 0).length;
const stat = (a) => (a.length ? `mean ${mean(a) >= 0 ? "+" : ""}${mean(a).toFixed(1)}%  median ${med(a) >= 0 ? "+" : ""}${med(a).toFixed(1)}%  win ${wins(a)}/${a.length}` : "n=0");
const cell = (x) => (x ? `${(x.ret >= 0 ? "+" : "") + x.ret.toFixed(1)}%`.padStart(7) : "   -   ");

function main() {
  const argv = process.argv.slice(2);
  let cases;
  if (argv.length >= 2) cases = [{ sym: argv[0], date: argv[1], gap: "?", cls: "?" }];
  else cases = loadPmOnly();

  console.log("# PM-only-gapper MECHANICAL-EXIT sim (Init 6, LOG-ONLY)");
  console.log(`# gate: ignition >= ${TRADES_MIN} trades, R+1&R+2 hold >= ${HOLD_FRAC * 100 | 0}% of running high, VWAP non-declining; enter R+3 open`);
  console.log("# all exits are causal (close-based); benchmarks: PMHigh = perfect ceiling, PM-last = hold-to-09:25 floor\n");

  const cols = ["PMHigh", "PM-last", "trail8", "trail12", "trail15", "trail20", "N1", "N2", "N3", "1stLH"];
  console.log("date        sym    cls          entry   " + cols.map((c) => c.padStart(7)).join(" "));

  const agg = {}; for (const c of cols) agg[c] = [];
  for (const c of cases) {
    const r = sim(c.sym, c.date, c.cls);
    if (r.error || r.admit === false) continue;
    // Skip names whose PM session is incomplete (reg pending) so exits are comparable.
    const row = [
      cell(r.pmHigh), cell(r.pmLast),
      cell(r.trail[8]), cell(r.trail[12]), cell(r.trail[15]), cell(r.trail[20]),
      cell(r.nbar[1]), cell(r.nbar[2]), cell(r.nbar[3]), cell(r.flh),
    ];
    console.log(`${r.date}  ${r.sym.padEnd(5)}  ${(r.cls || "").padEnd(11)}  $${r.entry.toFixed(2).padStart(5)}  ` + row.join(" "));
    agg["PMHigh"].push(r.pmHigh.ret);
    agg["PM-last"].push(r.pmLast.ret);
    agg["trail8"].push(r.trail[8].ret);
    agg["trail12"].push(r.trail[12].ret);
    agg["trail15"].push(r.trail[15].ret);
    agg["trail20"].push(r.trail[20].ret);
    agg["N1"].push(r.nbar[1].ret);
    agg["N2"].push(r.nbar[2].ret);
    agg["N3"].push(r.nbar[3].ret);
    agg["1stLH"].push(r.flh.ret);
  }

  console.log("\n# Aggregate on ADMITTED names:");
  for (const c of cols) console.log(`  ${c.padEnd(9)}: ${stat(agg[c])}`);
  console.log("\n# Spread cost reference: micro-cap PM round-trip ~1-3% (buy@ask/sell@bid). A rule must clear that AND beat PM-last to be worth a live pulse.");
}

main();
