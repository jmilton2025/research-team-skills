"""
mod-guide skill — Pass 3 of the styling pipeline.

Re-applies bold to:
  - Table header row (row 0) — all cells
  - Col 1 (label column) of every body row
  - Inline labels (runs ending in ":" at start of paragraph), e.g.
    "Responsible:", "Probe (Echo):", "Watch for:", "Setup:"

Why this exists: the font_and_widths pass sets weightedFontFamily without a
weight key, which preserves bold runs that already existed. But style-gdoc-full
sometimes leaves col 1 / header row in a state where the bold needs to be
re-asserted explicitly with weight=700, and it never bolds the inline labels
at all (those come from the source markdown's `**Bold:**` syntax, which
md2doc renders as separate text runs that can lose their boldness in the
intermediate styling pipeline).

Usage:
    uv run --python 3.12 \\
        --with google-api-python-client --with google-auth \\
        --with google-auth-oauthlib --with google-auth-httplib2 \\
        --with requests --with python-dotenv --with markdown --with pillow \\
        ~/.claude/skills/mod-guide/scripts/rebold_col1.py <DOC_ID>
"""

import sys

sys.path.insert(0, '/Users/jedidamilton/.claude/plugins/cache/instacart/md2doc/893dc15bd620/skills/md2doc/scripts')
import _env  # noqa: F401
from common.drive import get_docs_service

if len(sys.argv) < 2:
    print("Usage: rebold_col1.py <DOC_ID>", file=sys.stderr)
    sys.exit(1)

DOC_ID = sys.argv[1]

docs = get_docs_service()
doc = docs.documents().get(documentId=DOC_ID).execute()
content = doc['body']['content']

requests = []

# ─────────────────────────────────────────
# Pass 1: Bold table header row (row 0) + col 0 of all body rows
# ─────────────────────────────────────────
for el in content:
    if 'table' not in el:
        continue
    table = el['table']
    for row_idx, row in enumerate(table.get('tableRows', [])):
        for col_idx, cell in enumerate(row.get('tableCells', [])):
            should_bold = (row_idx == 0) or (col_idx == 0)
            if not should_bold:
                continue
            for cel in cell['content']:
                if 'paragraph' not in cel:
                    continue
                for tr in cel['paragraph'].get('elements', []):
                    if 'textRun' not in tr:
                        continue
                    s = tr.get('startIndex')
                    e = tr.get('endIndex')
                    if s is None or e is None or e <= s:
                        continue
                    requests.append({
                        'updateTextStyle': {
                            'range': {'startIndex': s, 'endIndex': e},
                            'textStyle': {
                                'bold': True,
                                'weightedFontFamily': {'fontFamily': 'DM Sans', 'weight': 700},
                            },
                            'fields': 'bold,weightedFontFamily',
                        }
                    })

print(f"Pass 1: {len(requests)} bold requests for table headers + col 1")


# ─────────────────────────────────────────
# Pass 2: Re-bold inline labels — runs ending with ":" that
# are short (< 50 chars) and at the start of a paragraph
# This catches "Probe (Echo):", "Watch for:", "Setup:", "Responsible:", etc.
# ─────────────────────────────────────────
def walk_for_inline_bold(c, requests):
    for el in c:
        if 'paragraph' in el:
            elems = el['paragraph'].get('elements', [])
            for tr in elems:
                if 'textRun' not in tr:
                    continue
                t = tr['textRun'].get('content', '')
                if not t.strip():
                    continue
                # First non-empty run: if it ends in ":" and is short, bold it
                if t.rstrip().endswith(':') and len(t) < 50:
                    s = tr.get('startIndex')
                    e = tr.get('endIndex')
                    if s is not None and e is not None and e > s:
                        requests.append({
                            'updateTextStyle': {
                                'range': {'startIndex': s, 'endIndex': e},
                                'textStyle': {
                                    'bold': True,
                                    'weightedFontFamily': {'fontFamily': 'DM Sans', 'weight': 700},
                                },
                                'fields': 'bold,weightedFontFamily',
                            }
                        })
                break  # only check first non-empty run per paragraph
        elif 'table' in el:
            for row in el['table']['tableRows']:
                for cell in row['tableCells']:
                    walk_for_inline_bold(cell['content'], requests)


before = len(requests)
walk_for_inline_bold(content, requests)
print(f"Pass 2: {len(requests) - before} additional inline-label bold requests")


# ─────────────────────────────────────────
# Apply in batches
# ─────────────────────────────────────────
BATCH = 200
for i in range(0, len(requests), BATCH):
    chunk = requests[i:i + BATCH]
    docs.documents().batchUpdate(documentId=DOC_ID, body={'requests': chunk}).execute()
    print(f"  Applied batch: {min(i + BATCH, len(requests))}/{len(requests)}")

print()
print(f"Done. View: https://docs.google.com/document/d/{DOC_ID}/edit")
