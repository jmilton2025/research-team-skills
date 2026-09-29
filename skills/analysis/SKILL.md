---
name: analysis
description: Use when analyzing qualitative UX research data, from one transcript through larger interview or open-response corpora, including pilot-signal synthesis, affinity synthesis, thematic analysis, or qualitative tagging; not for moderation or final stakeholder storytelling.
---

# UX Research Analysis

Use this skill to turn authorized, deidentified qualitative data into bounded, auditable research findings. The researcher owns the interpretation and final approval; AI extracts, organizes, challenges, and documents evidence.

## Non-negotiable contract

1. **Do not open or process a source until the pre-ingestion authorization and privacy gate passes.**
2. **Analyze only the exact approved scope.** A request for “five” items is not enough; identify the five tasks, sections, responses, files, or line ranges.
3. **Trace every evidence item to an exact source locator and preserve how it was elicited.**
4. **Keep stated evidence separate from inference.** Never invent or silently repair quotes.
5. **Match claim strength to the sample and method.** One session cannot establish a theme, pattern, prevalence, saturation, or transferable product recommendation.
6. **Run evidence QA before asking the researcher to approve findings.** Do not use researcher approval to discover preventable evidence errors.
7. **Run mode-aware final QA before delivery.** A limitation must stay visible; approval does not convert weak evidence into strong evidence.

## H.E.A.R.T. operating principles

| Principle | Required behavior |
|---|---|
| **Human-centered** | Preserve participant meaning, context, contradictions, and potential harm. |
| **Experience-focused** | Keep the workflow and output clear enough for the intended audience to use. |
| **Amplifying** | The researcher chooses the question, scope, method, and final interpretation. |
| **Responsible** | Enforce authorization, privacy, purpose limitation, and evidence boundaries. |
| **Transparent** | Attribute AI assistance, document the method, and expose uncertainty and limitations. |

## Workflow at a glance

| Stage | Work | Gate |
|---|---|---|
| 1 | Intake metadata without opening sources | Authorization, reuse, and deidentification confirmed |
| 2 | Open the approved source and audit data quality | No unexpected identifiers; provenance and scope recorded |
| 3 | Route by sample and objective; propose method | Researcher approves framing, exact scope, and method |
| 4 | Extract evidence and develop bounded claims | Evidence ledger complete |
| 5 | Run early evidence QA | Unsupported or mis-scoped claims revised or removed |
| 6 | Present the draft for researcher approval | Consolidated by default for n=1–4; unit-by-unit optional |
| 7 | Run final QA, fold fixes, and deliver | Materially changed claims reapproved |

## 1. Pre-ingestion authorization and privacy gate

Before reading a pasted transcript, opening an attachment, following a document link, transcribing media, or sending content to another tool, gather only metadata:

- data type and volume;
- source location and access method;
- research question and intended audience;
- exact requested scope;
- whether the researcher is authorized to use the data for AI-assisted analysis;
- whether participant consent, company policy, and the original collection purpose permit this use;
- whether the source was deidentified **before** being supplied.

Ask for a direct confirmation when any item is unknown. Record the basis, such as `researcher attestation`, an approved protocol, or a consent artifact.

### Gate decision

- **Pass:** authorization and permitted use are confirmed, and the supplied source is already deidentified. Continue.
- **Stop:** authorization, reuse scope, or deidentification is absent or uncertain. Do not open the source. Ask for an authorized, deidentified replacement or for processing in an organization-approved secure environment.
- An approved local preprocessing tool may redact the source only if it keeps raw content outside model and conversation context. Verify the redacted derivative before analysis.

Never say that raw PII was “scrubbed after receipt.” Once raw content has entered model or conversation context, later redaction cannot remove that exposure or rewrite history. If unexpected PII appears after opening a source, do not repeat it; stop analysis, state that the exposure cannot be undone, and request a properly deidentified replacement.

## 2. Source, quality, and exact-scope audit

After the gate passes, inspect the approved source and record:

- legibility, completeness, truncation, transcription uncertainty, and missing stimuli;
- speaker separation and normalized participant IDs;
- consent/provenance evidence and whether this is a secondary-use analysis;
- residual direct or contextual identifiers;
- exact included and excluded source units.

Define scope with stable locators: task or section IDs, question IDs, response IDs, timestamps, page/paragraph IDs, row IDs, or line ranges. If the source has none, assign stable IDs before analysis. Record exclusions explicitly. Do not draw evidence from material outside the approved scope, even when it is present in the same file.

Minor transcription uncertainty may remain if it is flagged at the affected evidence item. Material ambiguity, uncertain speaker attribution, or residual identifiers block analysis of that passage.

## 3. Route by sample and research objective

Count independent participants or response units, not pages or excerpts. Use volume as a starting route and the research objective as the final decision.

| Sample | Default route | What it can support |
|---|---|---|
| **n=1** | **Single-Session Evidence Memo** | Participant-specific evidence, bounded interpretation, hypotheses, and research validation priorities |
| **n=2–4** | **Pilot Signals** | Directional convergence, divergence, contradictions, and questions to validate; not cross-population themes |
| **n=5–10** | **General Affinity Synthesis** | Cross-session clusters and patterns with exact participant support |
| **n=10–30** | **Thematic Analysis, when the objective is patterns of shared meaning** | Developed themes with a coherent methodological variant |
| **n=30+** | **Tagging** | Systematic coding, filtering, and frequency reporting; survey opens may require a larger threshold |

At **n=10**, choose by objective: use affinity for a rapid “what did we hear?” briefing, or thematic analysis for interpretive patterns of shared meaning. A pre-existing schema or counting objective may justify tagging at a smaller n; document the exception rather than pretending volume alone chose the method.

When n=1, read [single-session-analysis.md](references/single-session-analysis.md) in full. For affinity, thematic analysis, tagging, method variants, codebook design, the ladder of inference, and IRR, read only the relevant section of [analysis-methodology.md](references/analysis-methodology.md). Preserve these coherence rules:

- Reflexive thematic analysis constructs themes through researcher interpretation and does **not** use IRR.
- Coding-reliability or codebook approaches may use agreement checks when the objective requires coder convergence.
- Tagging requires explicit definitions, inclusion criteria, exclusion criteria, and examples.
- Safety- or harm-relevant evidence is surfaced regardless of frequency and labeled low-n/high-severity.

### Pilot Signals, n=2–4

Report each signal with exact support (`2 of 3 participants`), divergent or contradictory cases, source-backed evidence, multidimensional confidence, and a validation question. Call it a **signal**, not a theme or general user pattern. Do not convert small-n support into percentages, saturation claims, or population prevalence.

## 4. Approve framing, method, and scope

Before substantive analysis, show one compact proposal containing:

- research question and audience;
- data, sample, and exact included/excluded scope;
- recommended mode and methodological variant;
- unit of analysis and intended claim language;
- known data-quality, consent, or secondary-use limitations;
- approval cadence.

Ask the researcher to approve or revise the proposal. For **n=1–4**, consolidate these decisions into one pre-analysis approval by default and plan one approval of the QA-checked draft. Offer unit-by-unit review when the researcher wants it or when risk and ambiguity make it useful. For larger studies, grouped or unit-by-unit approval is appropriate; a researcher may request one whole-draft review.

Do not add a separate style-selection gate to the analysis method. Formatting and publication decisions happen only after the analysis is approved.

## 5. Build an evidence ledger before writing claims

Every quote, observed behavior, or analytic note used in a claim needs these fields:

| Field | Required value |
|---|---|
| **Evidence ID** | Stable unique ID |
| **Participant / unit** | Deidentified ID |
| **Source** | File, session, or response set |
| **Source locator** | Exact timestamp, task/section, response ID, page/paragraph, row, or line |
| **Evidence text** | Verbatim text or precise behavioral description; mark transcription uncertainty |
| **Evidence origin** | `observed`, `spontaneous`, `prompted`, or `annotation` |
| **Attribution certainty** | `certain`, `probable`, or `uncertain` with reason when not certain |
| **Claim status** | `stated` or `inferred`; explain the inference |
| **Scope status** | Included scope unit and any relevant exclusion |

Quotation marks mean verbatim. Mark paraphrases as paraphrases and do not put them in quotation marks. A platform label, moderator annotation, or analyst note is not participant speech. Prompted evidence remains valid but must not be presented as spontaneous. Observed behavior and self-report remain distinct.

Develop claims upward from this ledger:

`evidence → observation/finding → bounded interpretation → implication`

Do not skip a rung. Actively seek negative, contradictory, and boundary evidence. Keep participant context separate from findings unless it directly answers the research question.

## 6. Confidence is multidimensional

Do not attach an unexplained single `High / Medium / Low` label to a finding. For each major claim, rate and justify:

- **source integrity** — clarity and completeness of the underlying passage;
- **attribution certainty** — confidence in who said or did it;
- **evidence directness** — distance between the source and the claim;
- **within-case coherence** — consistency or contradiction within a participant/response;
- **cross-case support** — exact support across independent participants; `N/A` for n=1;
- **transferability** — what contexts the evidence may reasonably inform; normally `Not assessable` for n=1.

Use `High`, `Medium`, `Low`, or `N/A / Not assessable` per dimension with a short rationale. Do not average dimensions into false precision. If a summary label is required, it cannot exceed the weakest dimension material to the claim.

## 7. Early evidence QA, then researcher approval

Before showing findings for approval, read and run the **Early Evidence QA** in [quality-gates.md](references/quality-gates.md). Mechanically verify quote-marked text against the source, source locators, attribution, scope, evidence origin, stated-versus-inferred status, claim fit, contradictions, and confidence. Revise or remove failures first.

Then present the QA-checked draft:

- **n=1–4:** one consolidated approval by default, with an optional unit-by-unit path;
- **n=5+:** grouped or unit-by-unit approval, with a whole-draft option;
- show what is approved, revised, excluded, and still uncertain;
- never interpret a partial selection as permission to silently drop the rest—read back the change.

The researcher may edit or reject any claim. Approval locks the analytic meaning, not hidden evidence defects.

## 8. Final QA and delivery

After researcher approval, run the mode-aware final gate in `quality-gates.md`. Use only `Pass`, `Pass with limitation`, `Fail`, or `N/A`, with evidence and a reason for every limitation or N/A. Run an independent review when available without moving deidentified data outside its approved environment. Fold confirmed fixes into the draft. If a fix materially changes an approved claim, its evidence, confidence, or implication, return only that affected unit for reapproval.

Do not deliver while any applicable check is `Fail`. A final `Pass with limitation` is acceptable only when the limitation is explicit and does not invalidate the claims.

After analytic approval and final QA, follow the [delivery rules](references/delivery-routing.md) as the single authoritative source for artifact type, formatting, test labeling, destination confirmation, creation, and verification. Do not duplicate or override those rules here.

## Completion contract

A run is complete only when:

1. pre-ingestion authorization, reuse, and deidentification were confirmed before the source was opened;
2. source quality, provenance, and exact scope were recorded;
3. the researcher approved the framing, method, and scope;
4. the evidence ledger supports every retained claim;
5. early evidence QA ran before findings approval;
6. the researcher approved the QA-checked analysis;
7. final mode-aware QA ran, material fixes were reapproved, and no applicable check failed;
8. the selected artifact was created and verified according to the authoritative delivery route.

If a required step could not run, say so precisely. Never report a blocked or skipped step as complete.

## Boundaries and handoffs

- Use `/research-plan` upstream when the research question or study design is not yet defined.
- Use `/mod-guide` for a discussion or usability-session guide.
- Use `/report` after the analysis is approved when the task is stakeholder storytelling rather than evidence synthesis.
- Use a structured-data analysis workflow for large quantitative tables; this skill is for qualitative evidence.
