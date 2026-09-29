# Analysis Quality Gates

Use this reference twice:

1. **Early Evidence QA** after the evidence ledger and draft claims exist, before researcher approval.
2. **Final Mode-Aware QA** after researcher approval and before delivery.

These gates assess evidence and method. Researcher approval does not waive a failed check.

## Status vocabulary

Use only these statuses for final QA:

| Status | Meaning | Action |
|---|---|---|
| **Pass** | The check is satisfied with traceable evidence. | Continue. |
| **Pass with limitation** | A real limitation remains, is disclosed, and does not invalidate the retained claim. | Continue cautiously; preserve the limitation. |
| **Fail** | The check is unsupported, unsafe, methodologically incoherent, or materially misleading. | Revise, remove, or stop. Do not deliver. |
| **N/A** | The check is structurally inapplicable to this mode or sample. | State why; do not use N/A to avoid work. |

Do not use letter grades. Do not convert a failure into a pass because the researcher wants speed.

## Gate 1: Early Evidence QA

Run this gate on every proposed claim before showing findings for approval.

| Check | Pass condition |
|---|---|
| **Approved scope** | Every evidence item falls inside an exact included task, section, response, timestamp, row, paragraph, or line range. |
| **Source locator** | Another reviewer can find the passage without guessing. |
| **Quote authenticity** | Every quote-marked string is mechanically found in the approved source, or an explicit transcription normalization is documented. |
| **Attribution** | Participant/unit identity and speaker attribution match the source; uncertainty is visible. |
| **Evidence origin** | `observed`, `spontaneous`, `prompted`, or `annotation` is recorded and represented accurately. |
| **Stated vs inferred** | Direct statements and analyst inference are visibly separated; the inference explains its evidence path. |
| **Observation vs interpretation** | The observation stays close to source; the interpretation does not masquerade as fact. |
| **Prompt/stimulus context** | The moderator prompt or stimulus needed to understand the response is retained or linked. |
| **Contradictory evidence** | Later, weaker, negative, and boundary evidence was actively checked and either included or documented. |
| **Claim fit** | Wording matches sample, evidence type, and method; no population leap or causal claim is introduced. |
| **Confidence dimensions** | Every major claim has reasoned dimension ratings, not an unexplained overall label. |
| **Privacy** | No direct/contextual identifier is reproduced, and unexpected PII triggered the stop rule. |

### Mechanical quote check

1. Extract every string shown in quotation marks anywhere in the draft, not only quote blocks.
2. Search the approved source for each exact string.
3. Record `found`, `normalized`, or `not found`, with locator.
4. For `normalized`, document only harmless transcript normalization such as corrected spacing; do not silently repair meaning.
5. A `not found` quote is a failure: replace it with verified verbatim text, mark a paraphrase without quotation marks, or remove it.

Do not count repeated uses of one quote as independent evidence. Do not use an analyst-created title in quotation marks if it could be mistaken for participant language.

### Early-QA outcome

- Revise or remove every failed evidence item or claim.
- Quarantine unresolved ambiguity rather than smoothing it over.
- Then show the cleaned draft and the important limitations to the researcher for approval.
- If n=1–4, show one consolidated draft by default; unit-by-unit review remains available.

## Multidimensional confidence

Rate each material claim on the dimensions below with `High`, `Medium`, `Low`, or `N/A / Not assessable`, plus a one-line rationale.

| Dimension | High | Medium | Low / Not assessable |
|---|---|---|---|
| **Source integrity** | Complete, legible passage with necessary context | Minor gaps or transcription noise that do not change meaning | Material truncation, missing stimulus, or unclear wording |
| **Attribution certainty** | Speaker/unit is explicit and consistent | Attribution is probable from structure but not labeled | Speaker is ambiguous or conflicting |
| **Evidence directness** | Claim closely restates observed behavior or explicit statement | Modest interpretation or prompted self-report | Long inferential leap, annotation-only support, or missing link |
| **Within-case coherence** | Repeated/consistent within the case and no material contradiction | One clear instance or a manageable contradiction | Contradictory, isolated, or context-dependent evidence |
| **Cross-case support** | Exact support across an adequate, relevant sample | Limited or uneven support, reported exactly | `N/A` for n=1; small pilot support cannot establish prevalence |
| **Transferability** | Sample/context aligns with the bounded target and limits are known | Context match is partial or uncertain | `Not assessable` for n=1; major sampling/context gap |

Prompted evidence is not automatically weak; its origin changes what can be claimed about spontaneity. Annotation evidence may explain context but cannot substitute for participant speech or behavior.

Do not average the dimensions. If a summary confidence label is needed, identify which dimension constrains it.

## Gate 2: Final shared QA

After researcher approval, check every retained claim and the analysis as a whole.

| Check | Required result |
|---|---|
| **Authorization and purpose** | Authorization, consent/reuse basis, secondary-use status, and deidentification are documented truthfully. |
| **Scope integrity** | Included/excluded units match the approved scope; no scope bleed occurred. |
| **Coverage** | Every relevant in-scope idea maps to a retained finding, contradiction, exclusion, or documented uncertainty. |
| **Provenance completeness** | Evidence ledger fields are complete for every cited item. |
| **Quote and attribution audit** | Mechanical quote check and attribution check passed. |
| **Evidence/claim separation** | Observation, interpretation, implication, and recommendation/hypothesis are not collapsed. |
| **Contradictions** | Disconfirming and boundary evidence is visible and affects confidence where appropriate. |
| **Claim calibration** | Counts, percentages, frequency language, causality, and transferability do not exceed the evidence. |
| **Confidence** | Multidimensional ratings are consistent with the evidence and limitations. |
| **Method coherence** | The work performed matches the named method and variant. |
| **H.E.A.R.T.** | Human authority, participant grounding, privacy, responsible limitations, and AI transparency are visible. |
| **Process transparency** | Method, analysis passes, AI role, researcher approvals, deviations, and limitations are documented. |
| **Safety/severity** | Low-frequency evidence with serious harm was not suppressed by pattern thresholds. |

## Mode-aware QA

Apply only the row for the selected mode. Mark other modes `N/A` with the reason.

### Single-Session Evidence Memo, n=1

- Claims use participant/session-specific language; no “users,” segment, or population leap.
- No themes, cross-user patterns, prevalence, percentages, saturation, or representativeness claims.
- Participant context is not promoted into a product finding without evidence.
- Cross-case support is `N/A`; transferability is `Not assessable`.
- Implications are research-only, and validation priority ranks evidence needs—not product work.
- No product prescription, roadmap owner, effort estimate, or P0/P1/P2 priority appears.

### Pilot Signals, n=2–4

- Output uses `signal`, `convergence`, `divergence`, or `hypothesis`, not generalized themes.
- Every signal reports exact participant support and the cases that contradict it.
- No percentages, saturation, population prevalence, or transferable recommendations are claimed.
- Validation questions and sample limitations accompany each signal.

### General Affinity Synthesis, n=5–10

- Each cluster is built from traceable observations across participants, not repeated excerpts from one person.
- Exact participant counts and denominators are reported; the agreed pattern rule is documented.
- Outliers and below-threshold evidence remain visible as outliers, hypotheses, or safety flags.
- Observation, pattern, insight, and implication follow a traceable ladder without skipping rungs.

### Thematic Analysis, usually n=10–30

- The selected variant—reflexive, codebook, or coding reliability—is explicit and coherent.
- Each theme has a central organizing concept and is more than a topic summary.
- Theme construction is traceable through familiarization, coding, generation, review, definition/naming, and write-up.
- Reflexive work uses active construction language and does not claim IRR; agreement checks appear only for compatible variants.
- Boundary cases, researcher reflexivity, and theme relationships are documented.

### Tagging, usually n=30+

- Every tag has a name, definition, inclusion criteria, exclusion criteria, and verified example.
- Deductive, inductive, or hybrid orientation and tag-evolution decisions are documented.
- Counts use the correct unit and denominator; excerpt frequency is not presented as participant prevalence.
- Multi-coder reliability is reported only when actually run, with sample, metric, and disagreement handling.
- Overlap, vague/other codes, uncoded material, cold tags, and drift were checked.

## Independent review

When an independent reviewer or multi-agent review is available inside the approved data environment, use it after researcher approval and before finalizing. Give the reviewer the approved scope, evidence ledger, draft, method, and deidentified source. Ask for:

- quote and locator verification;
- scope and attribution errors;
- unsupported inference or overgeneralization;
- missed contradiction or later-session evidence;
- method-variant coherence;
- confidence and limitation calibration.

Do not move data to a new tool or reviewer outside the authorization boundary. If independent review is unavailable or not permitted, mark it `N/A` with the reason and set the overall gate to at most `Pass with limitation`; never claim it ran.

## Final outcome and reapproval

Use a compact table:

| Check | Status | Evidence / limitation | Fix |
|---|---|---|---|
| [check] | Pass / Pass with limitation / Fail / N/A | [specific support or reason] | [change made or needed] |

Overall outcome:

- **Pass** — all applicable checks pass.
- **Pass with limitation** — no applicable check fails; one or more disclosed limitations remain but do not invalidate the bounded claims.
- **Fail** — at least one applicable check fails. Revise, remove, or stop before delivery.
- **N/A** — allowed only for an individual structurally inapplicable check, not as the overall result of an analysis run.

After fixes, return for researcher reapproval only when the analytic meaning materially changed: claim wording, evidence basis, confidence, implication, priority, or inclusion/exclusion. Typographic and layout-only changes do not require analytic reapproval.
