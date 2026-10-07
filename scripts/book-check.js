#!/usr/bin/env node
/**
 * book-check.js — read-only extended-hours book diagnostic. Places no orders.
 *
 * `broker.js quote` shows Alpaca's free-plan latest quote, which comes from IEX.
 * IEX trades only 08:00–17:00 ET, so from 17:00 ET (the 23:00 CEST entry window)
 * that quote is frozen even when the consolidated book is live. This tool prints
 * the IEX quote beside the consolidated SIP book, with feed name, ET time and age.
 *
 * Live:       node scripts/book-check.js SYM [SYM...] [--refresh SEC] [--json]
 *             IEX latest quote plus the free 15-minute-delayed SIP latest quote
 *             (feed=delayed_sip). --refresh re-reads IEX once after SEC seconds (max 60).
 *             A delayed snapshot older than 45 min (15 min delay + 30 min lookback) is
 *             stale (BURU Oct 6 returned a pre-split Jul 17 quote); it is replaced by
 *             the last historical SIP quote before now-16min, labelled `sip-hist`.
 * Historical: node scripts/book-check.js SYM [SYM...] --at ISO [--json]
 *             Last SIP quote within 30 min and last IEX quote within 12 h at or
 *             before ISO. SIP history needs ISO to be at least ~15 minutes old.
 *
 * Env: ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_DATA_URL (optional).
 */

const DATA = process.env.ALPACA_DATA_URL || "https://data.alpaca.markets";
const KEY = process.env.ALPACA_API_KEY;
const SECRET = process.env.ALPACA_SECRET_KEY;
const FRESH_SEC = 60;
const SIP_LOOKBACK_MS = 30 * 60 * 1000;
const IEX_LOOKBACK_MS = 12 * 60 * 60 * 1000;
const SIP_DELAY_MS = 15 * 60 * 1000;
const SIP_STALE_SEC = (SIP_DELAY_MS + SIP_LOOKBACK_MS) / 1000;
const SIP_HIST_END_MS = 16 * 60 * 1000;

function parseArgs(argv) {
  const flags = {};
  const syms = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--json") flags.json = true;
    else if (a === "--at" || a === "--refresh") {
      if (i + 1 >= argv.length) throw new Error(`${a} needs a value`);
      flags[a.slice(2)] = argv[++i];
    } else if (a === "-h" || a === "--help") flags.help = true;
    else if (a.startsWith("-")) throw new Error(`unknown option ${a}`);
    else syms.push(a.toUpperCase());
  }
  return { flags, syms };
}

async function get(path) {
  const res = await fetch(`${DATA}${path}`, {
    headers: { "APCA-API-KEY-ID": KEY, "APCA-API-SECRET-KEY": SECRET },
  });
  const text = await res.text();
  let body;
  try { body = JSON.parse(text); } catch { body = null; }
  if (!res.ok) throw new Error((body && body.message) || text || `HTTP ${res.status}`);
  return body;
}

const etFmt = new Intl.DateTimeFormat("en-CA", {
  timeZone: "America/New_York", year: "numeric", month: "2-digit", day: "2-digit",
  hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false,
});
function fmtEt(iso) {
  const p = Object.fromEntries(etFmt.formatToParts(new Date(iso)).map((x) => [x.type, x.value]));
  return `${p.year}-${p.month}-${p.day} ${p.hour}:${p.minute}:${p.second} ET`;
}
function fmtAge(sec) {
  const s = Math.max(0, Math.round(sec));
  if (s < 60) return `${s}s`;
  if (s < 3600) return `${Math.floor(s / 60)}m${String(s % 60).padStart(2, "0")}s`;
  return `${Math.floor(s / 3600)}h${String(Math.floor((s % 3600) / 60)).padStart(2, "0")}m`;
}
const usd = (v) => `$${Number(v).toFixed(Number(v) < 1 ? 4 : 2)}`;

// Describe one quote relative to a reference time (now, or --at).
function describe(q, refMs) {
  if (!q || !q.t) return { present: false };
  const bp = Number(q.bp) || 0, bs = Number(q.bs) || 0;
  const ap = Number(q.ap) || 0, as = Number(q.as) || 0;
  const twoSided = bp > 0 && bs > 0 && ap > 0 && as > 0;
  let shape = twoSided ? "two-sided" : "one-sided/empty";
  if (twoSided && ap === bp) shape = "locked";
  if (twoSided && ap < bp) shape = "crossed";
  const spreadPct = twoSided && ap > bp ? ((ap - bp) / ap) * 100 : null;
  const ageSec = (refMs - Date.parse(q.t)) / 1000;
  return { present: true, bp, bs, ap, as, t: q.t, ageSec, twoSided, shape, spreadPct };
}

function line(sym, label, d) {
  if (d.error) return `${sym} BOOK ${label} unavailable: ${d.error}`;
  if (!d.present) return `${sym} BOOK ${label} no quote in window`;
  const spread = d.spreadPct === null ? "" : ` spread ${d.spreadPct.toFixed(2)}% of ask`;
  return `${sym} BOOK ${label} bid ${usd(d.bp)} x${d.bs} / ask ${usd(d.ap)} x${d.as} @ ${fmtEt(d.t)} age ${fmtAge(d.ageSec)} ${d.shape}${spread}`;
}

function verdict(iex, sip, sipLabel) {
  const iexOk = iex.present && !iex.error;
  const iexFresh = iexOk && iex.ageSec <= FRESH_SEC;
  const iexPart = !iexOk ? "IEX NONE" : iexFresh ? (iex.twoSided ? "IEX FRESH" : "IEX FRESH NOT-TWO-SIDED") : `IEX STALE ${fmtAge(iex.ageSec)}`;
  const sipOk = sip.present && !sip.error;
  let sipPart = !sipOk ? `${sipLabel} NONE` : sip.twoSided ? `${sipLabel} TWO-SIDED` : `${sipLabel} NOT-TWO-SIDED`;
  if (sip.staleSnapshot) sipPart = `SIP-15m STALE ${fmtAge(sip.staleSnapshot.ageSec)} -> ${sipPart}`;
  return `${iexPart}; ${sipPart}`;
}

async function latest(syms, feed) {
  try {
    const r = await get(`/v2/stocks/quotes/latest?symbols=${syms.join(",")}&feed=${feed}`);
    return { quotes: r.quotes || {} };
  } catch (e) {
    return { error: e.message };
  }
}

async function lastBefore(sym, feed, atMs, lookbackMs) {
  const start = new Date(atMs - lookbackMs).toISOString();
  const end = new Date(atMs).toISOString();
  try {
    const r = await get(`/v2/stocks/${sym}/quotes?start=${start}&end=${end}&feed=${feed}&limit=1&sort=desc`);
    return { quote: (r.quotes || [])[0] || null };
  } catch (e) {
    return { error: e.message };
  }
}

async function runLive(syms, flags) {
  const nowMs = Date.now();
  const [iex, sip] = await Promise.all([latest(syms, "iex"), latest(syms, "delayed_sip")]);
  const out = {};
  for (const s of syms) {
    const i = iex.error ? { error: iex.error } : describe(iex.quotes[s], nowMs);
    let p = sip.error ? { error: sip.error } : describe(sip.quotes[s], nowMs);
    let sipLabel = "SIP-15m";
    if (p.present && p.ageSec > SIP_STALE_SEC) {
      const h = await lastBefore(s, "sip", nowMs - SIP_HIST_END_MS, SIP_LOOKBACK_MS);
      const staleSnapshot = { t: p.t, ageSec: p.ageSec };
      p = { ...(h.error ? { error: h.error } : describe(h.quote, nowMs)), staleSnapshot };
      sipLabel = "SIP-hist";
    }
    out[s] = { observed_utc: new Date(nowMs).toISOString(), iex: i, delayed_sip: p, verdict: verdict(i, p, sipLabel) };
  }
  if (flags.refresh !== undefined) {
    const wait = Math.min(60, Math.max(0, Number(flags.refresh) || 0));
    await new Promise((r) => setTimeout(r, wait * 1000));
    const againMs = Date.now();
    const again = await latest(syms, "iex");
    for (const s of syms) {
      const r = again.error ? { error: again.error } : describe(again.quotes[s], againMs);
      const before = out[s].iex.t;
      const moved = !r.error && r.present && before && r.t !== before ? "advanced" : "unchanged";
      out[s].iex_refresh = { after_sec: wait, ...r, status: r.error ? "error" : moved };
    }
  }
  if (flags.json) return console.log(JSON.stringify(out, null, 2));
  for (const s of syms) {
    const o = out[s];
    console.log(line(s, "iex", o.iex));
    const st = o.delayed_sip.staleSnapshot;
    if (st) {
      console.log(`${s} BOOK sip-15m stale snapshot @ ${fmtEt(st.t)} age ${fmtAge(st.ageSec)} (older than ${fmtAge(SIP_STALE_SEC)}; replaced by sip-hist)`);
      console.log(line(s, "sip-hist", o.delayed_sip));
    } else console.log(line(s, "sip-15m", o.delayed_sip));
    if (o.iex_refresh) {
      const r = o.iex_refresh;
      console.log(r.error ? `${s} BOOK refresh +${r.after_sec}s iex error: ${r.error}` : `${s} BOOK refresh +${r.after_sec}s iex ${r.status}${r.present ? ` @ ${fmtEt(r.t)}` : ""}`);
    }
    console.log(`${s} BOOK verdict: ${o.verdict} (observed ${fmtEt(o.observed_utc)}; log-only)`);
  }
}

async function runAt(syms, flags) {
  const atMs = Date.parse(flags.at);
  if (Number.isNaN(atMs)) throw new Error(`--at is not a valid ISO time: ${flags.at}`);
  const out = {};
  for (const s of syms) {
    const [sipR, iexR] = await Promise.all([
      lastBefore(s, "sip", atMs, SIP_LOOKBACK_MS),
      lastBefore(s, "iex", atMs, IEX_LOOKBACK_MS),
    ]);
    const p = sipR.error ? { error: sipR.error } : describe(sipR.quote, atMs);
    const i = iexR.error ? { error: iexR.error } : describe(iexR.quote, atMs);
    out[s] = { at_utc: new Date(atMs).toISOString(), sip: p, iex: i, verdict: verdict(i, p, "SIP") };
  }
  if (flags.json) return console.log(JSON.stringify(out, null, 2));
  for (const s of syms) {
    const o = out[s];
    console.log(line(s, "sip", o.sip));
    console.log(line(s, "iex", o.iex));
    console.log(`${s} BOOK verdict at ${fmtEt(o.at_utc)}: ${o.verdict} (historical; log-only)`);
  }
}

async function main() {
  const { flags, syms } = parseArgs(process.argv.slice(2));
  if (flags.help || !syms.length) {
    console.log("Usage:\n  node scripts/book-check.js SYM [SYM...] [--refresh SEC] [--json]\n  node scripts/book-check.js SYM [SYM...] --at ISO [--json]");
    return;
  }
  if (!KEY || !SECRET) throw new Error("ALPACA_API_KEY / ALPACA_SECRET_KEY not set");
  if (flags.at !== undefined) return runAt(syms, flags);
  return runLive(syms, flags);
}

main().catch((e) => { console.error("ERROR:", e.message); process.exit(1); });
