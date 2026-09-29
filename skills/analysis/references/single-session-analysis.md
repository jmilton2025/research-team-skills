# Single-Session Evidence Memo

Use this method only when the approved scope contains one participant, session, diary entry, or independent response unit (`n=1`). It is a within-case read, not a miniature cross-participant synthesis.

## What n=1 can and cannot support

It can support:

- what this participant explicitly said or did;
- a bounded interpretation of that evidence;
- contradictions and ambiguity within the session;
- hypotheses and research questions for later validation;
- research-only implications for recruiting, instrumentation, task design, or the next study.

It cannot support:

- themes, cross-user patterns, prevalence, percentages, saturation, or representativeness;
- claims about “users,” “customers,” a segment, or a population;
- product recommendations, roadmap priority, owners, effort sizing, or P0/P1/P2 labels;
- confidence in transferability beyond the case.

Use singular, attributed language: `P01 reported…`, `In this task, P01…`, or `This session suggests a hypothesis…`. Avoid `users need`, `customers struggle`, `the research shows`, `a theme emerged`, `many`, `most`, and `X%`.

## Required inputs

Before analysis, record:

- research question and intended audience;
- participant/session ID;
- exact included and excluded tasks, sections, timestamps, or line ranges;
- original study purpose and whether this is a secondary read;
- authorization/consent basis and deidentification status;
- known transcript, speaker, stimulus, or provenance limitations.

Read the full approved scope before extracting evidence. If only part of a session is in scope, do not use the rest to strengthen or resolve claims.

## Analysis sequence

1. **Familiarize within scope.** Read the approved material end to end; note uncertainties without correcting them silently.
2. **Build the evidence ledger.** Include every provenance field required by the main skill.
3. **Separate context from findings.** Category familiarity, demographics, or stated habits are participant context unless they directly answer the research question.
4. **Draft the smallest defensible finding set.** Each evidence unit contains a participant-specific claim, its evidence, a bounded interpretation, and its uncertainty. For one narrow research question, default to one integrated finding; treat supporting strategies, examples, tensions, and boundary conditions as evidence or complication within that unit. Split only when the claims answer materially different subquestions and combining them would hide a real distinction.
5. **Search for complication.** Check later passages, contrary statements, moderator prompting, task artifacts, and ambiguous attribution.
6. **Run early evidence QA.** Fix provenance and claim problems before researcher approval.
7. **Assign research validation priorities.** Prioritize what to test next, not what a product team should build.

## Evidence-unit schema

Use one unit per analytically distinct claim, not one unit per quote, cue, or supporting example. A narrow n=1 task often needs one finding plus participant context.

| Field | Content |
|---|---|
| **Participant-specific claim** | One sentence limited to this participant and approved scope |
| **Evidence** | Verbatim quote or observed behavior with Evidence ID and exact source locator |
| **Origin** | `observed`, `spontaneous`, `prompted`, or `annotation` |
| **Attribution certainty** | `certain`, `probable`, or `uncertain`, with rationale when needed |
| **Status** | What is directly `stated` versus what is `inferred` |
| **Observation** | Close-to-source description of what happened or was said |
| **Bounded interpretation** | What the evidence may mean for this participant; no population leap |
| **Contradiction / ambiguity** | Evidence that complicates the claim, or `none found within approved scope` |
| **Confidence dimensions** | Source integrity, attribution, directness, within-case coherence, cross-case support (`N/A`), transferability (`Not assessable`) |
| **Research-only implication** | A next-research action, not a product action |
| **Validation priority** | `High`, `Medium`, or `Low`, with rationale |

One quote may support more than one interpretation, but do not duplicate it to simulate evidence volume. A repeated idea from one participant increases within-case coherence, not sample support.

## Research-only implications

Allowed implications change what researchers do next. Examples:

- recruit participants with and without prior category experience;
- observe the behavior in a realistic task rather than rely on self-report;
- add a probe that distinguishes weight, serving count, and package format;
- test whether a signal recurs across household types;
- collect the missing stimulus or product-state context.

Disallowed implications prescribe product action from one case. Do not recommend building, shipping, prioritizing, assigning, or measuring a feature from n=1. Convert such an idea into a hypothesis and a research test.

### Validation priority

Validation priority ranks the **need for more evidence**, not product importance:

- **High** — the hypothesis could materially affect a consequential decision, current evidence is insufficient, and a follow-up study can test it.
- **Medium** — plausible and relevant, but the decision risk or immediacy is lower.
- **Low** — interesting but weakly connected to a current decision, or better monitored before dedicated research.

Do not infer priority from emotional wording alone. Consider decision consequence, uncertainty, and feasibility of validation.

## Recommended memo structure

1. **Scope and question** — one session, exact included units, audience, and purpose.
2. **Data quality and provenance** — authorization basis, deidentification, transcription/speaker limitations, secondary-use status.
3. **Participant context** — only context needed to interpret the evidence; explicitly not a finding.
4. **Evidence units** — use the schema above.
5. **Contradictions and unresolved ambiguity** — including places where no defensible interpretation is possible.
6. **Hypotheses and validation plan** — ordered by validation priority.
7. **Limitations and method note** — state that n=1 does not establish patterns or transferability and describe AI assistance.

## Claim-language examples

| Avoid | Use instead |
|---|---|
| `Users struggle to judge portion fit.` | `P01 said judging portion fit was difficult in Task 4.` |
| `Serving count would solve the problem.` | `Hypothesis to validate: category-appropriate size cues may reduce uncertainty.` |
| `A frozen-food theme emerged.` | `Participant context: P01 reported more frozen-food than meal-kit experience.` |
| `High confidence finding.` | `Source integrity: High; attribution: High; interpretation directness: Medium; cross-case support: N/A; transferability: Not assessable.` |

## Stop conditions

Remove or quarantine an evidence unit when:

- the passage falls outside approved scope;
- speaker attribution is materially uncertain;
- a quote cannot be found verbatim;
- the claim depends on a platform annotation presented as participant speech;
- the interpretation requires missing stimulus or context;
- residual identifying information is necessary to state the claim safely.

An empty memo with clearly documented limitations is more rigorous than a polished unsupported finding.
