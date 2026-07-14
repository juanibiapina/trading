#!/usr/bin/env node
/*
 * pm-gapper-sim.js — Initiative 6, PM-only-gapper hypothetical-entry pilot.
 *
 * LOG-ONLY. Places NO orders and changes no trading logic. It quantifies
 * whether the holdable PM-only gappers logged by the `pm-open-scan` pulse
 * (the AH->PM scanner's blind spot) would have made money as hypothetical
 * paper trades, so we can decide whether to propose a live pulse to Juan.
 *
 * Model (mirrors the real pulse timing):
 *   - Entry: the `pm-open-scan` cron runs 11:00 CEST = 09:00Z = 05:00 ET.
 *     Hypothetical buy at the OPEN of the 09:00Z 5-min bar (detection time).
 *   - Exit rules compared:
 *       PM-last  : hold through premarket, sell at close of 09:25 ET (13:25Z).
 *       RegOpen  : sell at the regular-session open, 09:30 ET (13:30Z open).
 *       RegHigh  : best-case passive hold, regular-session high (context only).
 *       RegClose : sell at the regular-session close, 16:00 ET (context).
 *
 * Data: SIP 5-min bars via `node scripts/broker.js bars SYM --start ISO`.
 * Bars are UTC; in EDT (summer) ET = UTC-4.
 *
 * Usage:
 *   node scripts/pm-gapper-sim.js            # all holdable PM-only gappers in the tracker
 *   node scripts/pm-gapper-sim.js SYM DATE   # one ad-hoc case (DATE = YYYY-MM-DD)
 */

const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const TRACKER = path.join(__dirname, "..", "log", "pm-open-scan.csv");

function fetchBars(sym, date) {
  // date = YYYY-MM-DD; pull from 08:00Z (04:00 ET) through end of regular session.
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
      t: m[1],
      o: +m[2], h: +m[3], l: +m[4], c: +m[5],
      vol: +m[6], vwap: +m[7], trades: +m[8],
    });
  }
  return bars;
}

// hourZ like "09:00" -> find first bar whose UTC time >= that time on the date.
function barAt(bars, date, hhmm) {
  const target = `${date}T${hhmm}:00Z`;
  return bars.find((b) => b.t >= target) || null;
}

function regularSession(bars, date) {
  const open = `${date}T13:30:00Z`;
  const close = `${date}T20:00:00Z`;
  return bars.filter((b) => b.t >= open && b.t <= close);
}

function pct(from, to) {
  return ((to - from) / from) * 100;
}

function sim(sym, date) {
  const bars = fetchBars(sym, date);
  if (bars.length === 0) return { sym, date, error: "no bars" };

  const entryBar = barAt(bars, date, "09:00"); // 05:00 ET detection (current pulse time)
  if (!entryBar) return { sym, date, error: "no 09:00Z entry bar (volume died before detection)" };
  const entry = entryBar.o;

  // Early-detection scenario: enter at 04:10 ET (08:10Z), 2 bars after the 04:00
  // ramp confirms - quantifies the value of a hypothetical earlier PM pulse.
  const earlyBar = barAt(bars, date, "08:10");
  const early = earlyBar ? earlyBar.o : null;

  const pmLastBar = barAt(bars, date, "13:25"); // 09:25 ET
  const regOpenBar = barAt(bars, date, "13:30"); // 09:30 ET
  const reg = regularSession(bars, date);

  const res = { sym, date, entry, entryTime: entryBar.t, early };
  const pmLastPx = pmLastBar && pmLastBar.t < `${date}T13:30:00Z` ? pmLastBar.c : null;
  const regOpenPx = regOpenBar ? regOpenBar.o : null;
  const hi = reg.length ? Math.max(...reg.map((b) => b.h)) : null;
  const cl = reg.length ? reg[reg.length - 1].c : null;
  if (!reg.length) res.pending = true;

  const exits = (base) => ({
    pmLast: pmLastPx != null ? { px: pmLastPx, ret: pct(base, pmLastPx) } : null,
    regOpen: regOpenPx != null ? { px: regOpenPx, ret: pct(base, regOpenPx) } : null,
    regHigh: hi != null ? { px: hi, ret: pct(base, hi) } : null,
    regClose: cl != null ? { px: cl, ret: pct(base, cl) } : null,
  });
  Object.assign(res, exits(entry));
  res.earlyExits = early != null ? exits(early) : null;
  return res;
}

function loadHoldablePmOnly() {
  const lines = fs.readFileSync(TRACKER, "utf8").trim().split("\n").slice(1);
  const rows = [];
  for (const l of lines) {
    const f = l.split(",");
    if (f[9] === "holdable" && f[3] === "none") rows.push({ date: f[0], sym: f[1], gap: f[2] });
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
  if (argv.length >= 2) {
    cases = [{ sym: argv[0], date: argv[1], gap: "?" }];
  } else {
    cases = loadHoldablePmOnly();
  }

  console.log("# PM-only-gapper hypothetical-entry sim (Init 6, LOG-ONLY)");
  console.log("# entry = 09:00Z open (05:00 ET, pulse time); rets vs entry\n");
  console.log(
    "date        sym    gap     entry   PM-last          RegOpen          RegHigh          RegClose"
  );

  const agg = { pmLast: [], regOpen: [], regHigh: [], regClose: [] };
  const aggE = { pmLast: [], regOpen: [], regHigh: [], regClose: [] };
  for (const c of cases) {
    const r = sim(c.sym, c.date);
    if (r.error) {
      console.log(`${c.date}  ${c.sym.padEnd(5)}  ${String(c.gap).padStart(5)}   ERROR: ${r.error}`);
      continue;
    }
    console.log(
      `${r.date}  ${r.sym.padEnd(5)}  ${String(c.gap).padStart(5)}  $${r.entry.toFixed(2).padStart(5)}  ` +
        `${fmt(r.pmLast)}  ${fmt(r.regOpen)}  ${fmt(r.regHigh)}  ${fmt(r.regClose)}` +
        (r.pending ? "  (regular session pending)" : "")
    );
    if (r.pmLast) agg.pmLast.push(r.pmLast.ret);
    if (r.regOpen) agg.regOpen.push(r.regOpen.ret);
    if (r.regHigh) agg.regHigh.push(r.regHigh.ret);
    if (r.regClose) agg.regClose.push(r.regClose.ret);
    const e = r.earlyExits;
    if (e) {
      if (e.pmLast) aggE.pmLast.push(e.pmLast.ret);
      if (e.regOpen) aggE.regOpen.push(e.regOpen.ret);
      if (e.regHigh) aggE.regHigh.push(e.regHigh.ret);
      if (e.regClose) aggE.regClose.push(e.regClose.ret);
    }
  }

  const mean = (a) => (a.length ? (a.reduce((s, x) => s + x, 0) / a.length) : NaN);
  const show = (a) => (a.length ? `${mean(a) >= 0 ? "+" : ""}${mean(a).toFixed(1)}% (n=${a.length})` : "n=0");
  console.log("\n# Mean return, entry at 09:00Z / 05:00 ET (current pulse time):");
  console.log(`  PM-last (hold to 09:25 ET) : ${show(agg.pmLast)}`);
  console.log(`  RegOpen (sell 09:30 ET)    : ${show(agg.regOpen)}`);
  console.log(`  RegHigh (best-case hold)   : ${show(agg.regHigh)}`);
  console.log(`  RegClose (sell 16:00 ET)   : ${show(agg.regClose)}`);
  console.log("\n# Mean return, EARLY entry at 08:10Z / 04:10 ET (hypothetical earlier pulse):");
  console.log(`  PM-last (hold to 09:25 ET) : ${show(aggE.pmLast)}`);
  console.log(`  RegOpen (sell 09:30 ET)    : ${show(aggE.regOpen)}`);
  console.log(`  RegHigh (best-case hold)   : ${show(aggE.regHigh)}`);
  console.log(`  RegClose (sell 16:00 ET)   : ${show(aggE.regClose)}`);
}

main();
