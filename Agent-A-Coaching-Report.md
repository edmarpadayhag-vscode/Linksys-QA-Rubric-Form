# Agent A — Coaching Report
## Week of 2026-05-25 – 2026-05-31

---

## At a Glance
| Calls Handled | Avg Handle Time | Top Product | Top Problem | Cases Documented | Cases Escalated |
| --- | --- | --- | --- | --- | --- |
| 12 | 30m 44s | WHW03 | CONNECTIVITY | 11 | 8 |

## Work Mix Lens
- Escalation-heavy week: 10 TE-owned calls vs 3 LTS queue calls.
- Coach as an escalation owner: emphasize case progression, diagnostics, documentation, and L2-ready handoffs.

## Scorecard
| Dimension | This Week | Calls Reviewed |
| --- | --- | --- |
| Accuracy | 2.50 | 12 |
| Protocol | 1.60 | 12 |
| Communication | 2.20 | 12 |
| Overall | 2.20 | 12 |

## Where Time Goes
**Product Families**
| Family | Calls | Avg Handle Time | Avg Overall | Avg Accuracy | Avg Protocol | Avg Communication | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LN | 1 | 69m 55s | 2.80 | 2.00 | 2.00 | 2.00 | Outlier: 4.6x weekly median handle time |
| WHW | 4 | 50m 11s | 2.35 | 1.25 | 1.75 | 2.50 | Outlier: 3.3x weekly median handle time |
| MX | 2 | 27m 0s | 1.50 | 4.00 | 2.00 | 1.00 | Outlier: 1.8x weekly median handle time |
| MBE | 1 | 17m 15s | 3.00 | 4.00 | 2.00 | 2.00 |  |
| MR | 1 | 13m 17s | 3.20 | 5.00 | 3.00 | 2.00 |  |
| OTHER | 1 | 12m 51s | 1.50 | 5.00 | 2.00 | 2.00 |  |
| SPN | 1 | 11m 37s | 1.30 | 1.00 | 1.00 | 2.00 |  |
| EA | 1 | 3m 42s | 3.00 | 4.00 | 1.00 | 3.00 |  |

**Key Observations**
- LN is the slowest family at 69m 55s; outlier: 4.6x weekly median handle time.
- WHW is the slowest family at 50m 11s; outlier: 3.3x weekly median handle time.

**Problem Categories**
| Category | Calls | Avg Handle Time | Avg Overall | Avg Accuracy | Avg Protocol | Avg Communication | Focus Area? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CONNECTIVITY | 7 | 23m 36s | 2.20 | 3.00 | 1.70 | 2.10 | ✓ |
| SETUP | 4 | 41m 8s | 2.10 | 1.80 | 1.80 | 2.50 | ✓ |

## Week-over-Week Movement
- Accuracy moved up 0.92 vs. last week.
- Protocol moved down 0.25 vs. last week.
- Communication moved up 0.17 vs. last week.
- Average handle time moved down by 23m 47s.
- Family swing: MR handle time moved down by 46m 44s vs. last week.
- Family swing: MX handle time moved down by 20m 07s vs. last week.

## What Went Well
- **Accurate mesh recovery guidance**
  > "Guided customer to press the parent router's reset button five times consecutively to initiate discovery mode (5-press method)."
  #TE00100001

- **Remote session persistence**
  > "Persisted through a remote session and eventually resolved the connectivity issue."
  #TE00100002

---

## Growth Opportunities
- **Technical accuracy in LED interpretation**
  > "Provided incorrect default admin password ('admin admin') and mentioned non-existent LED color (magenta/pink)."
  #TE00100001
  *Next step: Confirm default credentials per KB and use only documented LED states.*

- **Verification before escalation**
  > "Failed to verify internet connectivity post-reset or guide through factory reset procedure."
  #LTS00100001
  *Next step: Always validate WAN connectivity and follow documented reset durations.*

---

## Next Week's Focus
- Practice LED state verification for Velop devices using only documented colors.
- Implement pre-escalation checks: WAN cable integrity, modem handshake, and factory reset confirmation.
- Standardize post-reset connectivity tests (speed test, DNS resolution) before closing cases.

---

## Technical Accuracy
**Improvement**
> Agent provided incorrect default admin password ('admin admin') instead of 'admin' as per KB.
#TE00100001 — Ensure default credentials match KB and avoid guesswork.

**Improvement**
> Agent incorrectly identified LED color as magenta/pink, which is not documented for Velop devices.
#TE00100001 — Reference only documented LED states (solid blue/purple/white/red).

**Improvement**
> Agent did not perform basic troubleshooting steps before suggesting paid support.
#LTS00100001 — Complete foundational checks before escalation.

**Improvement**
> Agent incorrectly instructed 5-press pairing method for SPNM57 device, which is not supported per KB.
#TE00100003 — Use app-based setup or pair button for SPNM series.

**Strength**
> Agent correctly applied 5-press reset method for Velop mesh pairing, aligning with KB guidance.
#TE00100001 — Continue using KB-aligned reset procedures.

---

## Coaching Moments
**Improvement**
> "Failed to verify the presence or functionality of the BT modem before advising connection."
#LTS00100002 — Always confirm modem status before guiding WAN setup.

**Improvement**
> "Did not guide the customer through the initial setup process (e.g., connecting to temporary Wi-Fi, accessing http://myrouter.local)."
#LTS00100002 — Document and follow setup wizard steps for new installations.

---

## Escalation Lessons: What L2 Did
### #TE00100001 — Resolved by Level 2
- **What L1 saw**: All child nodes solid red, customer unable to connect devices.
- **Why it escalated**: Exceeded threshold for mesh recovery attempts.
- **What L2 did**: Verified modem connectivity, guided 5-press reset, confirmed node LEDs to solid green/blue, validated Wi-Fi access.
- **L1 learning points**:
  1. Confirm modem internet access before node troubleshooting.
  2. Use 5-press method only for Velop/Cognitive Mesh; document LED changes.
  3. Verify device connectivity via Wi-Fi password test post-recovery.

### #TE00100004 — Resolved by Level 2
- **What L1 saw**: Customer lacked a computer for troubleshooting; laptop had no internet.
- **Why it escalated**: No device available for diagnostic steps.
- **What L2 did**: Advised callback, collected payment for paid support, provided self-help resources.
- **L1 learning points**:
  1. Always attempt mobile device troubleshooting if available.
  2. Schedule concrete callback times and document escalation rationale.
  3. Offer self-help KB links even when paid support is requested.

---

## Coach Appendix
- **Top trend**: Escalation-heavy week with frequent mesh and connectivity issues; improve pre-escalation diagnostics to reduce L2 handoffs.
- **Key pattern**: Inconsistent LED identification and incomplete verification steps leading to unresolved cases. Focus on KB-aligned troubleshooting and post-reset validation.

---

## This Week's Calls
| Case | Date | Score | Direction | Product | Category | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| #TE00100001 | 2026-05-25 | 2.8 | OUTBOUND | WHW01 | CONNECTIVITY | ✓ Resolved |
| #TE00100004 | 2026-05-27 | 3.0 | OUTBOUND | EA7430 | CONNECTIVITY | ✓ Likely resolved |
| #LTS00100002 | 2026-05-27 | 1.5 | INBOUND | MX4200 | CONNECTIVITY | ⏳ Pending |
| #TE00100002 | 2026-05-27 | 2.8 | OUTBOUND | LN11011202 | SETUP | ✓ Resolved |
| #TE00100005 | 2026-05-27 | 3.0 | INBOUND | MBE7000 | CONNECTIVITY | ✓ Likely resolved |
| #LTS00100003 | 2026-05-28 | 3.0 | INBOUND | WHW03 | SETUP | ✓ Likely resolved |
| #LTS00100001 | 2026-05-28 | 3.2 | INBOUND | MR8300 | CONNECTIVITY | ✓ Resolved |
| #TE00100006 | 2026-05-28 | — | OUTBOUND | MX2000 | SETUP | — |
| #TE00100007 | 2026-05-28 | 1.8 | INBOUND | WHW03 | SETUP | ⏳ Pending |
| #TE00100003 | 2026-05-29 | 1.3 | INBOUND | SPNM62CF | CONNECTIVITY | ⏳ Pending |
| #TE00100008 | 2026-05-29 | 1.5 | INBOUND | MDE7000 | CONNECTIVITY | ⏳ Pending |
| #TE00100008 | 2026-05-29 | 3.0 | OUTBOUND | — | CONNECTIVITY | Email promised |
