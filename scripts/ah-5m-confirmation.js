#!/usr/bin/env node
/*
 * ah-5m-confirmation.js — Initiative 3 instrumentation (log-only; no orders).
 *
 * Reports whether a candidate satisfies the third-bar local-volume confirmation
 * gate tested in ah-5m-confirmation-replay.js. It is a scanner column only,
 * not an entry gate.
 *
 * Usage:
 *   node scripts/ah-5m-confirmation.js SYM:YYYY-MM-DD [SYM:YYYY-MM-DD ...]
 *        [--now HH:MM]
 */

const { execFileSync } = require("child_process");
const path = require("path");
const BROKER = path.join(__dirname, "broker.js");
const PRICE_MIN = 1.10;
const VOLUME_JUMP = 2;
const MIN_TRADES = 20;
const HOLD_FRAC = 0.8;

function bars(sym, tf, start, limit) {
  const out = execFileSync("node", [BROKER, "bars", sym, "--tf", tf, "--start", start, "--limit", String(limit)], { encoding: "utf8" });
  const rows = [];
  const re = /^(\S+)\s+O \$([\d.]+) H \$([\d.]+) L \$([\d.]+) C \$([\d.]+)\s+vol (\d+).*?trades (\d+)/;
  for (const line of out.split("\n")) {
    const m = line.match(re);
    if (m) rows.push({ t: m[1], o: +m[2], h: +m[3], l: +m[4], c: +m[5], vol: +m[6], trades: +m[7] });
  }
  return rows;
}

function median(xs) {
  const sorted = [...xs].sort((a, b) => a - b);
  const mid = sorted.length >> 1;
  return sorted.length % 2 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;
}

function etHM(t) {
  const d = new Date(new Date(t).getTime() - 4 * 3600e3);
  return `${String(d.getUTCHours()).padStart(2, "0")}:${String(d.getUTCMinutes()).padStart(2, "0")}`;
}

function minutes(hm) {
  const [h, m] = hm.split(":").map(Number);
  return h * 60 + m;
}

function priorClose(sym, date) {
  const start = new Date(new Date(`${date}T00:00:00Z`).getTime() - 7 * 864e5).toISOString().slice(0, 10);
  return bars(sym, "1Day", start, 12).find((bar) => bar.t.slice(0, 10) === date)?.c ?? null;
}

function analyze(sym, date, now) {
  const base = priorClose(sym, date);
  if (!base) return `${sym} ${date}  CONFIRM-3  NO-DATA prior close unavailable`;
  const start = `${date}T20:00:00Z`;
  const startMs = new Date(start).getTime();
  const ah = bars(sym, "5Min", start, 300).filter((bar) => {
    const t = new Date(bar.t).getTime();
    return t >= startMs && t < startMs + 4 * 3600e3 && (!now || minutes(etHM(bar.t)) <= minutes(now));
  });
  if (!ah.length) return `${sym} ${date}  CONFIRM-3  PENDING no AH bars${now ? ` as-of ${now}ET` : ""}`;

  for (let i = 1; i < ah.length; i++) {
    const prior = ah.slice(Math.max(0, i - 3), i).filter((bar) => bar.vol > 0);
    if (!prior.length) continue;
    const ratio = ah[i].vol / median(prior.map((bar) => bar.vol));
    const priorHigh = Math.max(...ah.slice(0, i).map((bar) => bar.h));
    const ignition = ah[i];
    if (!(ignition.c >= base * PRICE_MIN && ignition.c >= ignition.o && ignition.h > priorHigh && ignition.trades >= MIN_TRADES && ratio >= VOLUME_JUMP)) continue;

    const confirmIndex = i + 2;
    if (confirmIndex >= ah.length) return `${sym} ${date}  CONFIRM-3  PENDING ignition ${etHM(ignition.t)}ET; waiting for third bar${now ? ` as-of ${now}ET` : ""}`;
    let high = ignition.h;
    let held = true;
    for (let j = i + 1; j <= confirmIndex; j++) {
      high = Math.max(high, ah[j].h);
      if (ah[j].c < high * HOLD_FRAC) held = false;
    }
    const confirmed = ah[confirmIndex];
    if (held && confirmed.c >= ignition.c && confirmed.vol >= ignition.vol) {
      return `${sym} ${date}  CONFIRM-3  YES ignition ${etHM(ignition.t)}ET ${ratio.toFixed(1)}x; confirmed ${etHM(confirmed.t)}ET $${confirmed.c.toFixed(2)}${now ? ` as-of ${now}ET` : ""}`;
    }
    return `${sym} ${date}  CONFIRM-3  NO ignition ${etHM(ignition.t)}ET failed third-bar hold/volume${now ? ` as-of ${now}ET` : ""}`;
  }
  return `${sym} ${date}  CONFIRM-3  NO no local-volume new-high ignition${now ? ` as-of ${now}ET` : ""}`;
}

function main() {
  let now = null;
  const pairs = [];
  const args = process.argv.slice(2);
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--now") { now = args[++i]; continue; }
    if (/^[A-Za-z.\-]+:\d{4}-\d{2}-\d{2}$/.test(args[i])) {
      const [sym, date] = args[i].split(":");
      pairs.push([sym.toUpperCase(), date]);
    }
  }
  if (!pairs.length) {
    console.error("usage: node scripts/ah-5m-confirmation.js SYM:YYYY-MM-DD [...] [--now HH:MM]");
    process.exit(1);
  }
  console.log(`# third-bar confirmation (log-only)${now ? ` now<=${now}ET` : ""}`);
  for (const [sym, date] of pairs) {
    try { console.log(analyze(sym, date, now)); }
    catch (error) { console.log(`${sym} ${date}  CONFIRM-3  ERROR ${error.message.split("\n")[0]}`); }
  }
}

main();
