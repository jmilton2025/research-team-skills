# Synthesis Tail Templates

Plan-level templates for the 5-component synthesis tail (SKILL.md, "Synthesis tail" section, Output-structure component 5). These are drafting starting points at the plan level — they name the format and give placeholder wording so the plan reads as a real deliverable, not a checklist of labels. Full platform-tagged, programmer-ready versions (header tags, block labels, type-appropriate closes, the `> USERTESTING QUESTION TYPE` opener) are [[usertesting-script]]'s job — don't copy these directly into a script without running them through that skill's 4-way tagging discipline.

---

## 1. Recap MULTI-SELECT

Swap the bracketed verb/subject for whatever fits the study; the structure (multi-select + explicit escape option) is fixed.

```
Which of these would you no longer [use / shop from / trust / cook from]?
[Item 1]
[Item 2]
[Item 3]
None — I would still [use] all of them
```

Item order matches the order participants experienced the tasks (not randomized) — see usertesting-script's Rule 10/Rule 9 cross-reference.

## 2. Verbal "why?"

Asked immediately after the multi-select, before any other question — forces commitment before rationalization.

```
You said you'd no longer [use/trust] [item(s) selected]. Walk me through why.
```

If nothing was selected in the multi-select ("None"), keep the same slot but flip the framing:

```
You said you'd still [use/trust] all of these. What made you feel confident about all of them?
```

## 3. Pain-point question — pick ONE format

Choose based on the measurement goal (SKILL.md, Synthesis tail, item 3):

**DRAG-TO-RANK** — goal: detect hierarchy across 3+ pain points
```
Drag these into order from most to least [concerning/frustrating/confusing]:
[Pain point 1]
[Pain point 2]
[Pain point 3]
```

**SINGLE CHOICE with escape option pinned last** — goal: detect the single biggest pain point AND measure indifference
```
What was the single biggest issue for you?
[Pain point 1]
[Pain point 2]
[Pain point 3]
None of these bothered me
```

**VERBAL ranking with options on-screen** — goal: list is ≤6 items AND reasoning is part of the signal (collapses single-choice + verbal-why into one slot — don't also ask a separate verbal "why" if you use this format)
```
Looking at this list, which of these would you rank as the biggest issue, and which the smallest? Walk me through your reasoning as you go.
[Pain point 1]
[Pain point 2]
[Pain point 3]
```

## 4. Detection timing question

```
When would you first notice this — right away, partway through, or only after [completing the task / receiving the result]?
```

Adapt the trailing clause to the study's actual end-state (a delivered cart, a completed booking, a submitted form) — "receiving the result" is a placeholder, not literal wording.

## 5. Directive closing prompt

Never generic ("Any final thoughts?"). Ask 2–3 specific things, ~60 sec.

```
What could we improve about this experience? What would make this process easier for you? Was there anything you didn't like, or any features you wished worked differently?
```

Full alternates for feature-specific and comparison studies live in usertesting-script's `references/closing-card-templates.md` — reuse that file rather than forking a second copy here once the study reaches script stage.

---

## Sequencing reminder

Order is fixed regardless of which pain-point format is chosen: Recap multi-select → Verbal why → Pain-point question → Detection timing → Directive closing. All five run after per-task questions and before demographics (Discipline rules: "Demographics at the END").
