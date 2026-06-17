# Agent C — Coaching Report
## Week of 2026-05-25 – 2026-05-31

---

## At a Glance
| Calls Handled | Avg Handle Time | Top Product | Top Problem | Cases Documented | Cases Escalated |
| --- | --- | --- | --- | --- | --- |
| 34 | 12m 3s | WHW03 | CONNECTIVITY | 34 | 2 |

## Work Mix Lens
- Frontline-heavy week: 34 LTS queue calls vs 2 TE-owned calls.
- Coach as a frontline agent: emphasize safe troubleshooting branches, closure hygiene, and clear customer-facing next steps.

## Scorecard
| Dimension | This Week | Calls Reviewed |
| --- | --- | --- |
| Accuracy | 2.70 | 34 |
| Protocol | 1.80 | 34 |
| Communication | 2.20 | 34 |
| Overall | 2.40 | 34 |

## Where Time Goes
**Product Families**
| Family | Calls | Avg Handle Time | Avg Overall | Avg Accuracy | Avg Protocol | Avg Communication | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MX | 11 | 24m 4s | 2.49 | 2.82 | 1.91 | 2.27 | Outlier: 1.9x weekly median handle time |
| MBE | 2 | 23m 42s | 3.15 | 4.00 | 2.00 | 2.50 | Outlier: 1.9x weekly median handle time |
| SPN | 3 | 17m 16s | 2.10 | 2.67 | 2.00 | 2.33 |  |
| WHW | 7 | 14m 50s | 2.20 | 2.57 | 1.71 | 2.00 |  |
| EA | 3 | 12m 38s | 1.83 | 1.33 | 1.33 | 1.67 |  |
| MR | 4 | 11m 24s | 2.15 | 1.75 | 1.50 | 1.75 |  |
| RE | 3 | 10m 33s | 2.07 | 2.00 | 1.33 | 1.67 |  |
| E | 3 | 6m 25s | 3.27 | 4.00 | 1.67 | 2.67 |  |
| LN | 1 | 6m 19s | 1.50 | 4.00 | 1.00 | 2.00 |  |

**Key Observations**
- MX is the slowest family at 24m 4s; outlier: 1.9x weekly median handle time.
- MBE is the slowest family at 23m 42s; outlier: 1.9x weekly median handle time.

**Problem Categories**
| Category | Calls | Avg Handle Time | Avg Overall | Avg Accuracy | Avg Protocol | Avg Communication | Focus Area? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CONNECTIVITY | 18 | 14m 45s | 2.20 | 2.60 | 1.80 | 2.10 | ✓ |
| SETUP | 9 | 11m 42s | 2.20 | 2.30 | 1.70 | 2.10 | ✓ |
| ACCESS | 5 | 11m 34s | 2.70 | 3.20 | 2.00 | 2.60 |  |
| CONFIGURATION | 1 | 4m 0s | 1.20 | 1.00 | 1.00 | 1.00 | ✓ |

## Week-over-Week Movement
- Overall moved up 0.32 vs. last week.
- Accuracy moved up 0.42 vs. last week.
- Protocol moved up 0.23 vs. last week.
- Average handle time moved up by 4m 56s.
- Family swing: SPN handle time moved up by 10m 19s vs. last week.
- Family swing: MBE handle time moved up by 9m 44s vs. last week.
- Family swing: EA handle time moved up by 6m 01s vs. last week.

## What Went Well
- **Correct identification of non-Linksys products**: Agent correctly identified the product as TP-Link Deco and referred customer to TP-Link support without providing incorrect technical guidance.
- **Effective troubleshooting and resolution confirmation**: Agent successfully guided customer through factory reset and 5-press pairing, confirming resolution with solid white lights and Wi-Fi connectivity.

## Growth Opportunities
- **Incorrect technical guidance and protocol violations**: Agent provided incorrect support URL (support.com instead of support.linksys.com), failed to follow standard troubleshooting flow, and advised factory reset without model-specific guidance.
- **PCI compliance violations and premature resolution claims**: Agent collected full credit card details over unsecured phone line (PCI violation) and prematurely declared resolution when node reverted to red LED.

## Next Week's Focus
- Improve protocol adherence, especially in model identification and troubleshooting flow.
- Address accuracy errors in technical guidance (e.g., incorrect URLs, unsupported methods).
- Enhance communication clarity and empathy, particularly during high-stress calls.
- Reduce PCI compliance violations and premature resolution claims.

## Technical Accuracy
**Improvement**
Agent provided incorrect support URL (support.com) instead of support.linksys.com, constituting a serious accuracy and safety risk.

**Improvement**
5-press calibration: WHW03 and MX5500 can support 5-press pairing/recovery in supported child-node contexts. Do not coach this as unsupported solely because the product is Velop, WHW, MX, or MR; treat it as an error only when the evidence shows the method was wrong for the model/state, described as a factory reset by itself, failed without a pivot, or contradicted KB guidance.

**Improvement**
Agent provided incorrect factory reset duration (20 seconds) for WHW03, contradicting KB guidance of 10 seconds.

**Improvement**
Agent provided materially false technical advice including 'new hard drive' and '50-50 chance of fix' for router issue, contradicting KB guidance.

**Strength**
Agent correctly identified non-Linksys product (TP-Link Deco) and appropriately referred customer to correct manufacturer support.

## Coaching Moments
No additional coaching moments were extracted after the technical review.

## Escalation Lessons: What L2 Did
### #TE00100001 — Resolved
- Call Outcome: Customer to verify modem internet connectivity (swap cable, test with another device) and contact ISP; case number provided for follow-up.
- Level 2 Resolution Steps:
  - 2026-05-25 15:50:11 — Escalate for exceeding threshold.
  - 2026-05-25 15:50:26 — Status: Resolved -> Escalated.
  - 2026-05-25 17:32:41 — Status: Escalated -> Callback | claimed case from the queue.
  - 2026-05-25 17:32:41 — Assignee changed.
  - 2026-05-25 18:24:57 — Callback with customer; verified issue - nodes were reset; guided through app setup; confirmed connectivity.
  - 2026-05-25 18:25:56 — Status: Callback -> Resolved.
- Current Status: Resolved

### #TE00100002 — Resolved
- Call Outcome: Escalated to Level 2; customer to send error screenshot via email; await callback within 24-48 hours.
- Level 2 Resolution Steps:
  - 2026-05-27 15:08:55 — Callback: account verification issue; link expired after 48h; informed customer to send screenshot; ticket endorsed for escalation (24-48h).
  - 2026-05-27 15:10:14 — Requested screenshots for verification issue.
  - 2026-05-27 15:10:21 — Assignee changed.
  - 2026-05-27 17:29:23 — Assignee changed (L2).
  - 2026-05-27 17:29:27 — Status: Escalated -> Callback.
  - 2026-05-27 20:13:35 — Callback: customer changed ISP to Spectrum; verification email link not working; discussed Linksys Smart WiFi account issue.
  - 2026-05-27 20:13:42 — Status: Callback -> Resolved.
- Current Status: Resolved

## Coach Appendix
Weekly pattern unavailable.
Focus points: Improve protocol adherence, especially in model identification and troubleshooting flow; address accuracy errors in technical guidance (e.g., incorrect URLs, unsupported methods); enhance communication clarity and empathy, particularly during high-stress calls.

## This Week's Calls
| Case | Date | Score | Direction | Product | Category | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| #LTS00100001 | 2026-05-25 | 1.30 | INBOUND | EA7300 | CONNECTIVITY | Customer to search for model number and find setup instructions online, despite being given an incorrect URL. |
| #TE00100001 | 2026-05-25 | 2.40 | INBOUND | WHW01 | CONNECTIVITY | Customer to verify modem internet connectivity (swap cable, test with another device) and contact ISP; case number provided for follow-up. |
| #LTS00100002 | 2026-05-25 | 3.00 | INBOUND | WHW01 | SETUP | Customer referred to TP-Link support hotline for further assistance with Deco mesh system. |
| #LTS00100003 | 2026-05-25 | 1.50 | INBOUND | SPNMX55 | CONNECTIVITY | None — call ended without resolution or redirection. |
| #LTS00100004 | 2026-05-26 | 3.00 | INBOUND | EA7300 | SETUP | Advised customer to contact Spectrum for on-site assistance; offered optional $15 paid support with no self-help alternative. |
| #LTS00100005 | 2026-05-26 | 1.10 | INBOUND | WHW03 | CONNECTIVITY | No resolution achieved. Agent did not confirm fix or establish a clear next step. |
| #LTS00100005 | 2026-05-26 | 1.50 | OUTBOUND | WHW03 | CONNECTIVITY | Customer to test the modem connection using a USB-to-Ethernet adapter or another device and contact the ISP if the issue persists. |
| #LTS00100006 | 2026-05-26 | 1.80 | INBOUND | RE7000 | SETUP | Relocate extender; paid support offered; customer may replace unit. |
| #LTS00100007 | 2026-05-26 | 1.80 | INBOUND | MX5500 | CONNECTIVITY | Customer to contact ISP (Spectrum) to register the Linksys router's MAC address or adjust firewall settings; agent to follow up if needed. |
| #LTS00100008 | 2026-05-27 | 3.00 | INBOUND | MBE7000 | CONNECTIVITY | Customer to factory-reset the parent node, re-add it, send logs, and consider a recovery reset if drops continue. |
| #LTS00100009 | 2026-05-27 | 4.00 | INBOUND | E2500 | CONNECTIVITY | Provided recommendation (MR5500) with price range and ordering method. |
| #TE00100002 | 2026-05-27 | 3.10 | INBOUND | MX8500 | ACCESS | Escalated to Level 2; customer to send error screenshot via email; await callback within 24-48 hours. |
| #LTS00100010 | 2026-05-27 | 3.00 | INBOUND | WHW03 | CONNECTIVITY | Customer declined paid support and will attempt factory reset independently; no further action scheduled. |
| #LTS00100011 | 2026-05-27 | 1.50 | INBOUND | LN1100 | SETUP | No resolution achieved. Customer should access http://myrouter.local for further troubleshooting. |
| #LTS00100012 | 2026-05-27 | 1.40 | INBOUND | RE7000 | SETUP | None provided. Customer left to self-troubleshoot without clear guidance. |
| #LTS00100013 | 2026-05-27 | 3.00 | INBOUND | MR8300 | CONNECTIVITY | No resolution provided. Customer stated she would call back. No next steps, KB articles, or escalation path offered. |
| #LTS00100013 | 2026-05-27 | 1.40 | INBOUND | MR8300 | CONNECTIVITY | No resolution. Incorrect advice given; issue unresolved. |
| #LTS00100013 | 2026-05-27 | 3.00 | INBOUND | MR8300 | CONNECTIVITY | Password reset completed; customer regained access to the router admin interface. Warranty start date updated. |
| #GI00100001 | 2026-05-28 | 3.00 | INBOUND | — | ACCESS | Customer will call back when near the router; agent will assist with recovery key and password reset at that time. |
| #LTS00100014 | 2026-05-28 | 1.80 | INBOUND | SPNMX57CF | SETUP | Customer to contact Community Fiber for hardware replacement of the faulty node. |
| #LTS00100015 | 2026-05-28 | 1.40 | INBOUND | WHW01 | SETUP | Customer advised to perform factory reset and use 'admin' as password; no successful login achieved or confirmed. |
| #LTS00100016 | 2026-05-28 | 3.00 | INBOUND | E5350 | CONNECTIVITY | Suggested factory reset or contacting ISP; no further steps taken. |
| #LTS00100017 | 2026-05-28 | 3.00 | INBOUND | SPNMX55CF | CONNECTIVITY | None — agent provided no actionable recommendation or path forward. |
| #LTS00100018 | 2026-05-28 | 1.20 | INBOUND | EA9300 | SETUP | Agent incorrectly closed the call without confirming router configuration or internet connectivity. |
| #LTS00100019 | 2026-05-28 | 1.90 | INBOUND | MX4200 | CONNECTIVITY | No valid resolution achieved. Node reverted to red LED. Customer left without a confirmed fix or clear next step. |
| #LTS00100020 | 2026-05-28 | 1.20 | INBOUND | MR8300 | CONFIGURATION | Customer left with incorrect instructions to use 'Lynx app'; no valid resolution path provided. |
| #LTS00100021 | 2026-05-28 | 3.00 | INBOUND | MX4200 | CONNECTIVITY | Customer directed to online KB for self-help; paid support offered but declined. |
| #LTS00100022 | 2026-05-28 | 1.80 | INBOUND | MX2000 | SETUP | Customer to retry setup after reset; if issue persists, call back for further assistance. |
| #GI00100001 | 2026-05-28 | 3.20 | INBOUND | MX2000 | ACCESS | Router admin password reset completed; access to router and app restored. |
| #LTS00100023 | 2026-05-29 | 3.00 | INBOUND | RE6500 | CONNECTIVITY | Call sister-company number for support. No confirmation of callback or tracking provided. |
| #LTS00100024 | 2026-05-29 | 1.30 | INBOUND | MX2000 | SETUP | No valid resolution or next step was provided. The customer did not receive the promised troubleshooting guide. |
| #LTS00100025 | 2026-05-29 | 2.80 | INBOUND | E900 | CONNECTIVITY | Customer advised to purchase a newer router (MR2000 or MR5500) and may contact for paid support if needed. No self-help resources provided. |
| #LTS00100026 | 2026-05-29 | 3.30 | INBOUND | MBE7000 | SETUP | Nodes re-paired and Wi-Fi is working; advise 10-minute wait before relocating nodes. |
| #LTS00100027 | 2026-05-29 | 3.90 | INBOUND | MX6200 | CONNECTIVITY | Admin password changed successfully; advise the customer to keep the new password safe. |
| #LTS00100028 | 2026-05-29 | 3.00 | INBOUND | MX6200 | CONNECTIVITY | Monitor Wi-Fi performance for 24-48 hours; reboot router if issues persist. |
| #LTS00100029 | 2026-05-29 | 3.10 | INBOUND | MX6200 | SETUP | Router appears functional post-reset with solid white light; customer believes internet is restored. Advised to monitor and contact support if issue recurs. |
| #LTS00100030 | 2026-05-29 | 3.00 | INBOUND | WHW03 | CONNECTIVITY | Advised customer to consult KB articles and consider paid support; no fix confirmed. |
| #LTS00100031 | 2026-05-29 | 1.30 | INBOUND | MX5300 | ACCESS | Customer to perform factory reset independently; no confirmation of fix or understanding. |
