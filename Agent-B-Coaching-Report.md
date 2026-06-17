# Agent B — Coaching Report
## Week of 2026-05-25 – 2026-05-31

---

## At a Glance
| Calls Handled | Avg Handle Time | Top Product | Top Problem | Cases Documented | Cases Escalated |
| --- | --- | --- | --- | --- | --- |
| 22 | 21m 26s | WHW03 | CONNECTIVITY | 22 | 1 |

## Work Mix Lens
- Frontline-heavy week: 25 LTS queue calls vs 1 TE-owned calls.
- Coach as a frontline agent: emphasize safe troubleshooting branches, closure hygiene, and clear customer-facing next steps.

## Scorecard
| Dimension | This Week | Calls Reviewed |
| --- | --- | --- |
| Accuracy | 2.60 | 22 |
| Protocol | 1.70 | 22 |
| Communication | 2.10 | 22 |
| Overall | 2.40 | 22 |

## Where Time Goes
**Product Families**
| Family | Calls | Avg Handle Time | Avg Overall | Avg Accuracy | Avg Protocol | Avg Communication | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MX | 7 | 49m 40s | 2.27 | 2.57 | 1.57 | 1.86 | Outlier: 2.7x weekly median handle time |
| WHW | 6 | 36m 30s | 3.00 | 2.00 | 1.83 | 2.50 | Outlier: 2.0x weekly median handle time |
| MBE | 1 | 21m 47s | 2.80 | 2.00 | 2.00 | 2.00 |  |
| MR | 4 | 14m 38s | 1.70 | 1.50 | 1.25 | 2.00 |  |
| E | 2 | 7m 30s | 2.25 | 3.00 | 1.50 | 2.00 |  |
| EA | 6 | 6m 30s | 2.55 | 3.50 | 1.83 | 1.83 |  |

**Key Observations**
- MX is the slowest family at 49m 40s; outlier: 2.7x weekly median handle time.
- WHW is the slowest family at 36m 30s; outlier: 2.0x weekly median handle time.

**Problem Categories**
| Category | Calls | Avg Handle Time | Avg Overall | Avg Accuracy | Avg Protocol | Avg Communication | Focus Area? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CONNECTIVITY | 13 | 27m 0s | 2.30 | 2.30 | 1.60 | 2.10 | ✓ |
| SETUP | 7 | 20m 29s | 2.30 | 2.70 | 1.90 | 2.00 | ✓ |
| ACCESS | 2 | 78m 7s | 1.30 | 1.00 | 1.50 | 2.00 | ✓ |

## Week-over-Week Movement
- Protocol moved down 0.17 vs. last week.
- Average handle time moved up by 11m 40s.
- Family swing: WHW handle time moved up by 24m 44s vs. last week.
- Family swing: MR handle time moved up by 5m 25s vs. last week.
- Family swing: EA handle time moved down by 3m 37s vs. last week.

## What Went Well
> **Accurate model identification and LED interpretation**
> Agent correctly identified MX4200 and interpreted solid blue LEDs as normal operation.
> #LTS00100001

> **Professional tone and closure hygiene**
> Maintained polite tone and provided clear next steps (emailing setup instructions) despite unresolved issues.
> #LTS00100002

---

## Growth Opportunities
> **Correct reset and pairing procedures for Velop (WHW/MX) models**
> *What better looks like*: Use 10-second reset (not 20) and avoid 5-press pairing; verify model before instructions.
> #LTS00100001 | #LTS00100003

> **Verify warranty status before paid support offers**
> *What better looks like*: Confirm eligibility via serial number lookup before charging; provide free self-help paths first.
> #LTS00100004 | #LTS00100005

---

## Next Week's Focus
1. Confirm product model and warranty status before any troubleshooting or paid support offer.
2. Use model-specific reset durations: 10s for Velop (WHW/MX), 20s only for MR/E-series.
3. Avoid 5-press pairing on WHW/MX/MR devices; use app/web UI for setup.
4. Validate LED states against KB before concluding resolutions (e.g., solid white = connected).

---

## Technical Accuracy
**Improvement**
Agent used 5-press pairing method on MBE7000, contradicted by KB for Velop nodes.
#LTS00100001

**Improvement**
Incorrect reset duration (20s vs KB-recommended 10-15s) for WHW03.
#LTS00100003

**Improvement**
Misstated solid green LED as connected (KB: solid white = connected for Velop).
#LTS00100006

**Strength**
Guided successful reset and re-pairing of Velop nodes to solid white LEDs.
#LTS00100001

---

## Coaching Moments
**Improvement**
Provided incorrect pairing method for MX8500 (not supported).
> "Status: Callback -> Resolved"
#LTS00100007

**Improvement**
Incorrect registration URL 'register.Linxies.com' (phishing risk).
> "Please register at register.Linxies.com"
#LTS00100005

---

## Escalation Lessons: What L2 Did
### #TE00100001 — Resolved by Level 2
- **What L1 saw**: Customer unable to access website via MX4200 mesh; works via ISP router.
- **Why it escalated**: Intermittent hangs/slow loads and access issues unresolved by L1.
- **What L2 did**:
  1. Verified WAN cable and modem connectivity.
  2. Performed 10s factory reset (correct duration).
  3. Guided app-based re-pairing and SSID/password reconfiguration.
  4. Validated solid blue LEDs and functional internet access.
- **Current state**: Resolved.
- **L1 learning points**:
  1. Use 10s reset for Velop; avoid 5-press pairing.
  2. Test internet access post-reset before closing.
  3. Document WAN status and LED states in case notes.

---

## Coach Appendix
- **Top trend**: Inconsistent reset/pairing procedures for Velop models driving prolonged handle times and unresolved issues.
- **Recurring pattern**: Premature paid support offers without basic troubleshooting or warranty verification.
- **Key evidence**: 4 calls with incorrect 5-press pairing/reset durations; 3 calls with unpaid support pushes before diagnostics.

---

## This Week's Calls
| Case | Date | Score | Direction | Product | Category | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| #LTS00100008 | 2026-05-25 | 3.00 | INBOUND | MR8300 | CONNECTIVITY | Customer declined path |
| #LTS00100001 | 2026-05-25 | 2.80 | INBOUND | MBE7000 | CONNECTIVITY | ✓ Likely resolved |
| #LTS00100004 | 2026-05-25 | 3.00 | INBOUND | WHW03 | CONNECTIVITY | Closed with self-help |
| #LTS00100003 | 2026-05-26 | 3.00 | INBOUND | WHW03 | CONNECTIVITY | ✓ Resolved |
| #LTS00100009 | 2026-05-26 | 3.00 | INBOUND | E5400 | CONNECTIVITY | Customer declined path |
| #LTS00100002 | 2026-05-26 | 2.80 | INBOUND | WHW03 | SETUP | Closed with self-help |
| #LTS00100006 | 2026-05-27 | 3.00 | INBOUND | WHW03 | CONNECTIVITY | Likely fixed unconfirmed |
| #LTS00100010 | 2026-05-27 | 1.00 | INBOUND | EA6400 | CONNECTIVITY | Abandoned or vague |
| #LTS00100010 | 2026-05-27 | 3.00 | INBOUND | EA6400 | CONNECTIVITY | Escalated correctly |
| #LTS00100011 | 2026-05-28 | 3.00 | INBOUND | MX4200 | ACCESS | Customer declined path |
| #LTS00100007 | 2026-05-28 | 1.10 | INBOUND | MX8500 | SETUP | Abandoned or vague |
| #LTS00100012 | 2026-05-28 | 3.00 | INBOUND | EA8300 | ACCESS | Closed with self-help |
| #LTS00100005 | 2026-05-28 | 1.60 | INBOUND | MR6350 | SETUP | Callback or followup set |
| #LTS00100013 | 2026-05-28 | 3.00 | INBOUND | WHW01 | SETUP | Closed with self-help |
| #LTS00100014 | 2026-05-28 | 3.00 | INBOUND | EA9500 | CONNECTIVITY | Abandoned or vague |
| #LTS00100015 | 2026-05-28 | 2.30 | INBOUND | EA7500 | ACCESS | Pending resolution |
| #TE00100001 | 2026-05-28 | 1.40 | INBOUND | MX4200 | ACCESS | Escalated correctly |
| #LTS00100016 | 2026-05-28 | 1.10 | INBOUND | MR5500 | CONNECTIVITY | Abandoned or vague |
| #LTS00100017 | 2026-05-29 | 3.00 | INBOUND | WHW03 | SETUP | Closed with self-help |
| #LTS00100018 | 2026-05-29 | 3.40 | INBOUND | MX4200 | SETUP | ✓ Resolved |
| #LTS00100019 | 2026-05-29 | 3.00 | INBOUND | MX2000 | SETUP | Abandoned or vague |
| #LTS00100020 | 2026-05-30 | 1.50 | INBOUND | E2500 | CONNECTIVITY | Abandoned or vague |
