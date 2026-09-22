# Action Ladder Library

Pre-written ladders for common decision shapes. All are ordinal (mildest → most severe) — never randomize (SKILL.md Rule 6). Pick the shortest ladder that captures the decision space; don't add a 4th rung "just in case" if 3 already cover it.

---

## 4-option cart-level ladder (default for cart-action questions)

Use when: the participant is reacting to a whole cart and "buying elsewhere for the missing/wrong item" is a real, distinct option from editing the cart.

1. Add as-is
2. Edit the cart first (swap, remove, or add items)
3. Buy this cart now and get the missing item(s) elsewhere
4. Skip this and pick a different [recipe/option]

```
Options (do not randomize — action ladder):
1. Add as-is
2. Edit the cart first (swap, remove, or add items)
3. Buy this cart now and get the missing item(s) elsewhere
4. I would no longer continue with this and pick a different [recipe/option]
```

---

## 3-option cart-edit ladder (when "buy elsewhere" isn't relevant)

Use when: nothing is missing — the cart is complete but something about it (a substitution, a price, a signal) needs a decision that doesn't split into a "go elsewhere for one item" branch.

1. Add the cart as-is
2. Edit the cart first
3. I would no longer [continue with this]

```
Options (do not randomize — action ladder):
1. Add the cart as-is
2. Edit the cart first
3. I would no longer continue with this order
```

---

## 3-option single-row substitution ladder (Accept / Modify / Skip)

Use when: the decision is about ONE item, not the whole cart. This is an item-level ladder, not a layout — it applies whether that item is shown in isolation (a single-row card, asked → delivered) or as one flagged/badged item inside an otherwise-full cart (e.g., a confidence-badge study where the rest of the cart is just context). The stimulus layout is a [[usertesting-html]] call; this wording doesn't change either way.

1. Accept — "That works for me"
2. Modify — "I'd swap it myself" / "I'd swap for a smaller size"
3. Skip — "I'd skip it"

```
Options (do not randomize — action ladder):
1. Accept — "That works for me"
2. Modify — "I'd swap it myself"
3. Skip — "I'd skip that item"
```

**Adapting to a whole-cart-with-one-flagged-item stimulus:** keep the three options item-scoped ("that item," not "this cart") even though the participant is looking at a full cart — the ladder measures what they'd do about the ONE item, not the order as a whole. If you also need a cart-level decision in the same task, that's a second question using one of the two ladders above, not a 4th rung bolted onto this one.

---

## Choosing between ladders — quick decision guide

| Situation | Ladder |
|---|---|
| Whole cart, something's missing, "buy elsewhere" is plausible | 4-option cart-level |
| Whole cart, nothing missing, but something needs a decision | 3-option cart-edit |
| One item's fate (isolated card OR one flagged item in a full cart) | 3-option substitution (Accept/Modify/Skip) |

If none of these three fit, that's a real gap — flag it (per the "flag every mismatch" standing preference) and propose 2–3 candidate wordings rather than silently inventing a 4th ladder shape.
