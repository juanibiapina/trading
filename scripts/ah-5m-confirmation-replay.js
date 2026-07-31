#!/usr/bin/env node
/*
 * ah-5m-confirmation-replay.js — Initiative 3 / Initiative 1 research.
 *
 * LOG-ONLY. Places no orders and changes no trading logic.
 *
 * Tests Juan's proposed AH-open entry: buy after the second or third 5-minute
 * price-plus-volume bar, rather than waiting for the current scan grid. The
 * local-volume gate compares each ticker with its own preceding bars, which
 * makes BOOM a named negative control.
 *
 * Causal gate:
 *   1. Ignition is the first green 5-minute bar that closes >=10% above the
 *      regular close, makes a new AH high, has >=20 trades, and volume >=2x
 *      the median of up to three preceding active bars.
 *   2. Second/third-bar confirmation must hold every intervening close within
 *      80% of the running high. The confirming close and volume must be at
 *      least the ignition bar's close and volume.
 *   3. Hypothetical entry is the next bar's open. PM return uses the next
 *      morning's SIP premarket high as an optimistic ceiling.
 *
 * The current-grid comparison uses the first entry-eligible scheduled scan at
 * or after confirmation (17:00, 17:30, 18:00, 18:30 ET). A pre-17:00 signal
 * therefore measures both cadence and the current entry-time rule's cost.
 *
 * Usage:
 *   node scripts/ah-5m-confirmation-replay.js
 *   node scripts/ah-5m-confirmation-replay.js SYM:YYYY-MM-DD:label [...]
 */

const { execFileSync } = require("child_process");
const path = require("path");
const BROKER = path.join(__dirname, "broker.js");

const PRICE_MIN = 1.10;
const VOLUME_JUMP = 2;
const MIN_TRADES = 20;
const HOLD_FRAC = 0.8;
const ENTRY_GRID_ET = ["17:00", "17:30", "18:00", "18:30"];

const DEFAULT_CASES = [
  ["AMIX", "2026-07-28", "winner"],
  ["NUWE", "2026-07-29", "winner"],
  ["KUST", "2026-07-30", "winner"],
  ["DCX", "2026-07-29", "continuation"],
  ["CRE", "2026-07-29", "fade"],
  ["BOOM", "2026-07-29", "fade-negative-control"],
  ["ONMD", "2026-07-28", "fade"],
  ["YIBO", "2026-07-28", "fade"],
  ["IOTR", "2026-07-28", "fade"],
  ["EGG", "2026-07-28", "fade"],
];

function fetchBars(sym, tf, start, limit = 300) {
  const out = execFileSync(
    "node",
    [BROKER, "bars", sym, "--tf", tf, "--start", start, "--limit", String(limit)],
    { encoding: "utf8" }
  );
  const rows = [];
  const re = /^(\S+)\s+O \$([\d.]+) H \$([\d.]+) L \$([\d.]+) C \$([\d.]+)\s+vol (\d+)\s+vwap \$([\d.]+)\s+trades (\d+)/;
  for (const line of out.split("\n")) {
    const m = line.match(re);
    if (!m) continue;
    rows.push({
      t: m[1], o: +m[2], h: +m[3], l: +m[4], c: +m[5],
      vol: +m[6], vwap: +m[7], trades: +m[8],
    });
  }
  return rows;
}

function median(xs) {
  const s = [...xs].sort((a, b) => a - b);
  const m = s.length >> 1;
  return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2;
}

function priorClose(sym, date) {
  const start = new Date(new Date(`${date}T00:00:00Z`).getTime() - 7 * 864e5)
    .toISOString().slice(0, 10);
  const row = fetchBars(sym, "1Day", start, 12).find((b) => b.t.slice(0, 10) === date);
  return row ? row.c : null;
}

function nextDate(date) {
  const d = new Date(`${date}T12:00:00Z`);
  do d.setUTCDate(d.getUTCDate() + 1); while (d.getUTCDay() === 0 || d.getUTCDay() === 6);
  return d.toISOString().slice(0, 10);
}

function etHM(t) {
  const d = new Date(new Date(t).getTime() - 4 * 3600e3);
  return `${String(d.getUTCHours()).padStart(2, "0")}:${String(d.getUTCMinutes()).padStart(2, "0")}`;
}

function hmMinutes(hm) {
  const [h, m] = hm.split(":").map(Number);
  return h * 60 + m;
}

function pct(from, to) { return ((to - from) / from) * 100; }

function ignitionIndex(ah, base) {
  for (let i = 1; i < ah.length; i++) {
    const prior = ah.slice(Math.max(0, i - 3), i).filter((b) => b.vol > 0);
    if (!prior.length) continue;
    const priorHigh = Math.max(...ah.slice(0, i).map((b) => b.h));
    const localRatio = ah[i].vol / median(prior.map((b) => b.vol));
    if (
      ah[i].c >= base * PRICE_MIN &&
      ah[i].c >= ah[i].o &&
      ah[i].h > priorHigh &&
      ah[i].trades >= MIN_TRADES &&
      localRatio >= VOLUME_JUMP
    ) return { i, localRatio };
  }
  return null;
}

function confirmation(ah, ign, offset) {
  const end = ign.i + offset;
  if (end + 1 >= ah.length) return null;
  let runningHigh = ah[ign.i].h;
  for (let i = ign.i + 1; i <= end; i++) {
    runningHigh = Math.max(runningHigh, ah[i].h);
    if (ah[i].c < runningHigh * HOLD_FRAC) return null;
  }
  const bar = ah[end];
  const ignition = ah[ign.i];
  if (bar.c < ignition.c || bar.vol < ignition.vol) return null;
  return { confirm: bar, entry: ah[end + 1] };
}

function gridEntry(ah, confirmationTime) {
  const confirmedAt = hmMinutes(etHM(confirmationTime)) + 5;
  const scan = ENTRY_GRID_ET.find((hm) => hmMinutes(hm) >= confirmedAt);
  if (!scan) return null;
  const bar = ah.find((b) => hmMinutes(etHM(b.t)) >= hmMinutes(scan));
  return bar ? { scan, bar } : null;
}

function analyze(sym, date, label) {
  const base = priorClose(sym, date);
  if (!base) return { sym, date, label, error: "regular close unavailable" };
  const start = `${date}T20:00:00Z`;
  const end = new Date(start).getTime() + 4 * 3600e3;
  const ah = fetchBars(sym, "5Min", start, 300).filter((b) => {
    const t = new Date(b.t).getTime();
    return t >= new Date(start).getTime() && t < end;
  });
  if (ah.length < 3) return { sym, date, label, error: `only ${ah.length} AH bars` };

  const ign = ignitionIndex(ah, base);
  if (!ign) return { sym, date, label, base, reject: "no local-volume new-high ignition" };

  const pmDate = nextDate(date);
  const pm = fetchBars(sym, "5Min", `${pmDate}T08:00:00Z`, 100)
    .filter((b) => b.t >= `${pmDate}T08:00:00Z` && b.t < `${pmDate}T13:30:00Z`);
  const pmHigh = pm.length ? Math.max(...pm.map((b) => b.h)) : null;
  const pmOpen = pm.length ? pm[0].o : null;
  const result = { sym, date, label, base, ign, ignBar: ah[ign.i], pmHigh, pmOpen, variants: {} };
  for (const [name, offset] of [["2bar", 1], ["3bar", 2]]) {
    const c = confirmation(ah, ign, offset);
    if (!c) { result.variants[name] = null; continue; }
    const grid = gridEntry(ah, c.confirm.t);
    result.variants[name] = {
      confirmTime: etHM(c.confirm.t), entryTime: etHM(c.entry.t), entry: c.entry.o,
      pmOpenReturn: pmOpen == null ? null : pct(c.entry.o, pmOpen),
      pmHighReturn: pmHigh == null ? null : pct(c.entry.o, pmHigh),
      gridTime: grid ? grid.scan : null,
      gridEntry: grid ? grid.bar.o : null,
      gridPmOpenReturn: grid && pmOpen != null ? pct(grid.bar.o, pmOpen) : null,
      priceEdge: grid ? pct(grid.bar.o, c.entry.o) * -1 : null,
    };
  }
  return result;
}

function fPct(x) { return x == null ? "   -  " : `${x >= 0 ? "+" : ""}${x.toFixed(1)}%`; }
function fVariant(v) {
  if (!v) return "reject".padEnd(35);
  const grid = v.gridEntry == null ? "grid n/a" : `grid $${v.gridEntry.toFixed(2)} open ${fPct(v.gridPmOpenReturn)}`;
  return `${v.entryTime} $${v.entry.toFixed(2)} open ${fPct(v.pmOpenReturn)} / hi ${fPct(v.pmHighReturn)} | ${grid}`.padEnd(54);
}

function main() {
  const args = process.argv.slice(2);
  const cases = args.length ? args.map((arg) => {
    const [sym, date, label = "?"] = arg.split(":");
    return [sym.toUpperCase(), date, label];
  }) : DEFAULT_CASES;

  console.log("# AH 5-minute second/third-bar confirmation replay (LOG-ONLY)");
  console.log(`# ignition: close >= +${((PRICE_MIN - 1) * 100).toFixed(0)}%, green new high, >=${MIN_TRADES} trades, local volume >=${VOLUME_JUMP}x; hold >=${HOLD_FRAC * 100}%`);
  console.log("date        sym    label                  ignition                 second-bar result                  third-bar result");

  const results = [];
  for (const c of cases) {
    try { results.push(analyze(...c)); }
    catch (e) { results.push({ sym: c[0], date: c[1], label: c[2], error: e.message.split("\n")[0] }); }
  }

  for (const r of results) {
    const left = `${r.date}  ${r.sym.padEnd(5)}  ${r.label.padEnd(21)}`;
    if (r.error) { console.log(`${left} ERROR ${r.error}`); continue; }
    if (r.reject) { console.log(`${left} reject: ${r.reject}`); continue; }
    const ib = r.ignBar;
    const ignition = `${etHM(ib.t)} ${r.ign.localRatio.toFixed(1)}x ${Math.round(ib.vol / 1000)}k`.padEnd(24);
    console.log(`${left} ${ignition} ${fVariant(r.variants["2bar"])} ${fVariant(r.variants["3bar"])}`);
  }

  for (const variant of ["2bar", "3bar"]) {
    const admitted = results.filter((r) => r.variants && r.variants[variant]);
    const winners = admitted.filter((r) => r.label === "winner");
    const fades = admitted.filter((r) => r.label.startsWith("fade"));
    const avg = (xs) => xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : NaN;
    const openReturns = admitted.map((r) => r.variants[variant].pmOpenReturn).filter((x) => x != null);
    const highReturns = admitted.map((r) => r.variants[variant].pmHighReturn).filter((x) => x != null);
    const edges = admitted.map((r) => r.variants[variant].priceEdge).filter((x) => x != null);
    console.log(`\n# ${variant}: admitted ${admitted.length}/${results.length}; winners ${winners.length}/3; fade false-positives ${fades.length}/6`);
    console.log(`  PM-open mean ${fPct(avg(openReturns))}; PM-high ceiling mean ${fPct(avg(highReturns))}; entry-price edge vs current legal grid mean ${fPct(avg(edges))}`);
  }
}

main();
