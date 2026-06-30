# Linksys Technical Support — QA Grading Rubric (Revised)

**Audience:** Operations, Quality Assurance, Training
**Purpose:** This document explains how agent interactions are scored, **aligned to the QA Scoring Form Template** (the "Scoring Sheet"). It keeps the readable structure of the original rubric but replaces the five legacy dimensions with the **seven categories** of the Scoring Sheet, and it is written so an **AI evaluator** can rate each behavioral indicator consistently from the case evidence.

---

## How the Scoring System Works

Each interaction is evaluated across **seven weighted categories**. Every category receives a score from **0 to 5**, and an overall **weighted percentage** is derived from the category scores and weights.

Within each category, the evaluator rates a small set of **behavioral indicators** as **Met / Partially Met / Not Met / Not Applicable**, based solely on the evidence in the case. Those indicator ratings produce the category's 0–5 score; the category scores produce the overall result.

Every evaluation answers three questions: *Did we help the customer as effectively as we reasonably could? Did the agent demonstrate strong technical and communication behavior? What does the interaction reveal about training, process, or tooling gaps?*

> **Rating labels:** `Met`, `Partially Met`, `Not Met`, `Not Applicable` — these correspond exactly to the Scoring Sheet's dropdown values **Met / Partial / Missed / N.A.**

---

## The Seven Scoring Categories

| # | Category | Weight | What It Measures |
|---|----------|--------|------------------|
| 1 | **Resolution / Progress Toward Resolution** | 30% | Did the interaction move the customer meaningfully closer to a solution? |
| 2 | **Technical Accuracy** | 20% | Was troubleshooting logical and the technical guidance correct and evidence-based? |
| 3 | **Communication & Call Control** | 15% | Did the agent guide the interaction clearly and adapt to the customer? |
| 4 | **Customer Ownership** | 15% | Did the agent take responsibility for the outcome and continuity of the case? |
| 5 | **Escalation Judgment** | 10% | Were escalation decisions — including *not* escalating — appropriate and well-executed? |
| 6 | **Customer Experience** | 5% | Was the human quality of the interaction good — empathy, professionalism, low effort? |
| 7 | **Documentation & Notes** | 5% | Is the case record complete enough for the next agent? (Continuity, not compliance.) |

---

## Scoring Scale (0–5)

| Score | Label | What It Means |
|-------|-------|---------------|
| **5** | Excellent | Issue resolved or the strongest available outcome achieved. |
| **4** | Strong | Significant progress made with clear next steps. |
| **3** | Acceptable | Partial progress made but opportunities missed. |
| **2** | Weak | Limited progress despite available troubleshooting paths. |
| **1** | Poor | Little or no meaningful progress. |
| **0** | Breakdown | Agent actions delayed, prevented, or negatively impacted resolution. |

**Calibration note:** The normal coaching range is **3 to 4.5**. Reserve **0 and 1** for genuine breakdowns. An **unresolved** interaction can still score **3–4** when the agent followed sound process and left concrete next steps; a technically **resolved** one can still score low if reached through wrong guidance or a serious failure.

---

## How Indicator Ratings Become Scores

Each behavioral indicator carries a weight — **Primary (3)**, **Core (2)**, or **Supporting (1)** — reflecting how much it drives the category.

- **Met** counts as full credit (5), **Partially Met** as half (2.5), **Not Met** as zero.
- **Not Applicable** indicators are excluded, and their weight is redistributed across the rest.
- The **category score (0–5)** is the weighted blend of its indicators' credit.
- The **overall score** is the weighted sum of category scores (Resolution 30% … Documentation 5%), expressed as a percentage.

**Result bands:** ≥ 85% = *Meets / Exceeds* · 70–84% = *Developing* · < 70% = *Needs Improvement*.

**Auto-zero:** any auto-zero trigger (see *Auto-Zero & Critical Failures*) forces the overall score to **0%**; category scores still display, for coaching.

**Evidence discipline for the AI:** rate only from what the case shows; cite a short quote or observation for each rating; judge decisions on the information available at the time (no hindsight); and when the source needed to judge an indicator was **not provided** (e.g., ticket notes for Documentation), mark it **Not Applicable — insufficient evidence** rather than Not Met.

---

## Category Detail

Each category below states its **purpose**, its **behavioral indicators** (with weight tier), the **AI evaluation criteria** for each indicator (Met / Partially Met / Not Met / Not Applicable), and **what to watch** during scoring.

---

### 1 · Resolution / Progress Toward Resolution — 30%

*Did the interaction move the customer meaningfully closer to resolution?*

**R1. Resolved the issue or achieved the best available outcome** (resolution, RMA, valid escalation, limitation explained, or customer education). *(Primary)*
- **Met:** Issue fully resolved and confirmed with the customer, or the strongest available outcome was properly executed — RMA correctly initiated, valid escalation submitted with complete documentation, product limitation accurately explained, or appropriate customer education provided.
- **Partially Met:** An outcome was pursued but not fully executed or confirmed — RMA initiated but missing a field, escalation submitted with sparse notes, or the issue appeared resolved but the customer never confirmed.
- **Not Met:** Case closed with no meaningful outcome — generic KB link sent without investigation, escalation used with no prior troubleshooting, or an out-of-warranty product dismissed with no attempt to help.
- **Not Applicable:** Use only when the outcome is not observable in the provided materials (insufficient evidence). Every interaction should produce some outcome.

**R2. Conducted reasonable troubleshooting that meaningfully advanced the customer's path** before concluding or relying on self-help / KB resources. *(Primary)*
- **Met:** Agent worked through relevant, logically sequenced diagnostic steps appropriate to the product and symptom, and investigated before any KB article or self-help link was offered. Self-help, if used, complemented the investigation rather than replacing it.
- **Partially Met:** Some troubleshooting was done but key steps were skipped, or a KB article was leaned on before the investigation was complete.
- **Not Met:** No meaningful troubleshooting — agent jumped to a conclusion, blamed the ISP without evidence, escalated after a single step, or sent a generic KB article as the primary response.
- **Not Applicable:** Only when troubleshooting evidence is not available to assess (insufficient evidence).
- *"Meaningfully advanced" means the interaction eliminated a possible cause, gathered evidence, narrowed the problem scope, or identified the next valid action — not merely that time was spent.*

**R3. Selected an appropriate resolution path** for the customer's situation, product status, and support options — including best-effort out-of-warranty troubleshooting rather than using warranty as a reason to stop helping. *(Core)*
- **Met:** Agent determined warranty/product status correctly and matched the path to the situation: in-warranty hardware fault → RMA; software/config → troubleshooting; known limitation → education; out-of-warranty → best-effort troubleshooting with limitations explained rather than dismissal.
- **Partially Met:** Path mostly right but one element misaligned — offered paid support while in warranty, or gave an out-of-warranty customer only a partial best-effort attempt before redirecting.
- **Not Met:** Wrong path — RMA for a clearly out-of-warranty product without an exception, an in-warranty hardware fault closed without replacement, an out-of-warranty customer dismissed with "out of warranty, can't help" and no troubleshooting, or paid connect/support offered in place of best-effort help.
- **Not Applicable:** Only when warranty/product status was genuinely undeterminable despite a reasonable lookup, and that was documented.

**What to watch:** Concrete next steps *raise* this category — a specific KB article, a promised email with steps, or a defined step for escalation/replacement/follow-up testing. Do not over-penalize an unresolved case that still followed sound process and left the customer a clear path.

---

### 2 · Technical Accuracy — 20%

*Was the agent's troubleshooting logical and the technical guidance correct?*

**T1. Applied a logical diagnostic process** — identified the symptoms, asked relevant diagnostic questions, and determined the root cause (or most likely cause) when possible. *(Primary)*
- **Met:** Identified the specific symptom (not just "internet issue"), asked targeted diagnostic questions, worked through troubleshooting in a logical sequence, and identified the root cause or an evidence-backed likely cause.
- **Partially Met:** Symptoms partly identified or the sequence was disorganized; or a possible cause was named without narrowing it down or supporting it with evidence.
- **Not Met:** Troubleshot generically without understanding the symptom, asked few relevant questions, worked in no logical order, or stated an unsupported cause (ISP/customer blame) with no diagnostic to justify it.
- **Not Applicable:** Customer immediately requested escalation and declined any diagnostic interaction.

**T2. Used available tools, resources, and evidence effectively** to support troubleshooting and decision-making. *(Core)*
- **Met:** Used relevant tools at the right point — remote session, admin dashboard, modem/WAN test, logs, prior case data, approved KB — and interpreted the results correctly. Drew on the correct source of truth rather than memory or guesswork.
- **Partially Met:** Used some tools but missed relevant ones, used one at the wrong moment, or could not fully interpret the results.
- **Not Met:** Did not use available tools the situation required, or relied on the customer's verbal description for something a tool could have confirmed directly.
- **Not Applicable:** No tools were available or applicable — an offline issue prevented access, or the customer declined remote assistance.

**T3. Provided technically accurate information, recommendations, and conclusions supported by evidence.** *(Primary)*
- **Met:** All technical guidance, specs, and instructions were factually correct and consistent with documentation, and conclusions were validated before being presented.
- **Partially Met:** Mostly accurate with one or two minor inaccuracies unlikely to cause serious harm — slightly wrong reset duration or LED description — reflecting a knowledge gap.
- **Not Met:** Materially incorrect information — wrong default password, non-existent LED state, unsupported method — or a conclusion stated without evidence (ISP/customer blame). One clearly wrong, dangerous, or case-derailing instruction lands here.
- **Not Applicable:** Only when no technical guidance is observable to assess (insufficient evidence); accuracy is otherwise always required.

**What to watch — serious accuracy failures:** wrong router-access URL for the model, wrong default password/login, wrong reset procedure, wrong firmware/app/capability claim, wrong LED interpretation, a warranty/policy statement presented incorrectly as fact, a topology diagnosis that contradicts the transcript/KB, or unsafe domains / unsupported remote-session flows.

**5-press pairing calibration:** The 5-press method is valid on **all WHW, MX, and MR mesh routers**, and invalid on models with a dedicated Pair button (**SPNM60, SPNM62, SPNM60TB, LN11xx, LN12xx** — use the Pair button). EA-series routers are standalone; 5-press does not apply. Penalize **only** when (a) the model has a dedicated Pair button, or (b) the agent calls 5-press a factory reset. Do **not** flag 5-press on any WHW/MX/MR without a Pair button.

---

### 3 · Communication & Call Control — 15%

*Did the agent guide the interaction clearly and keep the customer with them?*

**C1. Effectively guided the interaction** — set clear expectations, maintained call control and troubleshooting flow, and managed time and transitions, including through difficult moments. *(Primary)*
- **Met:** Framed the interaction at the start (what, roughly how long, expected outcome), kept it on track, paced it well, narrated clear transitions between steps, and stayed in control through difficult or tense moments.
- **Partially Met:** Generally guided the interaction but lost direction at one or two points, set expectations weakly, or had abrupt transitions / unannounced holds that briefly disoriented the customer.
- **Not Met:** No framing and reactive throughout — the customer dominated or drifted, long unexplained silences, or the agent lost control when the customer became difficult.
- **Not Applicable:** Only when not observable (insufficient evidence); the interaction can always be guided.

**C2. Communicated appropriately to the customer's level, style, and accessibility needs** (hearing, vision, language, age, cognitive), maintaining mutual understanding. *(Primary)*
- **Met:** Actively listened, adapted terminology to the customer's level, confirmed understanding at key steps, and made deliberate accommodations for any accessibility need (slower pace, simpler language, one step at a time, written follow-up).
- **Partially Met:** Adapted mostly well but used unexplained jargon at points, did not consistently confirm understanding, accommodated one aspect of a need while overlooking another, or rushed instructions faster than the customer could follow.
- **Not Met:** Talked past the customer — technical language with no adaptation, little evidence of listening, no comprehension checks — or ignored a clear accessibility need.
- **Not Applicable:** Only when not observable (insufficient evidence).

**What to watch:** Score down for confusing or contradictory instructions, talking over the customer, multiple actions at once for a confused customer, long unexplained silences or holds, repeated questions already answered, chaotic flow the agent never takes control of, or ending with no clear recap. Do not over-penalize plain tone if the support was clear and useful. Apply the **Accent & ASR** rule below before flagging comprehension issues.

---

### 4 · Customer Ownership — 15%

*Did the agent take responsibility for the outcome and the continuity of the case?*

**O1. Demonstrated ownership of the customer's outcome** — took appropriate responsibility, avoided unnecessary transfers, and followed through on commitments. *(Primary)*
- **Met:** Owned the case from contact to close, made reasonable efforts personally, transferred only for a clear documented reason after appropriate effort, and honored every commitment (within the interaction or documented with an owner and timeline).
- **Partially Met:** Generally owned the case but transferred where more effort was reasonable, or made a commitment that was only partially honored — fulfilled late or not documented.
- **Not Met:** Transferred immediately or after minimal effort to avoid difficulty, or broke a commitment with nothing documented — the customer was left waiting on something that never happened.
- **Not Applicable:** Only when not observable (insufficient evidence); ownership is always expected.

**O2. Established clear next steps and realistic timelines, and completed required follow-up** — including disconnect and callback commitments within the agreed window. *(Core)*
- **Met:** Told the customer specifically what happens next (who, when, what to do meanwhile) with realistic timelines, and completed any required follow-up: a disconnect callback within the window, or a promised return call on time (or proactively renegotiated before the window lapsed).
- **Partially Met:** Some expectation-setting or follow-up occurred but was incomplete — a timeline without an owner, follow-up attempted but not documented, or a callback slightly outside the window without proactive communication.
- **Not Met:** Customer received no information about what happens next or an unrealistic timeline; or a disconnect/callback commitment was missed entirely with no follow-up made or documented.
- **Not Applicable:** Only when the issue was fully resolved and confirmed with nothing pending and no disconnect or callback commitment.

**O3. Maintained case continuity** — used prior contact history and provided sufficient handoff context so the customer did not have to repeat themselves. *(Core)*
- **Met:** Reviewed and referenced prior contact history, did not re-ask what was already answered or repeat documented steps, and on any handoff or escalation passed symptoms, findings, steps taken, status, and a specific next action so the receiving agent could continue seamlessly.
- **Partially Met:** Some continuity but a gap — re-asked something already in the notes, or a handoff that had context but missing specifics the receiving agent needed.
- **Not Met:** Treated a repeat contact as new — asked the customer to start over or repeated documented steps — or handed off with only "customer still has issue," forcing the customer to repeat their history.
- **Not Applicable:** Only when this is a confirmed first contact with no prior history and no handoff occurred on this touch.

**What to watch:** Automatic concerns include no documented follow-up after a disconnect, unclear next steps, passing responsibility without context, failing to complete a promised action, and missed or late callbacks without proactive renegotiation.

---

### 5 · Escalation Judgment — 10%

*Were escalation decisions — including the decision not to escalate — appropriate and well-executed?*

**E1. Made an appropriate escalation decision** (including the decision not to escalate) based on troubleshooting performed and recognized escalation criteria — including a customer complaint, management request, or legal-risk trigger. *(Primary)*
- **Met:** Escalation (or the decision not to escalate) was driven by a legitimate, recognized trigger after reasonable L1 work — complexity beyond L1, confirmed hardware fault, repeat unresolved issue, a customer complaint or management request, or a legal-risk signal — and routine cases were resolved rather than escalated.
- **Partially Met:** A trigger was present but borderline — the issue may have been resolvable at L1 with more effort, or a valid trigger was acted on but the troubleshooting behind it was thin.
- **Not Met:** Escalated with no valid trigger (to avoid a difficult call or after minimal effort), **or** failed to escalate a warranted case — most critically, an explicit management request or a legal-risk reference left unactioned.
- **Not Applicable:** Only when no escalation was involved on this touch and none was warranted.
- *"Enough troubleshooting before escalation" means the standard L1 steps for the issue type were completed and documented — a judgment about work done, not a timer.*

**E2. Executed the escalation effectively** — used the correct path, provided complete details and context, and explained the reason and next steps to the customer. *(Core)*
- **Met:** The escalation went to the correct team with complete details — symptom, product/warranty status, steps and findings, reason, and what's specifically needed — and the customer was told why, who would handle it, and when to expect contact.
- **Partially Met:** Submitted to the right team but missing some useful detail (no results, history, or contact info), or the customer was told about the escalation without a clear reason or timeline.
- **Not Met:** Critical information missing or wrong team entirely, or the customer was never told they were being escalated (or was told the case was resolved).
- **Not Applicable:** When no escalation occurred on this touch. *(If escalation execution lives only in CRM/notes that were not provided, mark Not Applicable — insufficient evidence.)*

**What to watch:** A low score is for premature, avoidable, or poorly documented escalations, escalation used to avoid ownership, or a warranted escalation (including a customer's management request) that was **not** made.

---

### 6 · Customer Experience — 5%

*Was the human quality of the interaction good?*

**X1. Demonstrated empathy, professionalism, and patience** throughout — including for repeat-contact fatigue and under pressure. *(Primary)*
- **Met:** Acknowledged the customer's frustration or history specifically and sincerely (not a scripted line), explicitly recognized repeated effort on repeat contacts, and stayed composed, courteous, and solution-focused even under pressure.
- **Partially Met:** Empathy was generic or scripted without acknowledging the specific history, or professionalism slipped briefly — a moment of visible impatience or a slightly defensive response.
- **Not Met:** Entirely transactional with no acknowledgment of frustration or repeat history, or became impatient, sarcastic, dismissive, or defensive in a way that damaged the interaction.
- **Not Applicable:** Only when not observable (insufficient evidence); professionalism is always required.

**X2. Adapted to the customer's tone, pace, and emotional state** and maintained engagement and understanding. *(Core)*
- **Met:** Naturally matched the customer's communication style — technical with a knowledgeable customer, warm and patient with an anxious one, efficient with someone who wanted speed — and kept the customer an informed, engaged participant, checking comprehension at key moments.
- **Partially Met:** Mostly matched the customer but one dimension was off (too formal, too technical, too slow), or the customer had moments of confusion or disengagement that were only partly addressed.
- **Not Met:** One-size-fits-all tone regardless of the customer's cues; the customer was confused or disengaged at multiple points and the agent did not adjust or respond.
- **Not Applicable:** Only when not observable (insufficient evidence).

**X3. Reduced customer effort** — avoided unnecessary repetition, complexity, delays, or obstacles. *(Core)*
- **Met:** Proactively reduced what the customer had to do — used information already on file, handled actions agent-side where possible, and avoided unnecessary repetition, holds, or steps.
- **Partially Met:** Some effort to reduce friction, but the customer was asked to repeat known information or perform steps that could have been handled more efficiently.
- **Not Met:** Customer had to repeat information multiple times, was sent through unnecessary steps, or hit avoidable friction (including unnecessary or unexplained holds) because available information was not used.
- **Not Applicable:** Only when not observable (insufficient evidence).
- *Necessary troubleshooting and required verification are not "customer effort" to be minimized — effort-reduction removes avoidable friction, never needed diagnostic steps.*

**What to watch:** Negative signals include dismissive or robotic responses, frustration escalated by agent behavior, and marathon sessions pushed onto vulnerable customers without offering to pause and resume.

---

### 7 · Documentation & Notes — 5%

*Is the case record complete enough for the next agent? Purpose is continuity, not compliance.*

> **Source dependency:** this category is judged from the **case record (ticket notes/status)**, not the call audio. If notes are not provided to the evaluator, rate D1–D3 **Not Applicable — insufficient evidence**.

**D1. Documented the customer issue, troubleshooting performed, and key findings** sufficiently to understand the case history. *(Primary)*
- **Met:** Notes clearly describe what the customer reported (symptom, affected devices, scope, onset, prior attempts) **and** the troubleshooting steps with the key findings they produced — specific values, states, discoveries — so the next agent can act without redoing the work.
- **Partially Met:** Issue or steps present but incomplete — a vague summary, missing key steps, or findings described only in general terms.
- **Not Met:** No issue summary or no troubleshooting record despite a full session — the next agent would have to start over.
- **Not Applicable:** When the contact was purely informational with no issue or troubleshooting to record.

**D2. Captured the reasoning behind decisions, recommendations, escalations, and actions** — including colleague / SME input when no private note applies. *(Core)*
- **Met:** Notes explain key decisions — why a path or closure was chosen, what criterion an escalation met, and any colleague/SME consultation that shaped the approach (captured in the case notes when no private note applies).
- **Partially Met:** Some reasoning captured but key decisions lack explanation — an escalation with no documented rationale, or colleague input followed but not attributed.
- **Not Met:** Notes contain only actions with no reasoning — a case closed RESOLVED or escalated with no explanation of why; the decision-making cannot be reconstructed.
- **Not Applicable:** A straightforward interaction with no escalation, no consultation, and no ambiguous decisions requiring explanation.

**D3. Recorded clear next steps, follow-up requirements, and an accurate current case status.** *(Core)*
- **Met:** Notes specify what happens next (owner, action, timeline, conditions) with callback details where applicable, and the ticket status truthfully reflects the case at close — Resolved only when confirmed resolved, otherwise Escalated/Callback/Pending — with a closure reason.
- **Partially Met:** Next steps in general terms (no owner/timeline), or status mostly accurate but the closure reason missing or applied late.
- **Not Met:** No next steps documented, or the status misrepresents the case — marked RESOLVED when escalated or unresolved (premature closure), misleading the next person.
- **Not Applicable:** Only when not observable (insufficient evidence); status must always reflect reality.

**What to watch:** The most harmful documentation failure is **premature closure** — marking a case RESOLVED when it is known to be unresolved. Notes must carry the full history, including pre-ticket contacts, so no agent treats a long-running case as new.

---

## Cross-Cutting Guidance

### Paid Support & Warranty
Paid support can be appropriate but must not replace basic triage. **Penalize** (Resolution/Escalation, and *Hard-selling* auto-zero in severe cases) when the agent pushes paid support before understanding the issue, repeats the offer after refusal without adding value, blocks safe basic guidance behind payment, or explains warranty/eligibility incorrectly. **Do not penalize** simply because a device is out of warranty or the call does not convert. For an out-of-warranty customer who declines paid support, handling is still good if the agent provides at least one practical self-help path: a specific article, an emailed set of steps, the official chatbot/self-service path, or safe basic guidance.

### Call Structure — What Good Interactions Usually Do
| Area | Good practice | Categories affected |
|------|--------------|---------------------|
| Opening | Restate the issue; set expectations for the path | Communication, Resolution |
| Problem understanding | Identify topology (modem/router/parent/child/extender); confirm symptom, trigger, what was tried | Technical, Communication |
| Troubleshooting flow | Logical path; validate one step before the next; confirm outcome | Technical, Resolution |
| Credential & environment | Clarify early: Wi-Fi vs admin password, app vs router login, physical access | Technical, Communication |
| Customer handling | Acknowledge frustration; slow down when confused; one action at a time | Customer Experience, Communication |
| Resolution / escalation | Explain the outcome; explain why escalation is needed; set next step and timeframe | Resolution, Escalation, Ownership |

### Accent & ASR Normalization
Agents are primarily Filipino (Visayan/Cebuano accents); the transcription (ASR) may mishear specific terms. **Grade whether the customer's comprehension was adequate for the interaction to proceed — not whether the transcript matches Standard American English.** Do **not** penalize: TH→D/T (`de`, `dat`, `dis`), P/F switching (`prom`, `pirst`), B/V switching (`berify`, `bery`), number homophones (`fifty` may mean `fifteen`; Linksys paid support is $15, not $50), or pronoun-gender mixing. Accent becomes a Communication signal **only if** the customer asks for the same instruction to be repeated **≥ 2 times on the same step** *and* context indicates accent (not instruction complexity) was the cause.

### Payment / PCI / Recording
Flag for human/compliance review when payment data or redaction markers appear. **Do not** penalize solely because card data or a redaction marker is present. **Penalize** Documentation/Communication when payment terms, fees, or paid-support expectations are unclear. Severe mishandling — reading back a full card number, CVV, or expiry, or a coercive/confusing payment flow — is a **PCI auto-zero** condition.

---

## Auto-Zero & Critical Failures

Some conditions override the weighted score or force review regardless of it. Default every gate to *not triggered* and set it only on **positive evidence**.

**Auto-zero (forces the overall score to 0%):** any compliance gate failed — **Callback Hours**, **PCI & Information Security**, or **Sales** — or any of the A–K critical items present: **A** Call/Session Abandonment · **B** Avoidance/Evasion · **C** Discourtesy · **D** Escalation abuse · **E** Failure to ask for the email address · **F** Fraud · **G** Hard-selling · **H** Line Release · **I** Non-Adherence to Callback Hours · **J** Non-Adherence to PCI/Info-Sec · **K** Non-First Call Resolution. Category scores still display, for coaching. Where a gate depends on data beyond the transcript and cannot be confirmed, do not auto-zero — flag for human review instead.

**Coaching flags (raised when an indicator is Partially Met or Not Met):** Technical accuracy (T3) · Missed follow-up/callback (O2) · Commitments not honored (O1) · Customer left without a path forward (R2) · Escalation decision inappropriate (E1) · Escalation poorly executed (E2) · Professionalism concern (X1) · Ticket status inaccurate / premature closure (D3).

**Critical-failure conditions (force review regardless of score):** harmful or materially incorrect troubleshooting; misrepresented product capability; an unsupported root-cause claim presented as fact; no follow-up after a disconnect; a promised action not completed; the customer abandoned without a path forward; escalation without reasonable troubleshooting or to avoid ownership; rude/dismissive conduct; or a policy violation.

---

## Resolution Outcome (overall classification)

Independently of the weighted score, classify the interaction (first match wins):

1. **Unresolved** — R1 Not Met and R2 Not Met (no meaningful progress, no path forward).
2. **Ownership Gap** — technical progress was made (R1 not Not Met) but ownership failed (O1 or O2 Not Met) — e.g., premature closure or a missed callback.
3. **Appropriate Escalation** — an escalation occurred, E1 Met and E2 not Not Met, and the issue is not yet fully resolved.
4. **Successful Resolution** — R1 Met.
5. **Partial Resolution** — otherwise (some progress; core issue open or unconfirmed).

---

## Overall Score Calibration Summary

| Situation | Expected category scores | Overall band |
|-----------|--------------------------|--------------|
| Clean resolution, good process | mostly 4–5 | Meets / Exceeds |
| Resolved with minor misses | mostly 3–4 | Developing → Meets |
| Unresolved but good process, concrete next steps | Resolution 3–4 | Developing |
| Unresolved, meaningful troubleshooting but flawed | Resolution 2–3 | Developing → Needs Improvement |
| Weak, incomplete, poorly structured | mostly 2–3 | Needs Improvement |
| Operational breakdown, wrong guidance, severe failure | 0–2 | Needs Improvement (or Auto-Zero) |

**Hard rules:**
- Any compliance/payment concern → human review; do not assign a high overall score without it.
- Repeated accuracy errors → Technical Accuracy cannot score high even if communication was polite.
- Missing model/serial/warranty when relevant → Resolution/Technical reflect it; do not score those high.
- Chaotic flow or repeated loops → Communication & Call Control cannot score high.
- Poor call control → Communication cannot score high even if the tone was polite.

---

## Output Format for AI Evaluations

For each case, the AI should produce, in a consistent and parseable form:

1. **Per indicator** (all 19: R1–R3, T1–T3, C1–C2, O1–O3, E1–E2, X1–X3, D1–D3) — the rating (`Met` / `Partially Met` / `Not Met` / `Not Applicable`), a short **evidence quote or observation**, and a **confidence** (0–1). For `Not Applicable`, note whether it is *not applicable to this case* or *insufficient evidence*.
2. **Per category** — the derived 0–5 score.
3. **Overall** — the weighted percentage, the result band, any auto-zero triggers, the coaching flags, the resolution-outcome classification, and any critical failures.
4. **A 2–4 sentence summary** citing the decisive evidence.

The category scores, overall percentage, coaching flags, and outcome are **derived** from the indicator ratings by the rules above — they are not scored independently.

---

## How to Update This Rubric

The QA team owns the business rubric. You can update the behavioral expectations and **Met / Partially Met / Not Met / Not Applicable** criteria for any indicator, the calibration guidance, the cross-cutting themes, the 5-press exception list, and the accent patterns.

**Keep this document and the QA Scoring Form Template in lockstep.** The seven categories, their weights, and the nineteen behavioral indicators are the shared structure; if one changes, change both. Indicator labels (R1 … D3) are stable references used to keep the two aligned — do not renumber them.

---

*Revised 2026-06-29 to synchronize with the QA Scoring Form Template (7 weighted categories · 0–5 scale · 19 behavioral indicators · auto-zero · coaching flags), retaining the readable structure of the original rubric while optimizing the evaluation criteria for consistent AI-based scoring.*
