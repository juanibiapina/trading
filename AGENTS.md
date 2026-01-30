# AGENTS.md

Agent instructions for this trading repo.

## Structure

- `Day Trading.md` - Main trading plan, workflows, and resources
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
