# Design Tokens

Full reference for Rule 21. Copy the whole block into every stimulus HTML's
top-of-file `<style>` — even a build that only needs a subset of these tokens,
so every file in a study (and across studies) stays visually identical.

```css
:root {
  --ic-green: #0AAD0A;            /* Primary CTA, brand accent, success states */
  --label-ink: #2D4A3E;           /* Section banners, headers, primary text */
  --ic-bg: #FFFFFF;               /* Phone body background */
  --row-divider: #E8E8E8;         /* Cart row dividers */
  --meta-muted: #6B7280;          /* Meta labels, secondary text */
  --asked-bg: #F3F4F6;            /* Single-row card asked-pane background (Rule 4) */
  --added-bg: #E6F4EA;            /* Single-row card added-pane background (Rule 4) */
  --star-color: #F5A623;          /* Hero-block star rating (Rule 8) */
  --conditional-bg: #FEF3C7;      /* Conditional-question callout background (Rule 20) */
  --conditional-border: #F59E0B;  /* Conditional-question callout left border (Rule 20) */
}
```

## Where each token is used

| Token | Rule | Applied to |
|---|---|---|
| `--ic-green` | 2, 3, 8 | `.cta-button` background, brand accents |
| `--label-ink` | 14, 15 | Body text color, section banner text, header table |
| `--ic-bg` | 16 | `.phone` background |
| `--row-divider` | 11 | Borders between `.cart-row` items |
| `--meta-muted` | 6, 7 | `.phone-label`, `.hero-meta`, `.pane-item-meta` |
| `--asked-bg` | 4 | `.asked-pane` background on the single-row card |
| `--added-bg` | 4 | `.added-pane` background on the single-row card |
| `--star-color` | 8 | `.hero-stars` on SOURCE screens only (never on cart/result screens — see Rule 8's exception) |
| `--conditional-bg` | 20 | `.conditional-banner` background |
| `--conditional-border` | 20 | `.conditional-banner` left border |

Note the `.internal-ref-banner` (Rule 14) deliberately does **not** use a
token — it's styled as an obviously-not-stimulus dark/monospace treatment
(`#111827` background, `#FBBF24` text in the bundled templates) precisely so
it can never be mistaken for participant-facing chrome. Don't fold it into
the token set or theme it to match the rest of the UI.

## When to extend this set

These 10 tokens cover every pattern named in SKILL.md. If a build genuinely
needs a color beyond this list (e.g., a new badge-confidence tier, a
different signal color):

1. Add it to the `:root` block as a named token — never an inline hex value.
2. Document what it's for in a one-line comment, same style as the table above.
3. Note in the file's build notes (or header overview table) which rule/pattern
   required it, so the next person building a related study knows it exists
   and doesn't reinvent it under a different name.

**Never** introduce ad-hoc hex values inline in a `style=""` attribute or a
one-off CSS rule — if it's worth using once, it's worth naming and keeping
consistent everywhere else it could apply.
