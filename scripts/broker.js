#!/usr/bin/env node
/*
 * broker.js - Alpaca paper-trading CLI (Initiative 2).
 *
 * Thin wrapper over the Alpaca REST API so the trading loops can submit/track
 * paper orders and read real fills, to compare against our assumed paper-trade
 * prices. Paper only. No deps (uses Node built-in fetch).
 *
 * Env (inherited from zero's .envrc):
 *   ALPACA_API_KEY, ALPACA_SECRET_KEY
 *   ALPACA_BASE_URL   (trading API, default https://paper-api.alpaca.markets)
 *   ALPACA_DATA_URL   (market data, default https://data.alpaca.markets)
 *
 * Usage:
 *   node scripts/broker.js account
 *   node scripts/broker.js positions
 *   node scripts/broker.js orders [open|closed|all]
 *   node scripts/broker.js order <id>
 *   node scripts/broker.js buy  <SYM> <qty> [--limit P] [--tif day|gtc] [--ext]
 *   node scripts/broker.js sell <SYM> <qty> [--limit P] [--tif day|gtc] [--ext]
 *      --ext = extended-hours (pre/post market). Requires --limit; forces tif=day.
 *   node scripts/broker.js cancel <id>
 *   node scripts/broker.js clock                # market clock: is_open + next open/close (ET)
 *   node scripts/broker.js quote <SYM>
 *   node scripts/broker.js bars  <SYM> [--tf 5Min] [--start ISO] [--limit N] [--feed sip|iex]
 *      feed defaults to sip (full-market volume, incl. real ext-hours); falls back
 *      to iex if the free tier blocks recent SIP data (~last 15 min).
 *   node scripts/broker.js tradable <SYM>     # is the asset tradable on Alpaca?
 *
 * Add --json to any command for raw JSON output.
 */

const TRADING = process.env.ALPACA_BASE_URL || "https://paper-api.alpaca.markets";
const DATA = process.env.ALPACA_DATA_URL || "https://data.alpaca.markets";
const KEY = process.env.ALPACA_API_KEY;
const SECRET = process.env.ALPACA_SECRET_KEY;

if (!KEY || !SECRET) {
  console.error("ERROR: ALPACA_API_KEY / ALPACA_SECRET_KEY not set in env.");
  process.exit(1);
}

const HEADERS = {
  "APCA-API-KEY-ID": KEY,
  "APCA-API-SECRET-KEY": SECRET,
  "Content-Type": "application/json",
};

async function api(base, path, opts = {}) {
  const res = await fetch(base + path, { headers: HEADERS, ...opts });
  const text = await res.text();
  let body;
  try { body = text ? JSON.parse(text) : {}; } catch { body = { raw: text }; }
  if (!res.ok) {
    const msg = body && body.message ? body.message : text;
    throw new Error(`${res.status} ${res.statusText}: ${msg}`);
  }
  return body;
}

// --- flag parsing ---------------------------------------------------------
function parseFlags(args) {
  const flags = {};
  const positional = [];
  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (a.startsWith("--")) {
      const name = a.slice(2);
      const next = args[i + 1];
      if (next === undefined || next.startsWith("--")) { flags[name] = true; }
      else { flags[name] = next; i++; }
    } else { positional.push(a); }
  }
  return { flags, positional };
}

const fmtUsd = (n) => (n === null || n === undefined || n === "" ? "-" : `$${Number(n).toFixed(2)}`);

// --- commands -------------------------------------------------------------
async function cmdAccount(flags) {
  const a = await api(TRADING, "/v2/account");
  if (flags.json) return console.log(JSON.stringify(a, null, 2));
  console.log(`Account ${a.account_number} (${a.status})  paper=${TRADING.includes("paper")}`);
  console.log(`Equity ${fmtUsd(a.equity)} | Cash ${fmtUsd(a.cash)} | Buying power ${fmtUsd(a.buying_power)}`);
  console.log(`Portfolio value ${fmtUsd(a.portfolio_value)} | PDT=${a.pattern_day_trader} | blocked=${a.trading_blocked}`);
}

async function cmdPositions(flags) {
  const ps = await api(TRADING, "/v2/positions");
  if (flags.json) return console.log(JSON.stringify(ps, null, 2));
  if (!ps.length) return console.log("No open positions.");
  for (const p of ps) {
    const pl = Number(p.unrealized_pl), plpc = Number(p.unrealized_plpc) * 100;
    console.log(`${p.symbol.padEnd(6)} ${p.qty.padStart(6)} @ ${fmtUsd(p.avg_entry_price)} | now ${fmtUsd(p.current_price)} | P&L ${pl >= 0 ? "+" : ""}${pl.toFixed(2)} (${plpc >= 0 ? "+" : ""}${plpc.toFixed(1)}%)`);
  }
}

async function cmdOrders(flags, positional) {
  const status = positional[0] || "open"; // open|closed|all
  const os = await api(TRADING, `/v2/orders?status=${status}&limit=50&direction=desc`);
  if (flags.json) return console.log(JSON.stringify(os, null, 2));
  if (!os.length) return console.log(`No ${status} orders.`);
  for (const o of os) {
    const fill = o.filled_avg_price ? ` filled@${fmtUsd(o.filled_avg_price)}` : "";
    console.log(`${o.id.slice(0, 8)} ${o.side.toUpperCase().padEnd(4)} ${o.qty.padStart(6)} ${o.symbol.padEnd(6)} ${o.type}/${o.time_in_force} ${o.status}${fill}`);
  }
}

async function cmdOrder(flags, positional) {
  const id = positional[0];
  if (!id) throw new Error("usage: order <id>");
  const o = await api(TRADING, `/v2/orders/${id}`);
  console.log(JSON.stringify(o, null, 2));
}

async function submit(side, flags, positional) {
  const [symbol, qtyStr] = positional;
  if (!symbol || !qtyStr) throw new Error(`usage: ${side} <SYM> <qty> [--limit P] [--tif day|gtc] [--ext]`);
  if (flags.ext && !flags.limit) throw new Error("--ext (extended hours) requires --limit (limit orders only)");
  const body = {
    symbol: symbol.toUpperCase(),
    qty: qtyStr,
    side,
    type: flags.limit ? "limit" : "market",
    time_in_force: flags.ext ? "day" : (flags.tif || "day"),
  };
  if (flags.limit) body.limit_price = String(flags.limit);
  if (flags.ext) body.extended_hours = true;
  const o = await api(TRADING, "/v2/orders", { method: "POST", body: JSON.stringify(body) });
  if (flags.json) return console.log(JSON.stringify(o, null, 2));
  console.log(`Submitted ${side} ${o.qty} ${o.symbol} (${o.type}/${o.time_in_force}) -> ${o.status}  id=${o.id}`);
}

async function cmdCancel(flags, positional) {
  const id = positional[0];
  if (!id) throw new Error("usage: cancel <id>");
  await api(TRADING, `/v2/orders/${id}`, { method: "DELETE" });
  console.log(`Canceled ${id}`);
}

async function cmdQuote(flags, positional) {
  const sym = (positional[0] || "").toUpperCase();
  if (!sym) throw new Error("usage: quote <SYM>");
  const q = await api(DATA, `/v2/stocks/${sym}/quotes/latest`);
  if (flags.json) return console.log(JSON.stringify(q, null, 2));
  const x = q.quote || {};
  console.log(`${sym}  bid ${fmtUsd(x.bp)} x${x.bs}  ask ${fmtUsd(x.ap)} x${x.as}  @ ${x.t}`);
}

async function cmdBars(flags, positional) {
  const sym = (positional[0] || "").toUpperCase();
  if (!sym) throw new Error("usage: bars <SYM> [--tf 5Min] [--start ISO] [--limit N] [--feed sip|iex]");
  const tf = flags.tf || "5Min";
  const limit = flags.limit || 20;
  const start = flags.start ? `&start=${encodeURIComponent(flags.start)}` : "";
  // Default to SIP (full consolidated tape incl. real extended-hours volume).
  // Free tier serves SIP historical but blocks the most recent ~15 min; on that
  // error, fall back to IEX so live/recent queries still return something.
  let feed = flags.feed || "sip";
  const path = (f) => `/v2/stocks/${sym}/bars?timeframe=${tf}&limit=${limit}&feed=${f}${start}`;
  let q;
  try {
    q = await api(DATA, path(feed));
  } catch (e) {
    if (feed === "sip" && !flags.feed && /recent SIP data/i.test(e.message)) {
      feed = "iex";
      q = await api(DATA, path(feed));
    } else {
      throw e;
    }
  }
  if (flags.json) return console.log(JSON.stringify(q, null, 2));
  const bars = q.bars || [];
  if (!bars.length) return console.log(`${sym}: no bars (feed=${feed}${feed === "iex" ? "; AH/PM may be sparse" : ""}).`);
  console.log(`# ${sym} feed=${feed}`);
  for (const b of bars) {
    const vw = b.vw !== undefined && b.vw !== null ? `  vwap ${fmtUsd(b.vw)}` : "";
    const n = b.n !== undefined && b.n !== null ? `  trades ${b.n}` : "";
    console.log(`${b.t}  O ${fmtUsd(b.o)} H ${fmtUsd(b.h)} L ${fmtUsd(b.l)} C ${fmtUsd(b.c)}  vol ${b.v}${vw}${n}`);
  }
}

async function cmdClock(flags) {
  const c = await api(TRADING, "/v2/clock");
  if (flags.json) return console.log(JSON.stringify(c, null, 2));
  console.log(`now ${c.timestamp} | is_open=${c.is_open} | next_open ${c.next_open} | next_close ${c.next_close}`);
}

async function cmdTradable(flags, positional) {
  const sym = (positional[0] || "").toUpperCase();
  if (!sym) throw new Error("usage: tradable <SYM>");
  const a = await api(TRADING, `/v2/assets/${sym}`);
  if (flags.json) return console.log(JSON.stringify(a, null, 2));
  console.log(`${sym}: tradable=${a.tradable} shortable=${a.shortable} fractionable=${a.fractionable} exchange=${a.exchange} class=${a.class} status=${a.status}`);
}

const COMMANDS = {
  account: cmdAccount, positions: cmdPositions, orders: cmdOrders, order: cmdOrder,
  buy: (f, p) => submit("buy", f, p), sell: (f, p) => submit("sell", f, p),
  cancel: cmdCancel, clock: cmdClock, quote: cmdQuote, bars: cmdBars, tradable: cmdTradable,
};

async function main() {
  const [cmd, ...rest] = process.argv.slice(2);
  const { flags, positional } = parseFlags(rest);
  const fn = COMMANDS[cmd];
  if (!fn) {
    console.error("Commands: " + Object.keys(COMMANDS).join(", "));
    console.error("Run with no args for usage in the file header.");
    process.exit(cmd ? 1 : 0);
  }
  try { await fn(flags, positional); }
  catch (e) { console.error("ERROR:", e.message); process.exit(1); }
}

main();
