# Moderation-guide release tests

These offline tests protect the default **Option 4 — Leadership** Google Docs
delivery path and the cross-file `/mod-guide` contract. They use only the Python
standard library and make no Google API calls.

## Run the release gate

From the repository root:

```bash
python3 skills/mod-guide/tests/validate_contract.py
python3 skills/mod-guide/tests/test_option4_guide_layout.py
```

The layout file also runs under pytest when pytest is available:

```bash
python3 -m pytest skills/mod-guide/tests/test_option4_guide_layout.py
```

## What each gate protects

### `validate_contract.py`

The deterministic cross-file gate verifies:

- valid skill metadata and the required formatter, template, style, and safety
  assets;
- Option 4 is the single documented default, with plain native Docs only as an
  explicit or pre-approved disclosed fallback;
- the formatter resolves its contract package-relatively and contains no
  user-specific absolute path;
- the source-and-delivery safety reference is wired into the skill and contains
  authorization, minimization, consent, ACL, capability, idempotency,
  revision-reconciliation, and partial-artifact gates;
- both current OUTPUT TEMPLATE fences, and the SKILL.md shared scaffolding,
  use the canonical top matter: `# Moderation Guide`, `## Study Title`, a
  `Study period:` line, RACI, an optional `**Links:**` line, then the
  parameter table;
- interview and prototype templates retain their format-correct Objectives section,
  use a neutral incident gate before incident-specific follow-ups, and contain no
  unsafe `internal research only`, unconditional `Recording armed`, or Participant
  Grid defaults;
- the interview template keeps only Parameter and Consent tables, while the
  prototype template keeps only Parameter and `Phase | Description` tables,
  with the approved minutes in every Session Flow phase label;
- prototype topic bullets use italic `*Objective:*` / `*Key Questions:*` labels;
- participant-grid/log content stays outside the broadly shared guide; and
- the machine-readable visual contract describes the current template shapes
  and carries the reference-guide tokens (study period, 36pt list step, spacer
  rhythm, Links line, `[144, 554.4]` Session Flow); and
- the style reference names its reference guide without a Google Doc ID, and no
  skill file contains one.

### `test_option4_guide_layout.py`

The formatter suite constructs synthetic raw Google Docs JSON and exercises the
real parse, normalize, format, and verify functions. Coverage includes:

- the canonical top matter (title, study title, study period, RACI, Links line),
  warning, parameter dashboard, sections, lists, tables, and links;
- the reference vertical rhythm: one empty spacer paragraph between block
  groups, none after a band or H3, none before an H3, none between the Session
  Flow band and its table, and verifier rejection of a missing, extra, or
  styled spacer;
- an offline batch simulator (`apply_batch`) that applies each normalize batch,
  refuses edits Google Docs would refuse (such as deleting the newline before a
  table), and runs both fixtures, both templates, and noisy imports through
  normalize → re-fetch → repeat-normalize no-op → format → verify;
- study-period styling (DM Serif 16pt bold italic gray, 0/16pt), the study title
  as a NORMAL_TEXT paragraph, black underlined Links, italic Objective / Key
  Questions labels, bold topic lines as body text, and ☐ checklist bullets;
- rejection of a noncanonical H1 or a missing immediate Study Title H2;
- both current OUTPUT TEMPLATE fences through the complete offline pipeline;
- literal placeholders before links (`[TBD — fill in] · [Research plan](...)`),
  balanced brackets/parentheses, entities, and UTF-16 indices;
- ordered binding for exact duplicate prompts across separate phase lists, so the
  second occurrence cannot silently reuse the first paragraph;
- nested bullet geometry at a 36pt step (36/18, 72/54, 108/90pt) and verifier
  rejection when a nested probe is flattened or uses the old 18pt step;
- revision-bound normalize and format payloads, including rejection of missing,
  blank, stale, or mismatched revisions;
- a repeat normalize pass as an empty, revision-bound no-op;
- imported-header and horizontal-rule cleanup, exact pre-write hierarchy/header/
  cell/link binding, hidden-link rejection at normalize/format/final verify, and
  stale/tampered manifest rejection before any batch exists;
- private atomic JSON outputs that refuse overwrite, reject repository paths,
  and require an owner-only working directory;
- table geometry for `# | Ask`, Parameter, Consent, 3-column tables, and the
  `Phase | Description` Session Flow (`[144, 554.4]`, regular weight, white);
- every required formatting operation family, page geometry, section-band
  styling, bullet/numbered presets, and visual-drift rejection; and
- tables after the debrief, variable section names, and variable table counts.

## Fixtures

- `fixtures/mock-interview-guide.md` uses the canonical top matter with a
  Links line, a mock warning, extended ownership, nested interview probes, and
  additional table shapes used to pressure-test the structure-agnostic formatter.
- `fixtures/mock-prototype-guide.md` uses the same canonical top matter, a
  timed `Phase | Description` Session Flow, Objective / Key Questions topic
  bullets, H3 flow headings, task tables, and vendor back-matter. It
  intentionally omits the mock-warning paragraph to exercise the no-warning
  path.

Every fixture is a **TEST ARTIFACT**, never a real study.

## Behavioral subtype scenarios

Run these as isolated no-Drive dry runs after changing the router, either output
template, or the methodology. The run must read the current `SKILL.md`, safety
reference, selected format template, and methodology reference; return only
labeled Markdown; and make no external write.

### Diary check-in behavioral scenario

Use a 40-minute moderated remote check-in whose approved plan supplies five
de-identified diary entries and authorizes review of three during the session,
but does not authorize any new upload or photo request. The output passes only
when it renders a diary check-in (not an IDI label swap), allocates consent,
reconnect, entry review, and wrap-up to exactly 40 minutes, references only the
approved minimum-necessary entries, and does not request or retain new artifacts.

### Focus group behavioral scenario

Use a 75-minute moderated in-person focus group with six participants, approved
group ground rules, divergent discussion, and one approved prioritization
activity. The output passes only when it renders a focus-group flow (not a 1:1
IDI), totals exactly 75 minutes, includes turn-taking and dominant-voice
management, states only approved group-privacy limits, and does not promise
participant-to-participant confidentiality.

### Concept reaction behavioral scenario

Use a concept test with reaction/desirability hypotheses and no behavioral-use
objective. Approve P8 Include for the named first exposure. The output passes
only when it uses the 5-second hide-and-recall sequence, follows with neutral
comprehension/reaction/desirability prompts, maps every construct to a required
evidence-producing prompt, and contains zero invented `Task` rows.

### Usability Task-only behavioral scenario

Use a usability test with one task-completion hypothesis and no initial-reaction
objective. Approve P8 Task-only. The output passes only when each phase keeps
Scenario → Expectation → Task → Alignment, maps the completion hypothesis to an
observable task and cue, and contains zero First impression rows or placeholders.

## Live integration gate

Offline success does not prove Google Docs behavior. Before relying on the live delivery path,
run both current template shapes through a write-capable integration:

1. import Markdown into the confirmed permission-checked folder;
2. fetch raw tab content and a fresh revision;
3. apply the revision-bound normalize batch and re-fetch;
4. apply the revision-bound format batch and re-fetch;
5. run the verifier;
6. repeat normalize to confirm it is a no-op;
7. export/render and inspect the opening, dense interior, and final pages; and
8. confirm parent folder, effective permissions, content, links, and duplicate
   prevention before returning the Doc.
