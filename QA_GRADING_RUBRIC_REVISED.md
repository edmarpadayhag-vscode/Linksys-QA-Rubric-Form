# Linksys Technical Support — QA Grading Rubric (Revised)

**Audience:** Operations, Quality Assurance, Training, Engineering
**Purpose:** This document defines how support interactions are scored, **realigned to the current QA Scoring Form Template** (the "Scoring Sheet"). It supersedes the previous five-dimension rubric for *quality-program* purposes.

> **Status:** Revised copy, synchronized to the QA Scoring Form Template as of **2026-06-29** (7 weighted categories · 0–5 scale · 19 behavioral indicators). The original five-dimension `QA_GRADING_RUBRIC.md` is **retained unchanged** because it still drives the automated grading pipeline (`config/qa_grading_guidance.md`, the warehouse, and the dashboards). **Do not point the automated pipeline at this file without completing the engineering reconciliation described in *Discrepancies & Migration Notes*.**

---

## How the Scoring System Works

The quality program is a **resolution-focused coaching system**, not a compliance checklist. Each interaction is evaluated across **seven weighted categories**. Every category receives a score from **0 to 5**, and a **weighted total percentage** is derived from the category scores and weights.

Every evaluation answers three questions:

1. Did we help the customer as effectively as we reasonably could?
2. Did the agent demonstrate strong technical and communication behavior?
3. What does this interaction tell us about training, process, tooling, knowledge, or operational gaps?

Within each category, the evaluator rates a small set of **behavioral indicators** as **Met / Partial / Missed / N.A.** Those ratings produce a suggested (auto) category score, which the evaluator may accept or override with a documented reason.

---

## The Seven Scoring Categories

| # | Category | Weight | What It Measures |
|---|----------|--------|------------------|
| 1 | **Resolution / Progress Toward Resolution** | 30% | Did the interaction move the customer meaningfully closer to a solution? |
| 2 | **Technical Accuracy** | 20% | Was troubleshooting logical and the technical guidance correct and evidence-based? |
| 3 | **Communication & Call Control** | 15% | Did the agent guide the interaction clearly and adapt to the customer? |
| 4 | **Customer Ownership** | 15% | Did the agent take responsibility for the outcome and continuity of the case? |
| 5 | **Escalation Judgment** | 10% | Were escalation decisions (including *not* escalating) appropriate and well-executed? |
| 6 | **Customer Experience** | 5% | Was the human quality of the interaction good — empathy, professionalism, low effort? |
| 7 | **Documentation & Notes** | 5% | Is the case record complete enough for the next agent? (Continuity, not compliance.) |

The category structure, names, and weights match the Scoring Sheet exactly.

---

## Scoring Scale (0–5 Anchors)

| Score | Anchor |
|-------|--------|
| **5** | Issue resolved or strongest available outcome achieved. |
| **4** | Significant progress made with clear next steps. |
| **3** | Partial progress made but opportunities missed. |
| **2** | Limited progress despite available troubleshooting paths. |
| **1** | Little or no meaningful progress. |
| **0** | Agent actions delayed, prevented, or negatively impacted resolution. |

**Calibration philosophy (carried over from the original rubric):**
- The normal coaching range is **3–4.5**. Reserve **0 and 1** for genuine breakdowns.
- An **unresolved** interaction can still score **3–4** if the agent followed sound process and left concrete, useful next steps.
- A technically **resolved** interaction can still score poorly if it was reached through wrong guidance or a serious failure.
- Use **0** (new on this scale) only when the agent's actions actively *worsened or delayed* the outcome — contradictory guidance, harm, or a breakdown that set the customer back.

---

## Weighted Scoring Methodology

```
Category weighted % = (category score ÷ 5) × category weight
Weighted Total      = Σ (category weighted %) across all scored categories
```

**Result bands:**

| Weighted Total | Band |
|----------------|------|
| ≥ 85% | Meets / Exceeds |
| 70–84% | Developing |
| < 70% | Needs Improvement |

**N.A. handling:** If every indicator in a category is N.A. (e.g., no escalation occurred), that category is excluded and its weight is **redistributed proportionally** across the remaining categories, so the weighted total still sums to 100%.

**Auto-zero override:** any auto-zero trigger (see *Auto-Zero Gates*) forces the **Weighted Total to 0%**. Individual category scores still display, for coaching.

---

## Per-Indicator Weighting

Each behavioral indicator carries a weight used to compute the category's suggested score:

| Weight | Tier | Meaning |
|--------|------|---------|
| **3** | Primary | Core behavior — drives the category score. |
| **2** | Core | Important supporting behavior. |
| **1** | Supporting | Contributes, but lighter. |

Suggested category score = `5 × (weighted Met) + 2.5 × (weighted Partial)` divided by the total weight of all **scored** (Met/Partial/Missed) indicators, rounded to one decimal. **N.A.** indicators are excluded from the calculation.

---

## Category Detail

Each category lists its **objective**, its **behavioral indicators** (with weight tier), the **strong / weak signals** to score against (the original rubric's "score down when" guidance is preserved here, re-homed to the correct category), and **calibration**.

### 1 · Resolution / Progress Toward Resolution — 30%

**Objective:** Determine whether the interaction moved the customer meaningfully closer to resolution.

**Behavioral indicators:**
1. *(Primary)* Resolved the issue or achieved the best available outcome for the customer's situation (resolution, RMA, valid escalation, limitation explained, or customer education).
2. *(Primary)* Conducted reasonable troubleshooting that meaningfully advanced the customer's path toward resolution before concluding the interaction or relying on self-help / KB resources.
3. *(Core)* Selected a resolution path appropriate to the customer's situation, product status, and available support options — including best-effort troubleshooting for out-of-warranty products rather than using warranty status as a reason to stop helping.

**Score down when:**
- The customer leaves with the same problem and no concrete next step.
- A workaround is given without confirming it worked.
- The call ends before confirming the device, network, or app state.
- A generic KB article is sent in place of investigation, or the outcome is vague, contradictory, or left open.

**Concrete next steps that *help* this score:** a specific KB/support article; a promised email with detailed steps; a defined step for escalation, replacement, follow-up testing, or continued troubleshooting.

**Boundary — "meaningfully advanced":** eliminates possible causes, gathers evidence, narrows the problem scope, or identifies the next valid action — not merely time spent.

---

### 2 · Technical Accuracy — 20%

**Objective:** Evaluate the quality of troubleshooting and technical guidance.

**Behavioral indicators:**
1. *(Primary)* Applied a logical diagnostic process — identified the symptoms, asked relevant diagnostic questions, and determined the root cause (or most likely cause) when possible.
2. *(Core)* Used available tools, resources, and evidence effectively to support troubleshooting and decision-making (draw on the correct source of truth — approved knowledge, official troubleshooting flows, prior case evidence — not memory or guesswork).
3. *(Primary)* Provided technically accurate information, recommendations, and conclusions supported by available evidence.

**Serious accuracy failures (cap this category around 3, lower if dangerous or case-derailing):**
- Wrong router access URL (e.g., `myrouter.local`, `192.168.1.1` when not applicable), wrong default password, or wrong reset procedure.
- Wrong firmware/app/product-capability claim, wrong LED interpretation, or wrong warranty/support-policy statement presented as fact.
- Wrong topology diagnosis that contradicts the transcript or KB; settings changes advised without confirming model/topology when that matters.
- Unsupported remote-session flows, unsupported websites, or unsafe domains.

**5-press pairing calibration (preserved):** The 5-press method is valid on **all Linksys mesh routers** (WHW, MX, MR series) **except** models with a dedicated Pair button (SPNM60, SPNM62, SPNM60TB, LN11xx, LN12xx). EA series routers are standalone; 5-press does not apply. Do **not** flag 5-press on a WHW/MX/MR without a Pair button. Penalize only when (a) the model has a dedicated Pair button, or (b) the agent describes 5-press as a factory reset (it is not).

---

### 3 · Communication & Call Control — 15%

**Objective:** Evaluate how effectively the agent managed the interaction.

**Behavioral indicators:**
1. *(Primary)* Effectively guided the interaction — set clear expectations, maintained call control and troubleshooting flow, and managed time and transitions, including through difficult moments.
2. *(Primary)* Communicated appropriately to the customer's knowledge level, communication style, and accessibility needs (hearing, vision, language, age, cognitive), maintaining mutual understanding throughout.

**Score down when (absorbs the original EFFICIENCY + COMMUNICATION concerns):**
- Confusing or contradictory instructions; multiple actions at once for an already-confused customer.
- Long unexplained silence/hold; repeated questions the customer already answered; chaotic flow because the agent never took control.
- Talking over the customer; excessive filler/rambling; failure to acknowledge frustration; ending with no clear recap or next step.
- Registration/payment/admin steps that needlessly delay basic troubleshooting; repeated resets or path-switching without learning anything new.

**Calibration:** Do not over-penalize plain tone — efficient, correct, useful support can still score well even when warmth is minimal. See *Accent & ASR Normalization* before flagging comprehension issues.

---

### 4 · Customer Ownership — 15%

**Objective:** Measure the degree to which the agent accepted responsibility for moving the customer forward and for continuity of the case.

**Behavioral indicators:**
1. *(Primary)* Demonstrated ownership of the customer's outcome — took appropriate responsibility, avoided unnecessary transfers, and followed through on commitments.
2. *(Core)* Established clear next steps and realistic timelines, and completed required follow-up actions — including disconnect and callback commitments within the agreed window.
3. *(Core)* Maintained case continuity — used prior contact history and provided sufficient context during handoffs, escalations, or follow-ups so the customer did not have to repeat themselves. *Mark N.A. if confirmed first contact with no handoff.*

**Score down when:** deflecting to other teams without attempting to help; transferring to avoid difficulty; promising a callback/email and not delivering (with nothing documented); treating a repeat contact as new; missed/late callbacks without proactive renegotiation.

---

### 5 · Escalation Judgment — 10%

**Objective:** Determine whether escalation decisions — including the decision *not* to escalate, and upward escalations the customer requested (management, complaint, legal) — were appropriate.

**Behavioral indicators:**
1. *(Primary)* Made an appropriate escalation decision (including the decision not to escalate) based on troubleshooting performed and recognized escalation criteria — including a customer complaint, management request, or legal-risk trigger. *Mark N.A. if no escalation was involved and none was warranted.*
2. *(Core)* Executed the escalation effectively — used the correct path, provided complete details and context, and explained the reason and next steps to the customer. *Mark N.A. if no escalation occurred.*

**Score down when:** escalating after one step or because the customer is frustrated rather than because L1 options were exhausted; escalating an OOW product before any investigation; **failing** to escalate a complaint with a legal-risk reference or an explicit management request; incomplete escalation notes or the wrong queue.

**Boundary — "enough troubleshooting before escalation":** the standard L1 steps for the issue type completed and documented (a judgment about work done, not a timer).

---

### 6 · Customer Experience — 5%

**Objective:** Measure the human quality of the interaction.

**Behavioral indicators:**
1. *(Primary)* Demonstrated empathy, professionalism, and patience throughout — including for repeat-contact fatigue and under pressure.
2. *(Core)* Adapted to the customer's tone, pace, and emotional state and maintained positive engagement and understanding.
3. *(Core)* Reduced customer effort — avoided unnecessary repetition, complexity, delays, or obstacles.

**Score down when:** dismissive/robotic responses; frustration escalated by agent behavior; marathon sessions pushed onto vulnerable customers without offering to pause; unnecessary or unexplained holds.

**Boundary — effort vs. necessary work:** necessary troubleshooting and required verification are **not** "customer effort" to be minimized — effort-reduction removes avoidable friction, it never means skipping needed diagnostic steps.

---

### 7 · Documentation & Notes — 5%

**Objective:** Ensure the next agent can quickly understand the case. Purpose is continuity, not compliance.

**Behavioral indicators:**
1. *(Primary)* Documented the customer issue, troubleshooting performed, and key findings sufficiently to understand the case history.
2. *(Core)* Captured the reasoning behind key decisions, recommendations, escalations, and actions — including colleague / SME input when no private note applies.
3. *(Core)* Recorded clear next steps, follow-up requirements, and an accurate current case status.

**Score down when:** generic or missing issue summary; "performed troubleshooting" with no findings; a case marked **RESOLVED** with no confirming note; missing next steps or a status that misrepresents the case (premature closure).

> **Data-source caveat:** Documentation & Notes lives in the case record (HappyFox), **not** the call audio. An audio-only automated grader cannot assess this category reliably — see *Discrepancies & Migration Notes*.

---

## Auto-Zero Gates

Any **compliance gate marked "No"**, or any **A–K item marked "Yes"**, forces the **Weighted Total to 0%** (category scores still display, for coaching).

**Compliance gates (must be adhered):** Adherence to Callback Hours · Adherence to PCI & Information Security Standards · Sales.

**A–K critical list (any occurrence):** A. Call / Session Abandonment · B. Call / Session Avoidance / Evasion · C. Discourtesy · D. Escalation (abuse) · E. Failure to ask for the email address · F. Fraud · G. Hard-selling · H. Line Release · I. Non-Adherence to Callback Hours · J. Non-Adherence to PCI and Information Security Standards · K. Non-First Call Resolution.

---

## Coaching Flags

Each flag auto-fires when its linked indicator is rated **Partial or Missed**, and each requires a coaching action:

| Flag | Linked indicator |
|------|------------------|
| Technical accuracy failure | Technical Accuracy #3 |
| Missed follow-up / callback commitment | Ownership #2 |
| Commitments not honored / ownership gap | Ownership #1 |
| Customer left without meaningful progress or a path forward | Resolution #2 |
| Escalation decision inappropriate (premature, or warranted escalation not made) | Escalation #1 |
| Escalation poorly executed (path, handoff detail, customer not informed) | Escalation #2 |
| Professionalism concern | Customer Experience #1 |
| Ticket status inaccurate / premature closure | Documentation #3 |

> Survey / CSAT manipulation has no behavioral indicator and cannot be auto-detected — flag it manually in coaching if suspected.

---

## Resolution Outcome Classification

Independent of the weighted score, classify the interaction's outcome:

- **Successful Resolution** — issue resolved/confirmed, or strongest available outcome executed.
- **Partial Resolution** — real progress, but the core issue is open or unconfirmed at close.
- **Appropriate Escalation** — correctly escalated with complete handoff after reasonable L1 work.
- **Ownership Gap** — the failure was ownership/continuity (missed callback, premature closure, abandoned next step), not technical.
- **Unresolved** — no meaningful progress and no actionable path forward.

A closed case is **not** automatically a resolved case.

---

## Disconnected-Call Policy

If a call disconnects, evaluate whether reasonable follow-up occurred. Acceptable follow-up: a callback attempt, a follow-up email, a private note documenting the disconnect, or an explanation of why follow-up was not possible. A disconnect with **no** documented follow-up is a **missed ownership opportunity** (flag in Customer Ownership).

---

## Critical-Failure Conditions

The following trigger review/coaching regardless of the weighted score: harmful or incorrect troubleshooting; misrepresenting product capabilities; unsupported root-cause claims; no follow-up after a disconnected call; failure to complete a promised action; abandoning the customer without a path forward; escalating without reasonable troubleshooting, or using escalation to avoid ownership; unprofessional, rude, or dismissive conduct; policy violations. Always check for these even when the weighted score is otherwise strong.

---

## Multi-Touch / Team Scoring

When several agents touch one case, evaluate the whole customer journey, not just one interaction: handoff quality, documentation continuity, escalation quality, follow-up effectiveness, and shared ownership. The Scoring Sheet's Team Scoring / Case Tracker provides **Journey Outcome** and **Continuity of Support** anchors (0–5) for this. Identify where the support chain succeeded or failed.

---

## Cross-Cutting Guidance (preserved from the original rubric)

### Paid Support & Warranty
Paid support can be appropriate but must not replace basic triage or create avoidable frustration. **Penalize** (Resolution / Escalation, and Auto-Zero *Hard-selling* in severe cases) when the agent pushes paid support before understanding the issue, repeats the offer after refusal without adding value, blocks safe basic guidance behind payment, or explains warranty/eligibility incorrectly. **Do not penalize** simply because the device is out of warranty or the call does not convert. For OOW calls where the customer declines paid support, handling is still good if the agent provides at least one practical self-help path (a specific article, an email with steps, the official chatbot/self-service path, or safe basic guidance). *(This is exactly Resolution indicator #3.)*

### Call Structure — What Good Calls Usually Do
| Area | Good practice | Categories affected |
|------|--------------|---------------------|
| Call opening | Restate the issue; set expectations for the path | Communication, Resolution |
| Problem understanding | Identify topology (modem/router/parent/child/extender); confirm symptom, trigger, what was tried | Technical, Communication |
| Troubleshooting flow | Logical path; validate one step before the next; confirm outcome | Technical, Resolution |
| Credential & environment | Clarify early: Wi-Fi vs admin password, app vs router login, physical access | Technical, Communication |
| Customer handling | Acknowledge frustration; slow down when confused; one action at a time | Customer Experience, Communication |
| Resolution / escalation | Explain the outcome; explain why escalation is needed; set next step and timeframe | Resolution, Escalation, Ownership |

**Generic troubleshooting sequence (reference — not every call needs all steps):** 1) identify topology & symptom; 2) confirm modem/WAN/upstream when relevant; 3) confirm primary device state; 4) isolate child/secondary/client behavior; 5) one primary remediation path; 6) validate result; 7) escalate or close clearly.

### Accent & ASR Normalization
Our team is primarily Filipino agents from Mindanao with Visayan/Cebuano accents; the ASR may mishear specific terms. **Grade whether the customer's comprehension was adequate for the call to proceed — not whether the transcript matches Standard American English phonemes.**

| Pattern | Examples | Note |
|---------|----------|------|
| TH→D/T | `de`, `dat`, `dis` for `the`, `that`, `this` | Cosmetic |
| P/F switching | `prom`, `pirst`, `pollow` | Context recovers |
| B/V switching | `berify`, `bery` | Low–medium impact |
| Number homophones | `fifty` may mean `fifteen` | Linksys paid support is $15, not $50 |
| Pronoun gender mixing | `he/she` mixing | First-language transfer — no impact |

Accent is only a **Communication** coaching signal if the customer asks for the same instruction to be repeated **≥2 times** on the same step **and** context suggests accent (not instruction complexity) caused it.

### Payment / PCI / Recording
Flag for human/compliance review when payment data or redaction markers appear. **Do not** penalize solely because card data or a redaction marker is present. **Penalize** Documentation/Communication when payment terms, fees, or paid-support expectations are unclear. Severe mishandling (reading back card number, CVV, or expiry; a coercive/confusing payment flow) is a **PCI auto-zero** condition.

---

## Discrepancies & Migration Notes

This is where the previous five-dimension rubric and the Scoring Sheet **cannot be mapped 1:1**. Each item below is a deliberate decision point, not an oversight.

### Old dimension → new category mapping

| Original dimension (1–5) | Maps to (Scoring Sheet) | Notes |
|--------------------------|-------------------------|-------|
| **RESOLUTION** | Resolution / Progress (cat 1) | Near-direct. |
| **ACCURACY** | Technical Accuracy (cat 2) | Near-direct. |
| **COMMUNICATION** | Communication & Call Control (cat 3) **+** Customer Experience (cat 6) | The *empathy/professionalism/effort* half of the old dimension is now its own category (CX). |
| **EFFICIENCY** | Distributed: Communication (call control, time/transitions) **+** Customer Experience (reduced effort) **+** Resolution (troubleshooting that advances) | **No standalone home.** Efficiency is no longer a scored dimension. |
| **PROTOCOL** | Distributed: Escalation Judgment (pathing) **+** Documentation (case management) **+** Customer Ownership (follow-through) **+** Auto-Zero (PCI, callback hours, sales) | **No standalone home.** Administrative/process behavior is split across categories and gates. |
| *(none)* | **Customer Ownership, Escalation Judgment, Documentation & Notes** | New categories with **no equivalent** in the old rubric — must be assessed afresh. |

### Structural discrepancies & recommendations

1. **Scale 1–5 → 0–5.** The Scoring Sheet adds **0** (agent worsened/delayed the outcome). The warehouse stores 1–5 decimals, so adopting 0 is a **breaking change for historical comparisons**.
   *Recommendation:* keep the automated pipeline on 1–5 for now; apply 0 only in the human form, **or** run an engineering migration that documents a 1→0 bridge before backfilling.

2. **5 dimensions → 7 weighted categories, renamed.** Dimension names are keyed by the DB, dashboards, and JSON schema; renaming breaks them.
   *Recommendation:* do not rename in `config/qa_grading_guidance.md` unilaterally. Either (a) keep the automated grader on the 5 dimensions and **map** its output into this 7-category report at the presentation layer, or (b) coordinate a full schema/dashboard migration with engineering.

3. **Weighting (30/20/15/15/10/5/5).** The automated pipeline currently derives an overall score without category weights.
   *Recommendation:* add the weighted-total computation to the aggregation step; until then, treat the weighted total here as a **human-QA** figure.

4. **Indicator-level Met/Partial/Missed/N.A. + auto-score.** The grader scores at the dimension level; the Scoring Sheet rates 19 indicators that roll up to category scores.
   *Recommendation:* optionally have the AI rate the 19 indicators and reproduce the form's auto-score formula — this also enables the coaching flags below.

5. **Auto-Zero gates & Coaching Flags.** New mechanics with no pipeline equivalent.
   *Recommendation:* implement auto-zero as a post-scoring override and derive coaching flags from indicator ratings; until built, apply both as a **human-review overlay**.

6. **Documentation & Notes (cat 7) is not gradeable from audio.** Case notes live in HappyFox, not the call recording.
   *Recommendation:* feed the case record into the grader, **or** mark Documentation **N.A.** in the automated path and score it only in human review. (Escalation Judgment is partially affected too — whether/where an escalation was filed often lives in the CRM, not the transcript.)

7. **Multi-touch / Team Scoring, Resolution-Outcome classes, Disconnect policy.** These are journey-level / case-level constructs beyond a single-call audio grade.
   *Recommendation:* keep them in the human QA workflow (Case Tracker / Team Scoring) and out of the per-call automated score unless case data is joined in.

8. **Preserved-but-re-homed PROTOCOL content.** Model/serial/warranty confirmation now sits under Technical Accuracy and Resolution; case-management discipline under Documentation; escalation pathing under Escalation Judgment; PCI/callback/sales under Auto-Zero. No expectation was dropped — only relocated. The original calibration that *missing one administrative field is usually a 2–3, not an automatic failure* is preserved in the relevant categories.

---

## How to Update This Rubric

**The QA team owns the business rubric.** You can freely update behavioral expectations, calibration guidance, cross-cutting themes, the 5-press exception list, and the accent patterns.

**Do not change without engineering involvement** (these break the automated pipeline that still runs on the original five-dimension file):
- The **five automated dimension names** in `config/qa_grading_guidance.md` (DB/dashboards/JSON key off them). Adopting the seven categories here is a **coordinated migration**, not a text edit.
- The **stored 1–5 scale** in the warehouse.
- The **JSON output schema** in the grading scripts.

**To adopt this revised rubric in production**, treat it as an engineering project: align the JSON schema and warehouse columns to the seven categories and 0–5 scale, add weighting + auto-zero + coaching-flag logic, decide how Documentation/Escalation source their data, then update the dashboards. Until that work is done, **use this document for human QA and coaching**, and keep the original `QA_GRADING_RUBRIC.md` as the live automated-pipeline spec.

---

*Revised 2026-06-29 to synchronize with the QA Scoring Form Template (7 weighted categories · 0–5 scale · 19 behavioral indicators · auto-zero · coaching flags). The original five-dimension rubric remains the authoritative spec for the automated grading pipeline until the migration above is completed.*
