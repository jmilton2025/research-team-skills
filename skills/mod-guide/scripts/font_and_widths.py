"""
mod-guide skill — Pass 2 of the styling pipeline.

Layers DM Sans 10pt + DM Serif Display headers + narrow/wide column widths
on top of style-gdoc-full.py's color and table styling.

Critically: NO foregroundColor changes — let style-gdoc-full's dark-green
Jedi's Template colors win.

Usage:
    uv run --python 3.12 \\
        --with google-api-python-client --with google-auth \\
        --with google-auth-oauthlib --with google-auth-httplib2 \\
        --with requests --with python-dotenv --with markdown --with pillow \\
        ~/.claude/skills/mod-guide/scripts/font_and_widths.py <DOC_ID>
"""

import sys

sys.path.insert(0, '/Users/jedidamilton/.claude/plugins/cache/instacart/md2doc/893dc15bd620/skills/md2doc/scripts')
import _env  # noqa: F401
from common.drive import get_docs_service

if len(sys.argv) < 2:
    print("Usage: font_and_widths.py <DOC_ID>", file=sys.stderr)
    sys.exit(1)

DOC_ID = sys.argv[1]

# Col widths in points (72pt = 1 inch)
COL1_WIDTH_PT = 115  # ~1.6 inches — narrow label column
COL2_WIDTH_PT = 350  # ~4.86 inches — wide content column

docs = get_docs_service()


def font_request(start, end, font, size):
    """Set font + size, preserve color/bold/everything else.

    Critical: do NOT pass a `weight` key inside weightedFontFamily — that
    silently overrides any pre-existing bold runs. Omitting weight preserves
    whatever bold the previous styling pass set.
    """
    return {
        'updateTextStyle': {
            'range': {'startIndex': start, 'endIndex': end},
            'textStyle': {
                'weightedFontFamily': {'fontFamily': font},
                'fontSize': {'magnitude': size, 'unit': 'PT'},
            },
            'fields': 'weightedFontFamily,fontSize',
        }
    }


def font_for_paragraph(nst):
    """(font, size) — no color, let style-gdoc-full's colors win."""
    if nst == 'TITLE':
        return 'DM Serif Display', 26
    elif nst == 'SUBTITLE':
        return 'DM Serif Display', 16
    elif nst == 'HEADING_1':
        return 'DM Serif Display', 20
    elif nst in ('HEADING_2', 'HEADING_3'):
        return 'DM Serif Display', 16
    elif nst == 'HEADING_4':
        return 'DM Serif Display', 14
    else:
        return 'DM Sans', 10


# ─────────────────────────────────────────
# STEP 1: Update NORMAL_TEXT namedStyle baseline
# ─────────────────────────────────────────
print("Step 1: NORMAL_TEXT namedStyle → DM Sans 10pt")
docs.documents().batchUpdate(
    documentId=DOC_ID,
    body={'requests': [{
        'updateTextStyle': {
            'range': {'startIndex': 1, 'endIndex': 2},
            'textStyle': {
                'weightedFontFamily': {'fontFamily': 'DM Sans'},
                'fontSize': {'magnitude': 10, 'unit': 'PT'},
            },
            'fields': 'weightedFontFamily,fontSize',
        }
    }]},
).execute()


# ─────────────────────────────────────────
# STEP 2: Sweep fonts on every text run
# ─────────────────────────────────────────
print("Step 2: Font sweep (preserves colors/bold from style-gdoc-full)")
doc = docs.documents().get(documentId=DOC_ID).execute()
content = doc['body']['content']
sweep = []


def walk(content):
    for el in content:
        if 'paragraph' in el:
            nst = el['paragraph'].get('paragraphStyle', {}).get('namedStyleType', 'NORMAL_TEXT')
            font, size = font_for_paragraph(nst)
            for tr in el['paragraph'].get('elements', []):
                if 'textRun' not in tr:
                    continue
                s = tr.get('startIndex')
                e = tr.get('endIndex')
                if s is None or e is None or e <= s:
                    continue
                sweep.append(font_request(s, e, font, size))
        elif 'table' in el:
            for row in el['table']['tableRows']:
                for cell in row['tableCells']:
                    walk(cell['content'])


walk(content)
print(f"  Sweep requests: {len(sweep)}")

BATCH = 200
for i in range(0, len(sweep), BATCH):
    chunk = sweep[i:i + BATCH]
    docs.documents().batchUpdate(documentId=DOC_ID, body={'requests': chunk}).execute()
    print(f"  Applied {min(i + BATCH, len(sweep))}/{len(sweep)}")


# ─────────────────────────────────────────
# STEP 3: Override col widths — narrow col 1, wide col 2
# ─────────────────────────────────────────
print(f"\nStep 3: Column widths → col 1 = {COL1_WIDTH_PT}pt, col 2 = {COL2_WIDTH_PT}pt")
doc = docs.documents().get(documentId=DOC_ID).execute()
content = doc['body']['content']
width_reqs = []

for el in content:
    if 'table' not in el:
        continue
    table_start = el.get('startIndex')
    if table_start is None:
        continue
    num_cols = el['table'].get('columns', 2)
    if num_cols == 2:
        width_reqs.append({
            'updateTableColumnProperties': {
                'tableStartLocation': {'index': table_start},
                'columnIndices': [0],
                'tableColumnProperties': {
                    'widthType': 'FIXED_WIDTH',
                    'width': {'magnitude': COL1_WIDTH_PT, 'unit': 'PT'},
                },
                'fields': 'widthType,width',
            }
        })
        width_reqs.append({
            'updateTableColumnProperties': {
                'tableStartLocation': {'index': table_start},
                'columnIndices': [1],
                'tableColumnProperties': {
                    'widthType': 'FIXED_WIDTH',
                    'width': {'magnitude': COL2_WIDTH_PT, 'unit': 'PT'},
                },
                'fields': 'widthType,width',
            }
        })

print(f"  Width requests: {len(width_reqs)}")
if width_reqs:
    docs.documents().batchUpdate(documentId=DOC_ID, body={'requests': width_reqs}).execute()


print()
print("=" * 60)
print(f"Done. View: https://docs.google.com/document/d/{DOC_ID}/edit")
