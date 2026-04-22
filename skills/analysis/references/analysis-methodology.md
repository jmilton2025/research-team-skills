# Analysis Methodology Reference

Deep methodology reference for the `/analysis` skill. Load this file on demand when executing Step 4 of the skill. Three sections:

1. **Braun & Clarke's 6-phase reflexive thematic analysis** (with worked example)
2. **Tag schema design patterns** (deductive, inductive, hybrid; hierarchy; schema library)
3. **Inter-rater reliability** (Cohen's kappa, when to use, how to compute, how to interpret)

Plus: **General Synthesis ladder of inference** and **Common pitfalls** at the end.

---

## 1. Braun & Clarke's 6-Phase Reflexive Thematic Analysis (2022)

### Key distinction: Reflexive vs Coding Reliability vs Codebook TA

Per Braun & Clarke 2022, there are three "families" of thematic analysis. They are NOT interchangeable — they rest on different epistemological assumptions.

| Variant | Epistemology | Themes are... | Uses IRR? | Best for |
|---------|--------------|---------------|-----------|----------|
| **Reflexive TA** (Braun & Clarke default) | Qualitative, constructionist | Constructed by the analyst from codes via interpretive work | No — IRR is antithetical | In-depth qual, 10-30 interviews, single analyst or small team with shared sensibility |
| **Coding Reliability TA** (Boyatzis, Guest et al.) | Post-positivist | "In" the data; multiple coders should converge on the same themes | Yes — kappa required | Mixed-methods studies, large teams, evaluation research |
| **Codebook TA** (framework analysis, template analysis) | Hybrid | Start with a structured codebook (often deductive), applied systematically | Sometimes | Applied research with pre-defined questions, policy research |

**Default choice for UX research at Instacart:** Reflexive TA. Switch to Coding Reliability only if:
- The study has 3+ analysts
- Stakeholders require statistical defensibility (e.g., medical device research, regulatory)
- The research question requires counting theme prevalence with precision

### The 6 phases

#### Phase 1: Familiarization with the data

**Goal:** Deep immersion. Read transcripts fully, multiple times, before coding anything.

**Concrete steps:**
1. Read each transcript end-to-end without annotating
2. Read again, this time jotting casual notes in a separate familiarization journal (not in the transcript)
3. Note initial analytical ideas, curiosities, contradictions, gut reactions
4. Do this for ALL transcripts before moving to Phase 2

**Common mistake:** Skipping to coding on first read. This anchors you to early data and you miss patterns that only become visible across the full corpus.

**Output:** Familiarization notes per transcript (1 page per transcript is typical).

#### Phase 2: Generating initial codes

**Goal:** Systematically apply concise labels to data segments.

**Concrete steps:**
1. Work through each transcript line-by-line (or segment-by-segment)
2. For each segment expressing a discrete idea, write a code (2-5 words)
3. Codes can be descriptive ("participant describes sticker shock") or interpretive ("price as trust signal")
4. Apply multiple codes to the same segment when relevant
5. Revisit and refine codes as new ones emerge
6. After initial coding, list ALL codes in a master codebook

**Example codes from a pricing study:**
- `visible-price-reaction`
- `hidden-fee-betrayal`
- `value-vs-price-tradeoff`
- `price-as-quality-signal`
- `competitive-price-checking`

**Common mistake:** Codes that are too long (full sentences) or too abstract (entire themes dressed as codes). A code is a handle, not a finding.

**Output:** Full codebook with every code, definition, and 2-3 example excerpts.

#### Phase 3: Generating initial themes

**Goal:** Cluster codes into candidate themes — patterns of shared meaning with a central organizing concept.

**Concrete steps:**
1. Print or export all codes
2. Physically or digitally cluster related codes
3. For each cluster, articulate a **central organizing concept** in one sentence
4. Name the candidate theme with a 2-6 word label that captures the concept
5. Identify sub-themes within larger themes
6. Identify outlier codes that don't fit anywhere — these become either new themes, excluded data, or flagged for Phase 4 review

**Example theme construction:**

Codes to Theme candidate:
- `hidden-fee-betrayal` + `price-transparency-relief` + `trust-broken-by-surprise-charge` + `itemized-receipt-reassurance`
- **Central concept:** "Pricing transparency builds trust; hidden fees feel like a breach of trust, not merely inconvenience"
- **Theme name:** "Transparency as a trust contract"

**Common mistake:** Treating themes as "buckets" or "topic summaries." A bucket theme is "Pricing" — it just names a topic. A fully-realized theme says something: "Pricing transparency builds trust" is a *pattern of shared meaning*.

**Output:** 3-7 candidate themes with central concepts articulated.

#### Phase 4: Reviewing themes

**Goal:** Test candidate themes against data. Are they coherent? Do they tell a story together?

**Two-level review:**

**Level 1 — Review against coded extracts:** For each theme, read every excerpt coded into it. Does the excerpt actually support the theme? If many excerpts don't fit, refine or split the theme.

**Level 2 — Review against the full dataset:** Re-read the full transcripts with themes in mind. Do the themes capture something real and important? Are there themes you missed? Is the thematic map coherent?

**Concrete steps:**
1. For each candidate theme, list all coded excerpts
2. Check internal homogeneity (excerpts within the theme feel related)
3. Check external heterogeneity (themes feel distinct from each other)
4. Merge themes that overlap too much
5. Split themes that are doing too much work
6. Drop themes that don't hold up

**Common mistake:** Staying attached to a theme because you've invested in it. Per Braun & Clarke, "killing your darlings" is a rigor criterion.

**Output:** Refined thematic map with 3-6 themes.

#### Phase 5: Defining and naming themes

**Goal:** For each theme, write a definition and a memorable name.

**Concrete steps for each theme:**
1. Write a 2-4 sentence definition that expresses the central organizing concept
2. Identify the 2-3 best illustrative quotes (ones that express the theme most clearly)
3. Write a theoretical memo: how does this theme relate to existing frameworks, prior research, or domain knowledge?
4. Give the theme a punchy name — ideally a participant phrase or a short metaphor
5. Identify sub-themes if the theme has internal structure

**Good theme names:**
- "Transparency as a trust contract" (metaphor)
- "It just works (until it doesn't)" (participant language)
- "The hidden cost of convenience" (tension)

**Bad theme names:**
- "Pricing" (topic, not pattern)
- "User concerns about fees" (description, not interpretation)
- "Things users said about trust" (summary, not analysis)

**Output:** Final theme definitions, names, illustrative quotes, memos.

#### Phase 6: Writing up

**Goal:** Produce a defensible, readable theme report.

**Concrete steps:**
1. Open with research question + reflexivity statement
2. Present thematic overview (table of themes with central concepts)
3. Deep-dive per theme: definition, quotes, memo, contradictions, sub-themes
4. Close with theme relationships / thematic map
5. Include recommendations grounded in themes
6. Appendix: codebook, method notes, trustworthiness statement, limitations

Per Braun & Clarke 2022, a good theme report does NOT read like a chronological summary of what you did. It reads like an **interpretive argument** — the themes are the claims, the quotes are the evidence.

### Worked example: Pricing transparency study

**Research question:** How do participants experience and interpret pricing transparency in grocery delivery?

**Phase 1 (Familiarization):** 12 transcripts read twice. Notes capture: "everyone mentions fees", "strong affect around surprise charges", "transparency repeatedly framed as trust issue not just convenience".

**Phase 2 (Codes):** 47 initial codes. Examples: `visible-price-reaction`, `hidden-fee-betrayal`, `competitive-price-checking`, `itemized-receipt-relief`, `service-fee-confusion`, `tip-pressure`, `value-vs-price-tradeoff`.

**Phase 3 (Candidate themes):**
1. "Transparency as a trust contract" (12 codes)
2. "The invisible cost of convenience" (8 codes)
3. "Price as quality signal" (6 codes)
4. "Competitive price-checking as self-defense" (5 codes)

**Phase 4 (Review):** Theme 3 "Price as quality signal" had only 4 supporting excerpts across 3 participants — demoted to a sub-theme under "Transparency as a trust contract". Theme 4 refined to "Active price vigilance".

**Phase 5 (Defining):**

- **Theme 1: "Transparency as a trust contract"**
  - Definition: "Pricing transparency is experienced not as a convenience feature but as a moral contract. Hidden fees are interpreted as betrayal, while itemized disclosure builds durable trust — participants describe being willing to pay MORE for transparency."
  - Quotes: *"I'd rather pay $5 more and know what I'm paying for."* — P04
  - Sub-themes: Price as quality signal (2 of 12 participants)

**Phase 6 (Write-up):** Full theme report with 3 themes, 12 quotes, recommendations.

---

## 2. Tag Schema Design

### Three tagging approaches (per Dscout/Nikki Anderson)

| Approach | When | Process | Pros | Cons |
|----------|------|---------|------|------|
| **Deductive** | Schema exists before analysis (e.g., JTBD, pain-point taxonomy, heuristic framework) | Design codebook, apply to data, refine | Fast, consistent, easy to train new coders | Risks missing what data shows; forces data into pre-existing categories |
| **Inductive** | Exploratory research, no prior framework | Read 10-20% of data, draft tags, apply to rest, refine iteratively | Grounded in data; surfaces unexpected patterns | Slower; requires more analyst skill; harder to achieve IRR |
| **Hybrid** | Most common in practice | Start with seed tags (deductive) + allow new tags to emerge (inductive) | Balances structure with discovery | Requires discipline to document tag evolution |

**Recommendation:** Default to hybrid unless there's a compelling reason. Start with 5-10 seed tags based on research question, allow 10-20 more to emerge.

### Tag types: descriptive vs analytical

Per Dscout and Saldana (2016), codes/tags serve different functions at different stages.

**Descriptive tags** stay close to participant language:
- `price-mentioned`
- `feature-recipe-search`
- `task-abandoned`

**Analytical tags** interpret meaning:
- `friction.trust-broken`
- `jtbd.save-time-weeknights`
- `emotion.frustration.high`

**Best practice:** Start descriptive (Phase 1-2), add analytical (Phase 3+). Per Anderson: "You don't want to be too deductive at the beginning and risk misunderstanding what the participant is getting at."

### Tag hierarchy: parent to child

For corpora of 200+ excerpts, flat tag lists break down. Use hierarchical tags separated by dots or slashes.

**Pattern:** `category.subcategory.specific`

**Example schema from a grocery delivery study:**

```
friction/
  friction.pricing/
    friction.pricing.sticker-shock
    friction.pricing.hidden-fees
    friction.pricing.tip-pressure
  friction.search/
    friction.search.no-results
    friction.search.wrong-results
  friction.checkout/
    friction.checkout.payment-declined
    friction.checkout.address-confusion

trust/
  trust.transparency
  trust.brand-familiarity
  trust.social-proof

jtbd/
  jtbd.save-time
  jtbd.household-restock
  jtbd.special-meal
  jtbd.healthy-eating

emotion/
  emotion.delight
  emotion.frustration
  emotion.confusion
  emotion.anxiety
```

**Rules:**
- Max 3 levels of hierarchy (deeper gets unwieldy)
- Every child tag must clearly fit its parent
- Each tag needs its own definition — children are NOT redundant with parents

### Common seed-tag schemas (starter library)

**Global tags (per Nikki Anderson):**
- Goal / Need / Motivation / Task / Pain Point / Tools

**Jobs-to-be-done:**
- `jtbd.functional.*` (the task)
- `jtbd.emotional.*` (how they want to feel)
- `jtbd.social.*` (how they want to be perceived)

**Usability heuristics (Nielsen):**
- `heuristic.visibility-of-system-status`
- `heuristic.match-system-to-real-world`
- `heuristic.user-control-freedom`
- ...(10 total)

**Emotion (simplified):**
- `emotion.delight / positive / neutral / confusion / frustration / anxiety / anger`

**Friction/value (binary frame):**
- `friction.*` (anything participant described negatively)
- `value.*` (anything participant described as beneficial)

### Codebook structure

Every tag in a codebook has 5 fields:

| Field | Purpose | Example |
|-------|---------|---------|
| **Name** | Unique identifier | `friction.pricing.sticker-shock` |
| **Definition** | What this tag captures (1-2 sentences) | "Strong negative reaction expressed at the moment of seeing a price, before considering value received." |
| **Inclusion criteria** | When to apply the tag | "Apply when participant expresses surprise, shock, or immediate negative affect at price display." |
| **Exclusion criteria** | When NOT to apply | "Do not apply to general dissatisfaction with price once value is considered — use `friction.pricing.value-gap` instead." |
| **Example quote** | Canonical example | *"I saw the total and just closed the tab."* — P07 |

---

## 3. Inter-Rater Reliability (IRR)

### When IRR matters

IRR is only relevant for **Coding Reliability TA** or **multi-coder Tagging** projects. Per Braun & Clarke 2022, IRR is **antithetical to reflexive TA** — if you're doing reflexive TA, do not compute IRR.

Compute IRR when:
- 2+ analysts are tagging the same data
- Stakeholders require statistical defensibility
- The output will be used for quantitative comparison (e.g., "40% of users expressed X")

### Cohen's kappa

Cohen's kappa measures inter-rater agreement, correcting for agreement by chance.

**Formula:**

```
kappa = (p_o - p_e) / (1 - p_e)

where:
  p_o = observed agreement (proportion of items where both raters agree)
  p_e = expected agreement by chance
```

**Computing p_e:** For binary tag (present/absent):
```
p_e = (P(rater1=1) * P(rater2=1)) + (P(rater1=0) * P(rater2=0))
```

### Interpretation (Landis & Koch, 1977)

| kappa value | Agreement |
|---------|-----------|
| < 0.00 | Poor (worse than chance) |
| 0.00 - 0.20 | Slight |
| 0.21 - 0.40 | Fair |
| 0.41 - 0.60 | Moderate |
| 0.61 - 0.80 | **Substantial** — commonly treated as acceptable threshold |
| 0.81 - 1.00 | Almost perfect |

**Target for applied research:** kappa >= 0.70.

### Practical IRR workflow

1. **Pilot phase:** Two coders independently tag 10% of the data
2. **Compute kappa** per tag and overall
3. **Discuss disagreements:** Where do coders differ? Refine tag definitions (usually inclusion/exclusion criteria are too vague)
4. **Second pilot:** Re-tag a fresh 10% with refined codebook. Recompute kappa.
5. **Proceed** when kappa >= 0.70 per tag
6. **Spot-check** throughout: randomly double-code 5% of ongoing work to detect drift

### Lightweight alternative: % agreement

For smaller studies or when kappa is overkill, report **% agreement** on a double-coded sample.

- Target: >= 80% agreement
- Not as rigorous as kappa (doesn't correct for chance), but acceptable for applied UXR

### Common IRR mistakes

1. **Computing overall kappa without per-tag kappa** — masks tags where coders disagree severely
2. **Double-coding only easy data** — sample should be representative
3. **Reconciling disagreements by averaging** — instead, discuss and refine the tag
4. **Treating kappa as a one-time hurdle** — drift happens; spot-check continuously

---

## 4. General Synthesis: Ladder of Inference

For **Mode A (General Affinity Synthesis)**, use the synthesis ladder (adapted from Sharon's *Validating Product Ideas* and Argyris' ladder of inference).

Each step UP the ladder increases abstraction and interpretation. Each step must be grounded in the one below.

| Step | Definition | Example |
|------|------------|---------|
| **Raw data** | Verbatim quote or observed behavior | *"I saw the $27 total and just closed the tab."* — P07 |
| **Observation** | Factual summary of what was heard/seen, close to participant language | P07 abandoned checkout when seeing higher-than-expected total |
| **Pattern** | Observation repeated across participants | 8 of 14 participants (57%) abandoned at least one session citing total cost surprise |
| **Insight** | Interpretive claim about what the pattern MEANS | Sticker shock at checkout reflects a breakdown in trust — participants feel deceived rather than inconvenienced |
| **Recommendation** | Actionable ask grounded in insight | Show estimated total (including fees + tip range) on cart screen, BEFORE checkout. Owner: Checkout PM. Target: Q3. Measure: cart abandonment rate |

**Rule:** Never skip a rung. A claim that leaps from raw data to recommendation is ungrounded and stakeholders will (correctly) push back.

### Common ladder mistakes

1. **Observation masquerading as insight.** "Participants talked about pricing." — That's an observation of the topic, not an insight. Insight requires interpretation: *why* it matters.
2. **Recommendation without insight.** "We should add a cart subtotal." — Why? Because users want it? (That's weak.) Because hidden fees feel like betrayal? (That's strong.)
3. **Insight without pattern.** "Sticker shock breaks trust." — Based on what? One participant? Eight? Report the pattern.

---

## 5. Common Pitfalls (all modes)

| Pitfall | Why it's a problem | Fix |
|---------|-------------------|-----|
| **Themes as buckets / topic summaries** (Thematic) | Per Braun & Clarke, #1 pitfall in reflexive TA. "Pricing" is a topic, not a pattern of shared meaning. | Every theme must have a **central organizing concept** expressible in one sentence. If you can't write that sentence, you have a topic, not a theme. |
| **"Themes emerged from the data"** (Thematic) | Per Braun & Clarke 2022, this language hides the analyst's interpretive work and is epistemologically incoherent in reflexive TA. | Use active, reflexive language: "I developed...", "I constructed...", "I generated from codes X, Y, Z..." |
| **Quote cherry-picking** | Confirmation bias. Selecting only quotes that support your theme while ignoring disconfirming evidence. | Actively seek quotes that complicate or contradict each theme. Report them under "Contradictions / boundary cases." |
| **Prevalence inflation** | "Most participants..." when actually 6 of 14. | Always report exact numbers: "6 of 14 (43%)". Use ~1/3 as minimum pattern threshold per Anderson. |
| **Tag proliferation** (Tagging) | 150 tags, most used 1-2 times. Makes analysis impossible. | Cap at 40 tags. Merge rare tags. Use hierarchy for granularity. |
| **Codebook without exclusion criteria** (Tagging) | Coders disagree because tags are ambiguous. | Every tag needs explicit inclusion AND exclusion criteria. If you can't write them, the tag is too vague. |
| **Skipping familiarization** (all) | Jumping to coding on first read anchors to early data. Misses cross-corpus patterns. | Read everything twice before coding anything. Take familiarization notes separately. |
| **Collapsing observation to recommendation** (General) | "Users want cheaper prices — we should lower prices." Skips the insight rung. | Climb the ladder: raw data, observation, pattern, insight, recommendation. |
| **Treating IRR as optional in multi-coder work** (Tagging) | Stakeholders can't trust prevalence figures without reliability evidence. | Compute kappa on >=10% double-coded sample. Target kappa >= 0.70. |
| **Applying IRR to reflexive TA** (Thematic) | Per Braun & Clarke, antithetical — reflexive TA assumes themes are constructed, not found. | Don't compute IRR in reflexive TA. If IRR is required, switch to coding reliability TA instead. |

---

## 6. Quick Reference: Which methodology when?

```
Research question type                  Recommended mode

"What did we hear?" (briefing)          General Affinity Synthesis
"What patterns of meaning exist?"       Thematic Analysis (reflexive)
"How prevalent is X across corpus?"     Tagging (+ IRR if multi-coder)
"What does the data SAY we missed?"     Inductive Thematic or Inductive Tagging
"Does our framework hold up in data?"   Deductive Tagging or Deductive Thematic

Sample size                             Recommended mode

5-10 sessions                           General Affinity Synthesis
10-30 interviews (deep)                 Thematic Analysis
30+ transcripts OR 200+ survey opens    Tagging
50+ structured rows                     /batch-analysis (different skill)

Timeline                                Recommended mode

<3 days                                 General Affinity Synthesis
1-2 weeks                               Thematic or Tagging
Multi-week, publishable                 Thematic (reflexive, rigorous)
```
