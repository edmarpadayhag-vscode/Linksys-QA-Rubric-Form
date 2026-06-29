# Linksys Technical Support — QA Grading Rubric

**Audience:** Operations, Quality Assurance, Training  
**Purpose:** This document explains how agent calls are scored by the automated grading system and how to update the rubric when scoring guidance changes.

---

## How the Scoring System Works

Each call is evaluated across **five dimensions**. Every dimension receives a score from 1 to 5. An overall score is derived from those five scores.

The system uses four AI models in sequence: an initial scorer, an adversarial challenger, a gap-checker, and a final arbitrator. All four models are guided by this rubric. When you update this rubric, all four stages pick up the change on the next grading run.

---

## The Five Scoring Dimensions

| Dimension | What It Measures |
|-----------|-----------------|
| **RESOLUTION** | Did the customer's issue get identified and resolved? |
| **PROTOCOL** | Did the agent follow required Linksys support process? |
| **EFFICIENCY** | Did the agent move the call forward without unnecessary loops? |
| **ACCURACY** | Was the technical guidance correct per the Linksys KB? |
| **COMMUNICATION** | Was the agent clear, professional, empathetic, and easy to follow? |

---

## Scoring Scale

| Score | Label | What It Means |
|-------|-------|--------------|
| **5** | Excellent | Strong troubleshooting, correct guidance, clear structure, clean resolution or clearly managed next step. |
| **4** | Good | Operationally strong call with minor misses that do not materially harm the customer outcome. |
| **3** | Acceptable | Useful support with coachable gaps. The customer was still helped meaningfully even if the call was not clean or fully resolved. |
| **2** | Weak | Poor or incomplete support, but still at least partly functional. The agent made some real attempt to help; the execution or guidance was weak. |
| **1** | Failure | Use only for operational breakdown: almost no real troubleshooting, no meaningful help, materially wrong or misleading guidance, severe protocol failure, or a clear failure to manage outcome/next steps. |

**Calibration note:** The target operating range for normal coaching is **3 to 4.5**. Reserve `1` for genuine failures. Do not use `1` for every unresolved or incomplete call.

---

## Dimension Detail

### RESOLUTION

*Did the customer's actual issue get identified and resolved by the end of the call?*

**Score down when:**
- The customer leaves with the same problem and no concrete next step.
- The agent gives only a workaround without confirming it worked.
- The call ends before confirming the device, network, or app state.
- The outcome is vague, contradictory, or left open.

**Calibration:**
- Unresolved calls should rarely score above `4` — but they can score `3` or even `4` if the agent followed sound process and gave concrete, useful next steps.
- Unresolved calls should usually be `2` or `3`, not `1`, when the agent performed meaningful troubleshooting.
- Reserve `1` for calls that end with no meaningful progress, clearly wrong direction, or a breakdown in handling.
- A call that was technically resolved can still score poorly if the agent reached the outcome through wrong guidance or serious protocol failure.

**Concrete next steps that help RESOLUTION scoring:**
- Pointing the customer to a specific KB or support article.
- Telling the customer an email with detailed next steps will be sent.
- Setting a specific next step for escalation, replacement, follow-up testing, or continued troubleshooting.

---

### PROTOCOL

*Did the agent follow required Linksys support process?*

**Expected protocol behaviors:**
- Collect or confirm product model when relevant.
- Collect or confirm serial number when needed for warranty or device-specific troubleshooting.
- Verify warranty status when support eligibility, paid support, replacement, or escalation is discussed.
- Confirm customer identity/contact details when appropriate.
- Create, cite, or update the HappyFox case when available.
- Follow the correct escalation path instead of guessing.
- Clarify environment and credential access before starting procedures that depend on them.

**Especially meaningful protocol failures:**
- No case-management discipline when a case should clearly exist.
- No model confirmation before model-specific guidance.
- No warranty discussion when support path or paid support is central.
- Pushing forward despite unresolved credential/access confusion.

**Calibration:**
- Missing one or more relevant administrative fields should often produce `2` or `3`, not automatically `1`, if the agent still followed a mostly coherent support process.
- Reserve `1` for calls with multiple major process failures, missing required pathing, or protocol behavior that materially harms the support outcome.
- Relevance matters: for feature/how-to questions, model/serial/warranty are weighted lightly. For troubleshooting, warranty/RMA, escalation, or paid-support pathing, those fields matter much more.
- If the agent appears to already have prior-case or CRM details on screen, do not assume a protocol miss just because the agent did not ask the customer to repeat them.

---

### EFFICIENCY

*Did the agent move the call toward resolution without avoidable loops?*

**Score down when:**
- Long silence or excessive hold without explanation.
- Repeated questions the customer already answered.
- Registration, payment, or admin steps that delay basic troubleshooting.
- Repeated resets or path-switching without learning anything new.
- Failure to summarize next steps clearly.
- Agent lets the customer drive a chaotic call because the agent never takes control.

**Calibration:**
- Reserve `1` for severe looping, aimless handling, or clearly wasted call structure.
- Use `2` when the agent was inefficient but still moved the call forward in some meaningful way.
- Use `3` when the flow was imperfect or somewhat reactive but still practically useful.
- Use stronger markdowns when bad early diagnosis leads to 10–20+ minutes of avoidable wasted effort.

---

### ACCURACY

*Was the agent's technical advice correct and consistent with the Linksys KB?*

**Serious accuracy failures:**
- Wrong router access URL (e.g., `myrouter.local`, `192.168.1.1`).
- Wrong default password or login instruction.
- Wrong reset procedure.
- Wrong firmware, app, or product capability claim.
- Wrong LED interpretation.
- Wrong warranty or support-policy statement presented as fact.
- Wrong topology diagnosis that contradicts the transcript or KB.
- Advising settings changes without confirming product model or topology when that matters.
- Unsupported remote-session flows, unsupported websites, or unsafe domains.

**5-press pairing procedure calibration:**
The 5-press method is valid on **all Linksys mesh routers** (WHW, MX, MR series) **except** models with a dedicated Pair button (SPNM60, SPNM62, SPNM60TB, LN11xx, LN12xx — those use the Pair button instead). EA series routers are standalone; 5-press does not apply.
- Do NOT flag 5-press guidance as an error on any WHW, MX, or MR router without a Pair button.
- Only penalize when: (a) the model has a dedicated Pair button, or (b) the agent describes it as a factory reset (it is not).

**Calibration:**
- One clearly wrong technical instruction should usually cap ACCURACY around `3`, not automatically `1`, unless it is dangerous, materially misleading, or derails the case.
- Reserve `1` for materially wrong technical guidance, unsafe guidance, or repeated KB contradictions.
- Use `2` when guidance is questionable, incomplete, or insufficiently validated, but not clearly dangerous.

---

### COMMUNICATION

*Was the agent clear, professional, empathetic, and easy to follow?*

**Score down when:**
- Confusing or contradictory instructions.
- Talking over the customer.
- Excessive filler or rambling explanations.
- Giving multiple actions at once when the customer is already confused.
- Failure to acknowledge frustration.
- Poor call control.
- Ending without a clear recap or next step.

**Calibration:**
- Reserve `1` for severe confusion, call-control collapse, talking over the customer, or communication that materially blocks support.
- Use `2` when communication is weak, reactive, or unclear but still understandable enough that the call continues.
- Do not over-penalize lack of warmth or scripted empathy if the agent was clear, efficient, and useful.
- Efficient, correct, and useful support can still score well even if the tone is plain.
- **Do not penalize accent-characteristic phoneme patterns** (TH→D/T, B/V, P/F switching, pronoun gender mixing) unless there is clear evidence of customer comprehension failure. See the Accent & ASR section below.

---

## Cross-Cutting Guidance

### Paid Support & Warranty

Paid support can be appropriate, but it should not replace basic triage or create avoidable customer frustration.

**Penalize when:**
- The agent pushes paid support before understanding the issue.
- The agent repeats the paid support offer after refusal without adding value.
- The agent blocks safe basic guidance behind payment.
- The agent explains warranty or support eligibility incorrectly.

**Do not penalize** simply because the device is out of warranty or the call does not convert to paid support.

For out-of-warranty calls where the customer declines paid support, handling can still be good if the agent provides at least one practical self-help path:
- A specific support article.
- An email with troubleshooting instructions.
- The official online chatbot / self-service path.
- Safe basic guidance the customer can try independently.

---

### Call Structure — What Good Calls Usually Do

| Area | Good practice | Dimensions affected |
|------|--------------|-------------------|
| **Call opening** | Restate the issue clearly; set expectations for the troubleshooting path | COMMUNICATION, EFFICIENCY |
| **Problem understanding** | Identify topology (modem / router / parent node / child node / extender); confirm symptom, trigger event, and what has already been tried | PROTOCOL, ACCURACY, EFFICIENCY |
| **Troubleshooting flow** | Logical path; validate one step before the next; confirm outcome after each significant step | EFFICIENCY, ACCURACY, RESOLUTION |
| **Credential & environment** | Clarify early: Wi-Fi password, admin/router password, app login vs router login, physical access | PROTOCOL, ACCURACY, EFFICIENCY |
| **Customer handling** | Acknowledge frustration; slow down when confused; one action at a time; calm and confident | COMMUNICATION |
| **Resolution / escalation** | Explain the outcome clearly; explain why escalation is needed; set expectation for next step and timeframe | RESOLUTION, PROTOCOL, COMMUNICATION |

**Generic troubleshooting sequence (for reference — not every call needs all steps):**
1. Identify topology and symptom.
2. Confirm modem / WAN / upstream state when relevant.
3. Confirm primary device state.
4. Isolate child / secondary device / client behavior when relevant.
5. Use one primary remediation path.
6. Validate result.
7. Escalate or close clearly.

---

### Accent & ASR Normalization

Our support team is primarily Filipino agents from Mindanao speaking with Visayan/Cebuano accents. The automated transcription (ASR) system may mishear specific terms or accent patterns. The governing principle is:

> **Grade whether the customer's comprehension was adequate for the call to proceed — not whether the transcript matches Standard American English phonemes.**

**Do not penalize for these accent-characteristic patterns:**

| Pattern | Examples | Note |
|---------|---------|------|
| TH→D/T | `de`, `dat`, `dis`, `dere` for `the`, `that`, `this`, `there` | Cosmetic in most grading contexts |
| P/F switching | `prom`, `pirst`, `pollow` for `from`, `first`, `follow` | Context usually recovers |
| B/V switching | `berify`, `bery` for `verify`, `very` | Low–medium impact |
| Number homophones | `fifty` may mean `fifteen` when discussing Linksys fees | Use context (Linksys paid support is $15 not $50) |
| Pronoun gender mixing | `he/she` mixing | First-language transfer — no grading impact |

Accent is only a COMMUNICATION coaching signal if the customer asks for the same instruction to be repeated **≥2 times** on the same step AND context suggests accent (not instruction complexity) was the cause.

---

### Payment / PCI / Recording

- Flag calls for human/compliance review when payment data or redaction markers appear.
- Do not penalize solely because payment-card data appears in the transcript or a redaction marker exists.
- Penalize PROTOCOL and/or COMMUNICATION when the agent fails to clearly explain payment terms, fees, or paid-support expectations.
- Reserve severe penalties for mishandled payment process behavior (e.g., agent reads back card number, CVV, or expiration date; makes the payment flow coercive or confusing).

---

## Overall Score Calibration Summary

| Situation | Expected range |
|-----------|--------------|
| Clean resolution, good process | 4–5 |
| Resolved with minor misses | 3–4 |
| Unresolved but good process, concrete next steps | 3–4 |
| Unresolved, meaningful troubleshooting but flawed | 2–3 |
| Weak support, incomplete, poorly structured | 2–3 |
| Operational breakdown, wrong guidance, severe failure | 1–2 |

**Hard rules:**
- Calls with compliance/payment concerns should not receive a high overall score without human review.
- Calls with repeated accuracy errors should not receive a high ACCURACY score even if communication was polite.
- Calls missing model/serial/warranty (when relevant) should not receive a high PROTOCOL score.
- Calls with chaotic flow or repeated loops should not receive a high EFFICIENCY score.
- Calls with poor call control should not receive a high COMMUNICATION score even if the tone was polite.

---

## How to Update This Rubric

### What You Can Change

The QA team owns the business rubric. You can update:

- The **behavioral expectations** for any dimension (what agents should do, what to penalize).
- The **calibration guidance** (when to use `1` vs `2` vs `3`, what counts as a serious vs. minor miss).
- The **cross-cutting themes** (paid support guidance, call structure, protocol expectations).
- The **5-press procedure** exception list (if Linksys releases new hardware with different pairing methods, update the model list here).
- **Accent patterns** (if new accent-characteristic patterns are identified, add them to the "do not penalize" list).

### What You Should NOT Change Without Engineering Involvement

- The **names of the five dimensions** (`RESOLUTION`, `PROTOCOL`, `EFFICIENCY`, `ACCURACY`, `COMMUNICATION`). The database and dashboards key off these exact strings.
- The **1–5 scale**. The warehouse stores scores as decimals; changing the scale would break historical comparisons.
- The **JSON output schema** in the grading scripts. That is the machine-readable output format, separate from this rubric.

### How to Submit a Rubric Change

1. Edit the file `config/qa_grading_guidance.md` in the call_audio repository.
2. The file is plain Markdown — headings, bullet points, and tables are all supported.
3. Commit the change to the `master` branch (or submit via pull request if your team uses that workflow).
4. The change takes effect on the **next grading run**. Already-graded calls are not automatically re-graded; a manual backfill run is required to re-score historical calls under the new rubric.

### Adding a New Scoring Theme (without a new dimension)

If you want the system to consider a new behavior — for example, "agent must confirm customer is not using a VPN before troubleshooting" — add it as a subsection under the most relevant dimension(s). Use the existing format:

```
### My New Theme Name

Good calls usually:
- [describe the expected behavior]

Penalize when:
- [describe the failure mode]

This should mostly affect:
- PROTOCOL
- EFFICIENCY
```

Do not create a new top-level dimension. Instead, route the new theme into the existing five via the "This should mostly affect" guidance.

### Adding a New Scoring Dimension (structural change)

Adding a sixth dimension (e.g., `EMPATHY` or `COMPLIANCE`) requires changes to:
1. `config/qa_grading_guidance.md` — add the dimension definition and calibration.
2. `scripts/grade_call.py` — add the dimension name to the expected output schema.
3. `db/migrations/` — a new migration to add the column to the warehouse.
4. Metabase dashboards — update the QA dashboard to display the new score column.

This is a multi-step engineering task. Coordinate with the engineering team before adding dimensions.

---

*This document reflects the rubric as of 2026-06-29. The authoritative source is `config/qa_grading_guidance.md` in the call_audio repository.*
