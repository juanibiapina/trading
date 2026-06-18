#!/usr/bin/env node
/**
 * Send an HTML or plain-text email via InboxKit (sends as zero@inboxkit.cc).
 *
 * Drop-in replacement for send-email.js. Same CLI:
 *   node scripts/send-email-inboxkit.js --to EMAIL --subject SUBJECT --body "<h1>Hi</h1>"
 *   node scripts/send-email-inboxkit.js --to EMAIL --subject SUBJECT --body-file report.html
 *   node scripts/send-email-inboxkit.js --to EMAIL --subject SUBJECT --text "plain body"
 *
 * Credentials: reads INBOXKIT_API_KEY / INBOXKIT_EMAIL from the environment.
 * If absent (cron runs in the trading cwd without zero's env), it parses them
 * from zero's .envrc so there is a single source of truth for the key.
 */

const https = require("https");
const fs = require("fs");

const ENVRC = "/home/juan/Sync/notes/zero/.envrc";

function loadCreds() {
  let key = process.env.INBOXKIT_API_KEY;
  let email = process.env.INBOXKIT_EMAIL;
  if (key && email) return { key, email };
  try {
    const txt = fs.readFileSync(ENVRC, "utf8");
    const grab = (name) => {
      const m = txt.match(new RegExp(`^export ${name}=(.*)$`, "m"));
      if (!m) return undefined;
      return m[1].trim().replace(/^["']/, "").replace(/["']$/, "");
    };
    key = key || grab("INBOXKIT_API_KEY");
    email = email || grab("INBOXKIT_EMAIL");
  } catch (e) {
    // fall through to validation below
  }
  return { key, email };
}

const args = process.argv.slice(2);
let to = "", subject = "", body = "", bodyFile = "", text = "";
for (let i = 0; i < args.length; i++) {
  switch (args[i]) {
    case "--to": to = args[++i]; break;
    case "--subject": subject = args[++i]; break;
    case "--body": body = args[++i]; break;
    case "--body-file": bodyFile = args[++i]; break;
    case "--text": text = args[++i]; break;
    default:
      console.error(`Unknown option: ${args[i]}`);
      process.exit(1);
  }
}

if (!to || !subject) {
  console.error("Usage: send-email-inboxkit.js --to EMAIL --subject SUBJECT (--body HTML | --body-file FILE | --text PLAIN)");
  process.exit(1);
}
if (bodyFile) body = fs.readFileSync(bodyFile, "utf8");
if (!body && !text) {
  console.error("One of --body, --body-file, or --text is required");
  process.exit(1);
}

const { key, email } = loadCreds();
if (!key) {
  console.error(`INBOXKIT_API_KEY not found in env or ${ENVRC}`);
  process.exit(1);
}

const payload = { to, subject };
if (body) payload.html = body;
if (text) payload.text = text;
const data = JSON.stringify(payload);

const req = https.request({
  hostname: "inboxkit.cc",
  path: "/api/messages",
  method: "POST",
  headers: {
    "Authorization": `Bearer ${key}`,
    "Content-Type": "application/json",
    "Content-Length": Buffer.byteLength(data),
  },
}, (res) => {
  let out = "";
  res.on("data", (d) => (out += d));
  res.on("end", () => {
    if (res.statusCode >= 200 && res.statusCode < 300) {
      console.log(`Sent from ${email || "zero@inboxkit.cc"} to ${to}: ${out}`);
    } else {
      console.error(`InboxKit error ${res.statusCode}: ${out}`);
      process.exit(1);
    }
  });
});
req.on("error", (e) => { console.error(e); process.exit(1); });
req.write(data);
req.end();
