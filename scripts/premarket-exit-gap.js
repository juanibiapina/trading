#!/usr/bin/env node
/*
 * premarket-exit-gap.js — Initiative 3 (execution pivot), exit-timing instrument.
 *
 * LOG-ONLY. Places NO orders and changes no trading logic.
 *
 * Context (2026-08-07 -> 2026-08-10): the execution-gap tally found that ~137%
 * of detected next-PM upside was lost to EXIT TIMING — held names whose PM
 * spikes fired well after our single 10:30 CET (04:30 ET) exit pulse but still
 * INSIDE premarket. That tally used hand-picked peak figures. This script sizes
 * the gap rigorously from real SIP 5-min bars, and — critically — caps the
 * measurement at the premarket close (09:30 ET / 13:30Z), because our rules
 * forbid holding into the regular session. So it answers the only question that
 * can justify an exit-pulse change: how much upside existed BETWEEN our actual
 * exit and the premarket open, that a later premarket exit could have captured?
 *
 * For each held name it reports:
 *   - exit ref     = our actual fill price/time (from the seed row)
 *   - PM peak-after = highest 5-min HIGH strictly after our exit and before
 *                     13:30Z (premarket only), with its time
 *   - PM-last       = last premarket bar close (09:25 ET floor)
 *   - gap%          = (PM peak-after - exit) / exit   (the capturable slice)
 *
 * Data: SIP 5-min bars via `node scripts/broker.js bars SYM --start ISO`.
 * Bars are UTC; EDT (summer) ET = UTC-4, so 08:00Z = 04:00 ET, 13:30Z = 09:30 ET.
 *
 * Usage:
 *   node scripts/premarket-exit-gap.js                     # all seed rows
 *   node scripts/premarket-exit-gap.js SYM DATE EXIT EXITZ # ad-hoc one name
 *     e.g. premarket-exit-gap.js PAVS 2026-08-06 6.65 2026-08-06T08:31:00Z
 */

const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const SEED = path.join(__dirname, "..", "log", "premarket-exit-gap.csv");
const PM_CLOSE_Z = "T13:30:00Z"; // 09:30 ET (EDT). Nothing at/after this counts.

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
    bars.push({ t: m[1], o: +m[2], h: +m[3], l: +m[4], c: +m[5], vol: +m[6], vwap: +m[7], trades: +m[8] });
  }
  return bars;
}

const pct = (from, to) => ((to - from) / from) * 100;
const etHHMM = (z) => {
  // z like 2026-08-06T10:55:00Z -> ET (EDT = UTC-4) HH:MM
  const d = new Date(z);
  const et = new Date(d.getTime() - 4 * 3600 * 1000);
  return `${String(et.getUTCHours()).padStart(2, "0")}:${String(et.getUTCMinutes()).padStart(2, "0")}ET`;
};

function analyze(row) {
  const bars = fetchBars(row.ticker, row.date);
  // Premarket window only: strictly after our exit, strictly before 13:30Z.
  const cutoffLo = row.exitZ;
  const cutoffHi = `${row.date}${PM_CLOSE_Z}`;
  const pm = bars.filter((b) => b.t > cutoffLo && b.t < cutoffHi);
  if (!pm.length) return { ...row, err: "no premarket bars after exit" };
  let peak = pm[0], last = pm[0];
  for (const b of pm) {
    if (b.h > peak.h) peak = b;
    if (b.t > last.t) last = b;
  }
  const gap = pct(row.exit, peak.h);
  const lastGap = pct(row.exit, last.c);
  return { ...row, peakH: peak.h, peakT: peak.t, lastC: last.c, gap, lastGap };
}

function loadSeed() {
  if (!fs.existsSync(SEED)) return [];
  return fs
    .readFileSync(SEED, "utf8")
    .split("\n")
    .filter((l) => l.trim() && !l.startsWith("#") && !l.startsWith("date,"))
    .map((l) => {
      const [date, ticker, entry, exit, exitZ, note] = l.split(",");
      return { date, ticker, entry: +entry, exit: +exit, exitZ, note: note || "" };
    });
}

function main() {
  const a = process.argv.slice(2);
  let rows;
  if (a.length >= 4) {
    rows = [{ date: a[1], ticker: a[0], entry: NaN, exit: +a[2], exitZ: a[3], note: "ad-hoc" }];
  } else {
    rows = loadSeed();
  }
  if (!rows.length) return console.log("No seed rows in log/premarket-exit-gap.csv and no ad-hoc args.");

  console.log("Premarket exit-timing gap — capturable upside between our exit and the PM open (09:30 ET)\n");
  console.log("ticker  exit@time         PMpeak-after    (time)     PM-last   gap%    to-last%");
  let sumGap = 0, n = 0;
  for (const r of rows) {
    const res = analyze(r);
    if (res.err) { console.log(`${r.ticker.padEnd(7)} ${String(r.exit).padEnd(8)} ${res.err}`); continue; }
    sumGap += Math.max(res.gap, 0);
    n++;
    console.log(
      `${r.ticker.padEnd(7)} $${String(r.exit).padEnd(7)} ${etHHMM(r.exitZ).padEnd(8)} ` +
        `$${res.peakH.toFixed(2).padEnd(6)} ${("(" + etHHMM(res.peakT) + ")").padEnd(11)} ` +
        `$${res.lastC.toFixed(2).padEnd(6)}  ${res.gap >= 0 ? "+" : ""}${res.gap.toFixed(1)}%  ${res.lastGap >= 0 ? "+" : ""}${res.lastGap.toFixed(1)}%`
    );
  }
  console.log(`\nPremarket exit-timing gap summed over ${n} held names: +${sumGap.toFixed(1)}%`);
  console.log("(gap = a *later premarket* exit at the post-exit PM peak vs our actual 04:31 ET exit;");
  console.log(" capped at 09:30 ET so it never counts regular-session prices we are barred from holding into.)");
}

main();
