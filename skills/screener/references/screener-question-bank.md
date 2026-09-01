# Screener Question Bank

A generic, reusable bank of screener question **patterns** — not tied to any real product, feature, or company beyond generic placeholders. Use this alongside `../SKILL.md` when drafting a standalone self-serve screener. Every pattern below is qualify-only, quota-only, or explicitly both-capable — check the tag before reusing.

Conventions used throughout (full legend in `SKILL.md` Step 3a): **[SCREEN OUT]** ends the screener · **[EXCLUSIVE]** can't combine with other selections · **[RANDOMIZE]** / **[DO NOT RANDOMIZE]** controls option order.

---

## 1. Hard eligibility gates (qualify)

Put these first — see `SKILL.md` Step 3b for why.

- **Age minimum:** "What is your age?" with the below-minimum band tagged `[SCREEN OUT]` and remaining bands left open for a quota mix.
- **Standard exclusion — employee/competitor/market research:** "Do you or anyone in your household currently work for [Company], a direct competitor, or a market research or user-research firm?" Yes → `[SCREEN OUT]`.
- **Standard exclusion — recent similar-study participation:** "Have you participated in a research study about [topic/category] in the last [3–6 months]?" Yes → `[SCREEN OUT]` (waive only if the study specifically wants repeat participants).
- **Consent / willingness gate:** "This study requires [screen-sharing / recording / completing tasks on your own device]. Are you willing and able to do this?" No → `[SCREEN OUT]`.

## 2. Role / core-behavior gates (qualify)

The single question that decides whether someone can speak to the study topic at all.

- **Decision-maker framing:** "Which of the following best describes your role in [decision domain]?" — only the bolded, genuinely-qualifying option(s) pass; every plausible-sounding but insufficient variant is tagged `[SCREEN OUT]`. Pattern: *"I always/mostly [do the core behavior]"* qualifies; *"I sometimes"* or *"I never"* screens out.
- **Ownership/usage gate:** "Do you currently [own / use / have an active account for] [product category]?" No → `[SCREEN OUT]`.
- **Task-capability gate:** "Have you personally [performed the core task] in the last [X months]?" No → `[SCREEN OUT]` if the study requires firsthand recent experience.

## 3. Recency / frequency-of-use qualifiers (qualify + quota)

Often does double duty: a "never" answer disqualifies, while the remaining bands define a quota split (e.g., light vs. heavy user).

- "In the past [X months], how often have you [core behavior]?" — bands from "more than once a week" down to "never." Tag the "never" band `[SCREEN OUT]` only if recent experience is a hard requirement; otherwise leave it as a quota-defining low-frequency band.
- "When did you last [core behavior]?" — recency bands (this week / this month / 1–3 months / 3+ months / never). Same disqualify-vs-quota decision as above.

## 4. Device / platform checks (qualify, only when study-specific)

Only include when the study evaluates a specific interface or OS.

- "Which of the following do you currently use to [core behavior]? Select all that apply. `[RANDOMIZE]`" — options: [Platform/device A], [Platform/device B], [Platform/device C], None of these `[EXCLUSIVE]` `[SCREEN OUT]` if the study can't run without one of the listed platforms.
- "What type of device would you use to complete this study?" — desktop / laptop / tablet / mobile — screen out any device type the study's prototype or tooling can't support.

## 5. Standard demographic quotas (quota only)

Not disqualifying on their own — used to shape sample mix. Always include "Prefer not to answer" on sensitive demographic items.

- Age band (post-minimum-gate mix)
- Household composition (living alone / with a partner / with children under 18 / multigenerational)
- Gender
- Income band
- Region / urbanicity (e.g., distance to nearest [relevant physical location], or urban/suburban/rural self-identification)

## 6. Competitive & crossover usage checks (quota only, occasionally a soft disqualifier)

- "Which of the following [adjacent products/services], if any, have you used in the past [X months]? Select all that apply. `[DO NOT RANDOMIZE]` if list order aids brand recognition; `None of these` `[EXCLUSIVE]`." Used for quota (competitive-usage mix) rather than disqualifying, unless the study specifically needs single-provider-only respondents.
- "Which of the following subscriptions do you currently pay for? Select all that apply." — quota/segmentation only.

## 7. Occasion / use-case checks (quota, sometimes qualify)

- "In the past [X months], have you used [product/category] for any of the following? Select all that apply. `[RANDOMIZE]`" — list of realistic occasions; `None of these` tagged `[SCREEN OUT]` only if the study requires a specific occasion to have occurred, otherwise left as quota/segmentation signal.
- "Who do you typically [core behavior] for? Select all that apply. `[RANDOMIZE]`" — self, household, others — quota/segmentation, not disqualifying, unless the study is scoped to one specific answer (e.g., self-use only).

## 8. Motivation / decision-factor questions (non-disqualifying)

- "Which of the following played a role in your decision to [core behavior]? Select all that apply." — non-disqualifying; feeds later segmentation/analysis, not eligibility.

## 9. Attribute & preference segmentation (non-disqualifying, feeds personalization)

Generic pattern — swap in whatever attribute dimension is relevant to the study (dietary, accessibility, lifestyle, professional context, etc.). Never disqualifying; used to assign stimuli variants or personalize the study experience.

- "Do you have any [relevant attribute] that affects how you [core behavior]? Select all that apply." — option list + "None of these."
- "Which of the following describe your [lifestyle/preference dimension]? Select all that apply." — option list + "None of the above."
- Follow-up importance rating: "How important is [attribute from above] to your experience with [product]?" — Extremely / Very / Somewhat / Not very / Not at all important.

## 10. Attitude / importance ratings (non-disqualifying)

- Standard 5-point importance scale (see above) — reusable for any attribute.
- Standard 5-point satisfaction or agreement scale, `[DO NOT RANDOMIZE]` since the option order is semantically ordinal.

## 11. Psychographic / attitudinal single-select segments (quota only)

Phrase every option so none reads as the "wrong" or embarrassing answer — this is a segmentation question, not a competence test.

- "Which of the following best describes you? Please select one." — 3-way pattern: *"I actively [engage with the attitudinal dimension] and it strongly motivates my [behavior]"* / *"I [engage] somewhat, but it doesn't fully drive my [behavior]"* / *"I don't [engage] — it doesn't factor into my [behavior] at all."* All three tagged "may select" — no disqualifying option.

## 12. Standard disqualifiers (qualify — reusable defaults)

Include by default; drop only on explicit requester confirmation that it doesn't apply.

- Company or competitor employee (self or household member)
- Market research or user-research professional
- Immediate family of either of the above
- Recent participant in a similar study (recency window depends on study cadence)
- "Professional respondent" red flag: belongs to [5+] paid research panels, if the platform can capture this

## 13. Termination & qualify messages (boilerplate)

- **Termination:** "Thank you for your interest — based on your answers, you don't qualify for this particular study. We appreciate your time."
- **Qualify:** "Thanks! Based on your answers, you qualify for this study. [Next steps — scheduling link, study access link, incentive details.]"

---

## Quota math worked pattern

When quotas are known, state them as a table so the math is checkable at a glance — never leave a quota as a vague "aim for a mix":

| Quota group | Target N | Definition |
|---|---|---|
| [Segment A] | [n] | [defining criterion] |
| [Segment B] | [n] | [defining criterion] |
| [Segment C] | [n] | [defining criterion] |
| **Total** | **[sum]** | Should equal the target sample size from intake |
