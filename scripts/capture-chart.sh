#!/bin/bash
# Capture a TradingView chart screenshot for a ticker
# Usage: ./capture-chart.sh TICKER [output_dir]

TICKER="${1:?Usage: capture-chart.sh TICKER [output_dir]}"
OUTPUT_DIR="${2:-/tmp}"
TIMESTAMP=$(date +%H%M)
OUTPUT_FILE="${OUTPUT_DIR}/${TICKER}-${TIMESTAMP}.png"

# TradingView chart URL with extended hours enabled
URL="https://www.tradingview.com/chart/?symbol=${TICKER}&interval=30"

echo "Capturing chart for ${TICKER}..."

# Open TradingView in a new tab
browse tab.new "$URL" > /dev/null 2>&1

# Wait for chart to load
sleep 3
browse wait.network --timeout 5000 > /dev/null 2>&1 || true

# Take screenshot
browse screenshot --output "$OUTPUT_FILE" > /dev/null 2>&1

# Close the tab
TAB_ID=$(browse tab.list 2>/dev/null | grep -o '"id":[0-9]*' | head -1 | grep -o '[0-9]*')
if [ -n "$TAB_ID" ]; then
  browse tab.close "$TAB_ID" > /dev/null 2>&1 || true
fi

if [ -f "$OUTPUT_FILE" ]; then
  echo "Saved: $OUTPUT_FILE"
else
  echo "Failed to capture chart for $TICKER"
  exit 1
fi
