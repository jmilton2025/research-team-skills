# Subtotal Audit Script

Full reference for Rule 11: every cart's `data-subtotal` must equal the sum
of its `data-price` line items. Run this after ANY edit that touches a price
or line item — don't rely on eyeballing it.

## Why a script instead of mental math

Mental "does this look right" checks miss transposed digits and rounding
errors, and they don't scale past 2–3 line items. The bundled templates
(`assets/dual-phone-template.html`, `assets/two-cart-template.html`) already
tag every line item and subtotal with `data-price="X.XX"` and
`data-subtotal="X.XX"` attributes specifically so this can be checked
mechanically instead of by hand.

## The script

Save as `audit_subtotals.py` next to the stimuli file and run
`python3 audit_subtotals.py path/to/stimuli.html`. It groups line items into
carts using the same structure the templates already produce — one or more
`data-price` rows followed by a `data-subtotal` row, repeated per phone —
and flags any cart where the sum doesn't match.

```python
#!/usr/bin/env python3
"""Verify every cart's data-subtotal equals the sum of its data-price rows.

Usage: python3 audit_subtotals.py path/to/stimuli.html
"""
import re
import sys

PRICE_RE = re.compile(r'data-price="([\d.]+)"')
SUBTOTAL_RE = re.compile(r'data-subtotal="([\d.]+)"')
# Matches either kind of tag, in document order, so line items are grouped
# correctly with the subtotal that follows them.
TOKEN_RE = re.compile(r'data-price="[\d.]+"|data-subtotal="[\d.]+"')


def audit(html: str):
    carts = []
    current_prices = []
    for token in TOKEN_RE.finditer(html):
        text = token.group(0)
        price_match = PRICE_RE.match(text)
        if price_match:
            current_prices.append(float(price_match.group(1)))
            continue
        subtotal_match = SUBTOTAL_RE.match(text)
        if subtotal_match:
            carts.append((current_prices, float(subtotal_match.group(1))))
            current_prices = []

    if current_prices:
        print(f"WARNING: {len(current_prices)} line item(s) with no matching "
              f"subtotal found after them — check the file structure.")

    if not carts:
        print("No carts found (no data-subtotal attributes in file).")
        return True

    all_pass = True
    for i, (prices, subtotal) in enumerate(carts, start=1):
        computed = round(sum(prices), 2)
        ok = abs(computed - subtotal) < 0.005
        status = "PASS" if ok else "FAIL"
        if not ok:
            all_pass = False
        print(f"Cart {i}: line items = {prices} -> sum = ${computed:.2f} | "
              f"labeled subtotal = ${subtotal:.2f} | {status}")
    return all_pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        html = f.read()
    ok = audit(html)
    sys.exit(0 if ok else 1)
```

## If your file doesn't use `data-price` / `data-subtotal` attributes

The templates set these attributes for exactly this reason — if you're
building a stimulus by hand without starting from a template, add them:

```html
<div class="cart-row"><span>Item name</span><span class="line-item-price" data-price="3.49">$3.49</span></div>
...
<div class="cart-subtotal" data-subtotal="8.67"><span>Subtotal</span><span>$8.67</span></div>
```

The visible `$X.XX` text and the `data-price`/`data-subtotal` value must
always match each other too — the script only checks the data attributes,
so a mismatch between the attribute and the displayed text won't be caught
automatically. Spot-check that by eye once per cart.
