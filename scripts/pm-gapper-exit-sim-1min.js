#!/usr/bin/env node
/*
 * pm-gapper-exit-sim-1min.js — Initiative 6, the deferred 1-MINUTE exit test
 * for the continuation-gated PM-only-gapper scalp.
 *
 * LOG-ONLY. Places NO orders and changes no trading logic.
 *
 * Context: pm-gapper-exit-sim.js (5-min cadence) found NO causal 5-min exit
 * turns the continuation-gate-admitted set positive after the ~1-3% spread. The
 * root cause it identified: the peak prints INTRABAR (e.g. INLF 08:15Z open
 * $3.76 -> $7.19 high within the same 5-min bar), uncapturable by a rule that
 * only sees 5-min closes. The only untested angle was a finer 1-MINUTE exit
 * that could sell the intrabar spike. The roadmap deferred this test until the
 * gate-admitted sample reached n>=12 so it doesn't hinge on one INLF. As of
 * 2026-08-17 the admitted set is n=12 (FRGT 08-13 added), so run it.
 *
 * Method: use the EXACT 5-min continuation gate (same TRADES_MIN / HOLD_FRAC /
 * VWAP rule) to pick admitted names, the entry bar (R+3 open) and entry price —
 * identical to the 5-min sim so results are directly comparable. Then fetch
 * 1-MINUTE SIP bars from the entry time forward (capped 13:30Z / 09:30 ET) and
 * apply causal 1-minute exits that use only info available at each 1-min bar:
 *
 *   - Trailing stop (close-based) at 8/12/15/20%: finer than 5-min, so it can
 *     lock a spike that a 5-min close would have already given back.
 *   - Resting sell-LIMIT at entry*(1+L%) for L in {10,15,20,30,50}: fills
 *     intrabar the first 1-min bar whose HIGH reaches the limit (models a GTC
 *     limit sitting above entry that catches the intrabar spike the 5-min close
 *     misses). This is the mechanism the 5-min sim structurally could not test.
 *
 * Benchmarks printed alongside: PMHigh (perfect-exit ceiling) and PM-last
 * (hold-to-09:25 floor) computed on the 1-min series after entry.
 *
 * Data: SIP bars via `node scripts/broker.js bars SYM --tf 1Min --start ISO`.
 * Bars are UTC; EDT (summer) ET = UTC-4, so 08:00Z = 04:00 ET.
 *
 * Usage:
 *   node scripts/pm-gapper-exit-sim-1min.js           # all footprint=none gappers
 *   node scripts/pm-gapper-exit-sim-1min.js SYM DATE  # one ad-hoc case
 */

const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const TRACKER = path.join(__dirname, "..", "log", "pm-open-scan.csv");
const TRADES_MIN = 3000;
const HOLD_FRAC = 0.8;
const TRAIL_WIDTHS = [8, 12, 15, 20];
const LIMIT_GAINS = [10, 15, 20, 30, 50];
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
    bars.push({
      t: m[1], o: +m[2], h: +m[3], l: +m[4], c: +m[5],
      vol: +m[6], vwap: +m[7], trades: +m[8],
    });
  }
  return bars;
}

const pct = (from, to) => ((to - from) / from) * 100;

// 5-min continuation gate — identical to pm-gapper-exit-sim.js.
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
  // entry = open of the R+3 5-min bar; entry time is that bar's timestamp.
  return { admit: true, entry: pm[rIdx + 3].o, entryTime: pm[rIdx + 3].t };
}

// 1-min trailing stop (close-based), causal walk from entry time.
function trailingStop1m(min, entry, widthPct) {
  const frac = 1 - widthPct / 100;
  let peak = min[0].c;
  for (let i = 0; i < min.length; i++) {
    const b = min[i];
    if (b.c > peak) peak = b.c;
    if (b.c <= peak * frac && i > 0) {
      return { px: b.c, ret: pct(entry, b.c), at: b.t };
    }
  }
  const last = min[min.length - 1];
  return { px: last.c, ret: pct(entry, last.c), at: last.t, held: true };
}

// Resting sell-limit at entry*(1+L%): fills intrabar on the first 1-min bar
// whose HIGH reaches the limit. If never reached, hold to PM-last.
function limitOnSpike(min, entry, gainPct) {
  const target = entry * (1 + gainPct / 100);
  for (let i = 0; i < min.length; i++) {
    const b = min[i];
    if (b.h >= target) {
      return { px: target, ret: gainPct, at: b.t, filled: true };
    }
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
  const pmHigh = Math.max(...bars1.map((b) => b.h));
  const pmLast = bars1[bars1.length - 1].c;
  const out = { sym, date, cls, admit: true, entry, entryTime: g.entryTime };
  out.pmHigh = { px: pmHigh, ret: pct(entry, pmHigh) };
  out.pmLast = { px: pmLast, ret: pct(entry, pmLast) };
  out.trail = {};
  for (const w of TRAIL_WIDTHS) out.trail[w] = trailingStop1m(bars1, entry, w);
  out.limit = {};
  for (const L of LIMIT_GAINS) out.limit[L] = limitOnSpike(bars1, entry, L);
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

  console.log("# PM-only-gapper 1-MINUTE exit sim (Init 6, LOG-ONLY, deferred test)");
  console.log(`# gate (5-min): ignition >= ${TRADES_MIN} trades, R+1&R+2 hold >= ${HOLD_FRAC * 100 | 0}% of running high, VWAP non-declining; enter R+3 open`);
  console.log("# exits walk 1-MIN bars from entry; trailN = close-based trailing stop, limL = resting sell-limit at entry*(1+L%) filled intrabar");
  console.log("# benchmarks: PMHigh = perfect ceiling, PM-last = hold-to-09:25 floor\n");

  const cols = ["PMHigh", "PM-last", "trail8", "trail12", "trail15", "trail20", "lim10", "lim15", "lim20", "lim30", "lim50"];
  console.log("date        sym    cls          entry   " + cols.map((c) => c.padStart(7)).join(" "));

  const agg = {}; for (const c of cols) agg[c] = [];
  const fills = {}; for (const L of LIMIT_GAINS) fills[L] = 0;
  let n = 0;
  for (const c of cases) {
    const r = sim(c.sym, c.date, c.cls);
    if (r.error || r.admit === false) continue;
    n++;
    const row = [
      cell(r.pmHigh), cell(r.pmLast),
      cell(r.trail[8]), cell(r.trail[12]), cell(r.trail[15]), cell(r.trail[20]),
      cell(r.limit[10]), cell(r.limit[15]), cell(r.limit[20]), cell(r.limit[30]), cell(r.limit[50]),
    ];
    console.log(`${r.date}  ${r.sym.padEnd(5)}  ${(r.cls || "").padEnd(11)}  $${r.entry.toFixed(2).padStart(5)}  ` + row.join(" "));
    agg["PMHigh"].push(r.pmHigh.ret);
    agg["PM-last"].push(r.pmLast.ret);
    for (const w of TRAIL_WIDTHS) agg[`trail${w}`].push(r.trail[w].ret);
    for (const L of LIMIT_GAINS) { agg[`lim${L}`].push(r.limit[L].ret); if (r.limit[L].filled) fills[L]++; }
  }

  console.log(`\n# Aggregate on ADMITTED names (n=${n}):`);
  for (const c of cols) console.log(`  ${c.padEnd(9)}: ${stat(agg[c])}`);
  console.log("\n# Limit fill rate (how often the resting sell-limit was reached intrabar):");
  for (const L of LIMIT_GAINS) console.log(`  lim${L}: filled ${fills[L]}/${n}`);
  console.log("\n# Spread cost reference: micro-cap PM round-trip ~1-3% (buy@ask/sell@bid). A rule must clear that AND beat PM-last to justify a 1-min monitoring pulse (higher cost than 5-min).");
}

main();
