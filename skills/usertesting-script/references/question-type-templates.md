# Question-Type Templates

Copy-paste blocks for all 4 allowed UserTesting question types, each with the full 4-way anti-platform-bug tagging (header tag / block label / type-appropriate close / programming opener). See SKILL.md Rule 2 for why all four places matter and Rule 1 for why "Written response" is never used.

Replace anything in `[brackets]`. Keep the block structure — headers, bold labels, blank lines, and the `>` programming opener — exactly as shown; the programmer scans for this pattern.

---

## VERBAL RESPONSE

```
### Question Q[N] — VERBAL RESPONSE

**Verbal response:**
[Prompt body]

Please give a verbal response.

> **USERTESTING QUESTION TYPE: VERBAL RESPONSE** (NOT Written response).
```

---

## SINGLE CHOICE

```
### Question Q[N] — SINGLE CHOICE

**Single choice:**
[Prompt body]

Options (see Rule 9 for whether this list randomizes):
1. [Option 1]
2. [Option 2]
3. [Option 3]

Please select one option.

> **USERTESTING QUESTION TYPE: SINGLE CHOICE** (NOT Written response).
```

---

## MULTI-SELECT

```
### Question Q[N] — MULTI-SELECT

**Multi-select:**
[Prompt body]

Options:
- [Option 1]
- [Option 2]
- [Option 3]
- None — [escape option matching the study's framing]

Please select all that apply.

> **USERTESTING QUESTION TYPE: MULTI-SELECT** (NOT Written response).
```

Recap multi-selects (Rule 10) always include a "None — I would still [use] all of them" style escape option, and are never randomized (Rule 9) — item order should match the order participants experienced the tasks.

---

## DRAG-TO-RANK

```
### Question Q[N] — DRAG-TO-RANK

**Drag to rank:**
[Prompt body — state what "top" and "bottom" of the ranking mean, e.g. "most to least concerning"]

Items to rank (display order randomized):
- [Item 1]
- [Item 2]
- [Item 3]

Please drag the items into your preferred order.

> **USERTESTING QUESTION TYPE: DRAG-TO-RANK** (NOT Written response).
```

DRAG-TO-RANK isn't at risk of the Written-Response auto-default bug the way the other three are — but it still gets all four tags (header, block label, close, programming opener). Consistency across every question means the programmer never has to guess a type from context, and it keeps the top-of-doc banner audit (Workflow step 7) mechanical rather than case-by-case.

**Fallback:** if the platform build doesn't support DRAG-TO-RANK for a given question, write the verbal fallback inline per Rule 23 rather than improvising at field time:

```
> **Fallback if DRAG-TO-RANK is unavailable on this build:** convert to VERBAL. Spoken text becomes: "[items], read aloud in whatever order you'd rank them, most to least [concerning/important/etc.], with your reasoning as you go."
```

---

## Quick reference — which close goes with which type

| Type | Close (NOT the type name substituted literally) |
|---|---|
| VERBAL RESPONSE | "Please give a verbal response." |
| SINGLE CHOICE | "Please select one option." |
| MULTI-SELECT | "Please select all that apply." |
| DRAG-TO-RANK | "Please drag the items into your preferred order." |
