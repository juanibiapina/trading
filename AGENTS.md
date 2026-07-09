# AGENTS.md

Agent instructions for this trading repo.

## Getting Started

Always read `Day Trading.md` at the beginning of each conversation. It contains:
- Current trading plan and rules
- Entry/exit strategies
- Lessons learned from past trades

## Structure

- `Day Trading.md` - Main trading plan, workflows, and resources
- `knowledge/` - Reference documents
  - `Trading Plan Requirements.md` - Use when defining or updating the trading plan
- `log/YYYY-MM-DD/` - Daily trade log and morning analysis
- `log/weekly/YYYY-WNN/` - Weekly reviews (ISO week format)

## Trade Log

Trade logs live in `log/YYYY-MM-DD/` directories.

Each day's directory contains:
- `log.md` - Morning analysis, trade details, execution log
- `TICKER-HHMM.png` - Chart screenshots for each candidate (with capture time)

## Weekly Review

Weekly reviews live in `log/weekly/YYYY-WNN/` directories (e.g., `2026-W05`).

Each week's directory contains:
- `review.md` - Trade summary, P&L, rule violations, lessons learned
