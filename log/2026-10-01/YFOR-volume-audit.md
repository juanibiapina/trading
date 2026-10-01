# YFOR shared volume audit — 2026-09-16

Metric: `sip-ah-volume-v1`; SIP raw 5-minute shares; log-only.

Reconstructed through 2026-09-16T21:35:00+00:00; source fetched 2026-10-01T13:05:45.189085+00:00.
Historical reconstruction does not prove these bars were available live at their closing times.

Prior AH session: 2026-09-15, 48/48 observed slots; largest observed bar 1793140 shares.

Local ratio = current shares / median of the three preceding five-minute slots in this AH session.
Explicit zeros count; missing slots and a zero median yield an unknown ratio.
Prior ratio = current shares / prior AH maximum; unavailable unless all 48 prior slots are observed.
The 10x column reports a measurement; it does not authorize an entry.

| Bar start ET | Shares | Trades | Prior 3-slot median | Local ratio | Local >=10x | Prior AH peak ratio | Status |
|---|---:|---:|---:|---:|---|---:|---|
| 16:00 | 32,656 | 58 | unknown | unknown | unknown | 0.0182x | warmup |
| 16:05 | 13,653 | 52 | unknown | unknown | unknown | 0.0076x | warmup |
| 16:10 | 6,072 | 34 | unknown | unknown | unknown | 0.0034x | warmup |
| 16:15 | 11,026 | 60 | 13,653 | 0.8076x | false | 0.0061x | ok |
| 16:20 | 11,779 | 76 | 11,026 | 1.0683x | false | 0.0066x | ok |
| 16:25 | 31,755 | 109 | 11,026 | 2.8800x | false | 0.0177x | ok |
| 16:30 | 14,786 | 85 | 11,779 | 1.2553x | false | 0.0082x | ok |
| 16:35 | 25,735 | 135 | 14,786 | 1.7405x | false | 0.0144x | ok |
| 16:40 | 6,419 | 60 | 25,735 | 0.2494x | false | 0.0036x | ok |
| 16:45 | 12,659 | 76 | 14,786 | 0.8561x | false | 0.0071x | ok |
| 16:50 | 4,482 | 42 | 12,659 | 0.3541x | false | 0.0025x | ok |
| 16:55 | 21,890 | 126 | 6,419 | 3.4102x | false | 0.0122x | ok |
| 17:00 | 41,751 | 188 | 12,659 | 3.2981x | false | 0.0233x | ok |
| 17:05 | 24,264 | 168 | 21,890 | 1.1085x | false | 0.0135x | ok |
| 17:10 | 36,929 | 227 | 24,264 | 1.5220x | false | 0.0206x | ok |
| 17:15 | 154,414 | 588 | 36,929 | 4.1814x | false | 0.0861x | ok |
| 17:20 | 941,842 | 4509 | 36,929 | 25.5041x | true | 0.5252x | ok |
| 17:25 | 405,299 | 2057 | 154,414 | 2.6248x | false | 0.2260x | ok |
| 17:30 | 191,620 | 1346 | 405,299 | 0.4728x | false | 0.1069x | ok |
