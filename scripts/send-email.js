#!/usr/bin/env node
/**
 * Send an HTML email from juanibiapina@gmail.com with gog.
 *
 * Usage:
 *   node scripts/send-email.js --to EMAIL --subject SUBJECT --body "<h1>Hello</h1>"
 *   node scripts/send-email.js --to EMAIL --subject SUBJECT --body-file report.html
 */

const { execFileSync } = require("child_process");
const fs = require("fs");

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

try {
  const out = execFileSync(
    "gog",
    ["--no-input", "send", "--to", to, "--subject", subject, "--body-html-file", "-", "--json"],
    { input: body, encoding: "utf8", stdio: ["pipe", "pipe", "inherit"] },
  );
  const json = JSON.parse(out);
  console.log(`Sent: ${json.messageId || json.id}`);
} catch (e) {
  console.error(`Send failed: ${e.message}`);
  process.exit(1);
}
