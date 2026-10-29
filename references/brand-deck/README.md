# Instacart Brand Deck — final deliverable for `/analysis` and `/report`

The finished deliverable for `/analysis` and `/report` is a **Google Slides deck built from Instacart's official brand template** ("Oct 2026 Template", 16:9). The template link is in [`slide-map.json`](slide-map.json) (`url`). It's access-controlled, so researchers outside the template's sharing need access from the team. `slide-map.json` lists the template slides used for a research readout and the element IDs to fill on each.

Markdown is the working draft. The deck is built only from approved content, after the skill's QA gates and its review status are done.

## The template's rules

- **Never edit the template.** Always work on a Drive copy in the researcher's confirmed folder.
- **Slide 1 is a "Still cooking" work-in-progress banner.** Delete it from every copy.
- **There are no layouts or placeholders to fill.** Every text element is a plain text box, so duplicate a template slide and fill its elements by ID.
- **Keep the brand look by keeping the template's own styles.** Replace text with `deleteText` plus `insertText`, so the inserted text inherits the existing run's font, size and color, and keep the paragraph count of multi-line cards (label / value / body). Don't set fonts or colors by hand, except for status colors (below).
- **Use the template's palette** (slide 108; in `slide-map.json` under `palette`): Kale `#003D29`, Cashew 10 `#FAF1E5` backgrounds, Matcha `#85CC3E` for good, amber about `#FFBB1A` for at-risk, and Carrot `#FF7009` for bad.
- **Long titles run at most 2–3 lines.** On metric slides, the headline sums up the key numbers.
- **The logo and footer** (CONFIDENTIAL plus the page number) come from the master. Leave the empty page-number text box alone.
- **Fix known template slips when reusing a slide.** Slide 21 has leftover sample content. Slides 98–99 have the typo "Q4 ‘256".

## Readout slide map

| Readout section | Template slide (`readout_mapping` key) | Used by |
|---|---|---|
| Title | 8 (`title`) | both |
| Bottom line / BLUF | 22 (`bluf_exec_summary`); 85 for three numbered takeaways | report; analysis for n≥5 |
| Agenda | 19 (`agenda`) | optional, for decks over about 10 slides |
| Method & sample | 44 (`method_and_sample`) | both |
| Research questions answered | 63 (`research_questions_answered`); 62 for 2 questions, 64 for 4 | both, when the questions are known |
| Section divider | 27 (`section_divider`) | optional, between themes |
| Finding: claim headline + evidence | 37 (`finding`); 77 when the evidence is a screenshot; 39 for a long evidence list | both, one per finding |
| Quote highlight | 22 (`quote_highlight`) | optional |
| Task success & severity | 103 (`task_success_severity_table`); 102 for the simpler table | usability studies |
| Insights → recommendations | 70 (`recommendations_table`); 71 for 4, 69 for 2 | report; analysis for multi-session work only |
| Next steps | 102 (`next_steps`) | both; for analysis n=1, research next steps only |
| Appendix | 28 divider, then 35 text, 97 data table, 94 chart (`appendix`) | as needed |
| Closing | 105 | both |

Skill-specific rules decide what goes on a slide. For example, `/analysis` n=1 and pilot-signal decks never get a recommendations slide or P0/P1/P2 priorities, and `/report`'s claim-heading, confidence-wording and count-plus-percentage rules apply to slide headlines too.

## Build steps

1. **Confirm the destination** (the exact Drive folder and audience) under the skill's own destination gate. A test or mock run gets no Drive artifact unless the tester asks for one.
2. **Copy the template** into that folder with a Drive copy tool (for example Google Drive `copy_file` or Google Workspace `copy_drive_file`). Name the copy `[Study title] — Research Readout` (or `— Analysis`). Record the new presentation ID. If the copy fails because the researcher can't open the template, stop and say so; don't rebuild the brand by hand.
3. **Plan the slide list** from the approved content: one row per slide, giving its template slide, a new slide ID, and the text for each element ID in `slide-map.json`.
4. **Build in one `batchUpdate` per stage**, with the Slides tools available (for example Google Workspace `batch_update_presentation`; never the whole-deck `apiGetPresentation` read, which times out on these decks):
   - `duplicateObject` each template slide, passing `objectIds` so that every new element ID is known ahead of time;
   - `deleteText` (type ALL) then `insertText` on each filled element; table cells use `cellLocation`, and `deleteTableRow` drops unused rows;
   - delete elements a slide doesn't need (an unused partner name or an empty pill);
   - `updateSlidesPosition` into readout order;
   - then delete slide 1 and **every original template slide**, so only the duplicates remain.
5. **Test labels.** On a test run, the title slide's eyebrow reads `⚠️ TEST RUN` or `⚠️ TEST ARTIFACT` (see `../output-status-and-labeling-conventions.md`), and the closing slide repeats it.

## Verify before returning the link

1. **Read every slide back** with a per-slide read (for example Google Workspace `get_page`). Confirm each filled element holds the approved text, and that no template filler remains: "00X", "Subtitle option here", "Optional label", "Name", "Month DD, YYYY", or sample names.
2. **Look at every slide**, via a thumbnail per slide (for example `get_page_thumbnail`) or a Drive PDF export rendered page by page. Check for overflowing or clipped text, a title over 3 lines, empty cards, and leftover template slides.
3. **Fix and re-check**, for at most three rounds. If the deck still fails, return it as blocked with what remains, not as finished.
4. **Return** the deck link, the slide count, and the skill's status line (content checked, slides rendered and checked, plus the review status).

## If Slides tools aren't available

Return the approved Markdown and say exactly what's blocked: *"Blocked — the brand deck wasn't created: [missing tool or access]."* If the Google Slides connector needs sign-in, name it and point to https://claude.ai/customize/connectors. Never return a plain, unbranded deck as the finished deliverable.
