#!/usr/bin/env node
/**
 * Send an HTML email via Gmail API using gmcli's OAuth credentials.
 *
 * Usage:
 *   node scripts/send-email.js --to EMAIL --subject SUBJECT --body "<h1>Hello</h1>"
 *   node scripts/send-email.js --to EMAIL --subject SUBJECT --body-file report.html
 */

const https = require("https");
const querystring = require("querystring");
const fs = require("fs");
const path = require("path");

// Parse args
const args = process.argv.slice(2);
let to = "", subject = "", body = "", bodyFile = "";

for (let i = 0; i < args.length; i++) {
  switch (args[i]) {
    case "--to": to = args[++i]; break;
    case "--subject": subject = args[++i]; break;
    case "--body": body = args[++i]; break;
    case "--body-file": bodyFile = args[++i]; break;
    default:
      console.error(`Unknown option: ${args[i]}`);
      process.exit(1);
  }
}

if (!to || !subject) {
  console.error("Usage: send-email.js --to EMAIL --subject SUBJECT --body HTML|--body-file FILE");
  process.exit(1);
}

if (bodyFile) {
  body = fs.readFileSync(bodyFile, "utf8");
}

if (!body) {
  console.error("Either --body or --body-file is required");
  process.exit(1);
}

// Load gmcli credentials
const accountsFile = path.join(require("os").homedir(), ".gmcli", "accounts.json");
const accounts = JSON.parse(fs.readFileSync(accountsFile, "utf8"));
const acct = accounts[0];
const { clientId, clientSecret, refreshToken } = acct.oauth2;
const from = acct.email;

function httpRequest(options, postData) {
  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      let body = "";
      res.on("data", (d) => (body += d));
      res.on("end", () => resolve({ status: res.statusCode, body }));
    });
    req.on("error", reject);
    if (postData) req.write(postData);
    req.end();
  });
}

async function getAccessToken() {
  const data = querystring.stringify({
    client_id: clientId,
    client_secret: clientSecret,
    refresh_token: refreshToken,
    grant_type: "refresh_token",
  });

  const res = await httpRequest({
    hostname: "oauth2.googleapis.com",
    path: "/token",
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  }, data);

  const json = JSON.parse(res.body);
  if (!json.access_token) throw new Error("Token error: " + res.body);
  return json.access_token;
}

async function sendEmail(token) {
  const raw = [
    `From: ${from}`,
    `To: ${to}`,
    `Subject: ${subject}`,
    "MIME-Version: 1.0",
    "Content-Type: text/html; charset=UTF-8",
    "",
    body,
  ].join("\r\n");

  const encoded = Buffer.from(raw).toString("base64url");
  const payload = JSON.stringify({ raw: encoded });

  const res = await httpRequest({
    hostname: "gmail.googleapis.com",
    path: "/gmail/v1/users/me/messages/send",
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  }, payload);

  if (res.status !== 200) {
    throw new Error(`Send failed (${res.status}): ${res.body}`);
  }

  const json = JSON.parse(res.body);
  console.log(`Sent: ${json.id}`);
}

async function main() {
  const token = await getAccessToken();
  await sendEmail(token);
}

main().catch((e) => {
  console.error(e.message);
  process.exit(1);
});
