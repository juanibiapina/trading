#!/usr/bin/env node
/*
 * ah-crosscheck.js - SIP after-hours snapshot for names tracked tonight.
 *
 * Used by the final-scan feed-lag cross-check in prompts/post-market-scan.md.
 * For each symbol it prints the regular-session close, the latest SIP AH bar,
 * the AH high, AH volume and the change from the close. It pages through all
 * bars from 16:00 ET, so the latest bar is never cut off by a bar limit.
 * During a live session it leaves the request end open, because the free tier
 * rejects an end inside the last 15 minutes with a 403.
 *
 * Usage:
 *   node scripts/ah-crosscheck.js SYM [SYM ...] [--date YYYY-MM-DD]
 *     --date defaults to today's ET date.
 *
 * Env: ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_DATA_URL (same as broker.js).
 */

const DATA = process.env.ALPACA_DATA_URL || "https://data.alpaca.markets";
const HEADERS = {
  "APCA-API-KEY-ID": process.env.ALPACA_API_KEY,
  "APCA-API-SECRET-KEY": process.env.ALPACA_SECRET_KEY,
};

async function getBars(sym, params) {
  const out = [];
  let token = "";
  do {
    const qs = new URLSearchParams({ feed: "sip", limit: "10000" });
    for (const [k, v] of Object.entries(params)) if (v !== undefined) qs.set(k, v);
    if (token) qs.set("page_token", token);
    const res = await fetch(`${DATA}/v2/stocks/${sym}/bars?${qs}`, { headers: HEADERS });
    const body = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(`${res.status}: ${body.message || res.statusText}`);
    out.push(...(body.bars || []));
    token = body.next_page_token || "";
  } while (token);
  return out;
}

// 16:00 America/New_York on `date`, as a UTC ISO string (handles DST).
function ahStartUtc(date) {
  for (const h of [20, 21]) {
    const t = new Date(`${date}T${h}:00:00Z`);
    const ny = t.toLocaleString("en-US", { timeZone: "America/New_York", hour: "2-digit", hour12: false });
    if (Number(ny) === 16) return t.toISOString();
  }
  throw new Error(`cannot place 16:00 ET on ${date}`);
}

// The free tier rejects SIP requests whose end falls in the last 15 minutes
// (403 "subscription does not permit querying recent SIP data"). Inside that
// window the end is omitted, and Alpaca returns everything it can serve, as
// `broker.js bars` does.
const SIP_DELAY_MS = 16 * 60e3;
const liveEnd = (iso) => (new Date(iso).getTime() > Date.now() - SIP_DELAY_MS ? undefined : iso);

const pct = (a, b) => (b ? ((a / b - 1) * 100).toFixed(1) : "-");
const hhmm = (iso) => iso.slice(11, 16) + "Z";

async function main() {
  const args = process.argv.slice(2);
  const i = args.indexOf("--date");
  const date = i >= 0 ? args.splice(i, 2)[1]
    : new Date().toLocaleDateString("en-CA", { timeZone: "America/New_York" });
  const syms = args.map((s) => s.toUpperCase());
  if (!syms.length) throw new Error("usage: ah-crosscheck.js SYM [SYM ...] [--date YYYY-MM-DD]");
  const start = ahStartUtc(date);
  if (new Date(start).getTime() > Date.now() - SIP_DELAY_MS) throw new Error(`no completed SIP AH bars yet for ${date}`);
  const end = liveEnd(new Date(new Date(start).getTime() + 4 * 3600e3).toISOString());
  const dayEnd = liveEnd(`${date}T23:59:59Z`);

  console.log(`# SIP AH snapshot ${date}, from ${hhmm(start)}; now ${hhmm(new Date().toISOString())} ${end ? "" : "(live: SIP lags ~15 min)"}`);
  console.log("SYM     close    lastAH  at      AHhigh   AH%    hi%    AHvol      last4vol   trades4");
  const rows = await Promise.all(syms.map(async (s) => {
    try {
      const [day, ah] = await Promise.all([
        getBars(s, { timeframe: "1Day", start: `${date}T00:00:00Z`, end: dayEnd }),
        getBars(s, { timeframe: "5Min", start, end }),
      ]);
      let close = day.length ? day[day.length - 1].c : null;
      let mark = "";
      if (close === null) {
        // No daily bar served yet: use the last regular-session 5Min close, marked "*".
        const pre = await getBars(s, { timeframe: "5Min", start: new Date(new Date(start).getTime() - 6.5 * 3600e3).toISOString(), end: new Date(new Date(start).getTime() - 1e3).toISOString() });
        if (pre.length) { close = pre[pre.length - 1].c; mark = "*"; }
      }
      if (!ah.length) return `${s.padEnd(7)} ${close ?? "-"}  no AH bars`;
      const last = ah[ah.length - 1];
      const hi = Math.max(...ah.map((b) => b.h));
      const vol = ah.reduce((a, b) => a + b.v, 0);
      const tail = ah.slice(-4);
      const v4 = tail.reduce((a, b) => a + b.v, 0);
      const n4 = tail.reduce((a, b) => a + (b.n || 0), 0);
      return [s.padEnd(7), (String(close ?? "-") + mark).padEnd(8), String(last.c).padEnd(9), hhmm(last.t).padEnd(7),
        String(hi).padEnd(8), pct(last.c, close).padStart(6), pct(hi, close).padStart(6),
        String(vol).padStart(10), String(v4).padStart(10), String(n4).padStart(9)].join(" ");
    } catch (e) {
      return `${s.padEnd(7)} error: ${e.message}`;
    }
  }));
  for (const r of rows) console.log(r);
  if (rows.some((r) => /^\S+\s+[\d.]+\*/.test(r))) {
    console.log("* no SIP daily bar yet: close is the last regular-session 5Min bar's close, not the official closing print; check the scanner close");
  }
}

main().catch((e) => { console.error(e.message); process.exit(1); });
