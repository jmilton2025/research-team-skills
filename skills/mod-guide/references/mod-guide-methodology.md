# Moderation Guide — Methodology Reference

Deep reference for the `/mod-guide` skill. Load on demand when the researcher asks about a specific probe type, bias, study-type nuance, or wants example scripts beyond the main template.

Grounded in: Portigal (*Interviewing Users*, 2nd ed.), Young (*Listening Deeply* / mental models), Hall (*Just Enough Research*), Sharon (*Validating Product Ideas*), NN/g (Rosala, Pernice, Moran, Fessenden), Anderson (User Research Academy), dscout *People Nerds*.

---

## 1. Named Probing Taxonomy

Use these names **in-line** in generated guides so moderators build muscle memory. Each probe has a one-line rule, an example, and a source.

| # | Probe | Rule | Example phrase | Source |
|---|-------|------|----------------|--------|
| 1 | **Echo** | Repeat the participant's last phrase with a slight interrogatory tone. Lets them expand without leading. | Participant: "The table was weird." → Moderator: "Table was weird?" | Fessenden — NN/g *Talking to Users* |
| 2 | **Silence** | Count 5-10 seconds after an answer. Silence is a tool; participants fill the void with richer content. | (Pause. Count to 10 before re-prompting.) | Portigal; Hall; Anderson |
| 3 | **Tell-Me-More** | The evergreen open probe. Works anywhere. | "Tell me more about that." | Anderson (TEDW); NN/g |
| 4 | **Laddering / Why-chain** | Climb from behavior → reason → value. Stop when they hit a terminal value or say "I just do." | "Why was that important to you?" / "In what sense?" / "How so?" | Portigal; dscout |
| 5 | **Critical Incident Technique (CIT)** | Replace typical-behavior questions with specific-incident prompts. Closes recall and say-do gaps. | "Tell me about the last time you [behavior]." / "Tell me about a time it went well… and a time it didn't." | Flanagan (1954) via NN/g |
| 6 | **Contrast** | Compare two experiences to surface implicit criteria. | "How did that compare to [prior experience]?" | Portigal |
| 7 | **Specificity** | When a vague or emotionally loaded word appears (frustrating, confusing, easy, annoying), unpack it immediately. | "What do you mean by 'frustrating'?" / "Can you give me an example of that?" | NN/g; dscout |
| 8 | **Hypothetical / Projective** | Use **sparingly and late**. Good for dreams / 5-year-out / magic-wand; bad for predicting actual future behavior. | "If we came back in 5 years, what would be different?" / "If you had a magic wand…" | Portigal; avoid per NN/g 6 Mistakes |
| 9 | **Boomerang** | Return the participant's question to them. Common in usability tests when they ask for help. | "What do you think?" / "What would you normally do?" | Fessenden — NN/g |
| 10 | **Columbo** | Trail off mid-sentence; let the participant complete the thought. Acts like an investigator, not an expert. | "So you clicked on that because…" (trail off) | Fessenden — NN/g |
| 11 | **Mirroring** | Match tone and energy. Build comfort. | (Non-verbal: lean in, nod, match pace.) | dscout *17 Pro Tips* |
| 12 | **Participatory / Artifact** | Ask them to sketch, show, or walk through a real artifact. Grounds abstract talk in evidence. | "Can you walk me through your last order on your phone right now?" / "Can you draw how you think about this?" | Portigal |

**Key usage rule:** name the probe in the `[Moderator Note]` of the guide so the moderator sees *why* each follow-up is suggested. Example: `• Probe (Echo): "The list was overwhelming?"` Not just a probe — a labeled technique.

---

## 2. Say-Do Gap Module — Full Playbook

Use when stated behavior likely diverges from actual behavior. NN/g: *"Interviews do not produce reliable data about user behavior."*

### 2a. Diagnostic — when is say-do risk Medium/High?

| Signal | Risk |
|--------|------|
| Study asks about stated preferences, intent, or willingness to pay | **High** |
| Study asks about frequency of everyday behaviors (cooking, shopping, reading labels) | **High** |
| Study asks about sensitive identity-adjacent behavior (dietary, health, parenting) | **High** — compounded by social desirability |
| Study asks what participants *would* do with a new feature | **High** |
| Study observes actual behavior with planned follow-up | **Low** |
| Study is a usability test (watching, not asking) | **Low** |

### 2b. Probes to include when risk is Medium/High

1. **Replace typical with specific.** Instead of "How often do you cook at home?" → "Tell me about the last time you cooked dinner. What about the time before that?"
2. **Ground in artifact.** "Can you open your Instacart app and walk me through your last order?" "Can you show me what's in your fridge right now?"
3. **Diary / photo pre-work.** If you can prep before the session: "Before we talk, send me 3 photos of meals you cooked this week."
4. **Probe the gap directly (non-accusatory).** When stated and shown diverge: "Earlier you mentioned X — I'm curious how that connected to [what I just saw]." Never: "But you said…"
5. **Ask about frequency via recent window.** "In the last 7 days, how many times did you…" beats "How often…"
6. **Avoid future-prediction questions entirely.** "Would you use this?" / "Would you pay for X?" — NN/g: *"people are bad at predicting their future behavior."*

### 2c. Social-desirability counter-moves (Indi Young, Portigal)

- **Normalize the undesirable answer.** "Lots of people I talk to skip this step — does that happen for you?"
- **Decouple from identity.** "I'm not evaluating you — I'm learning about the product."
- **Use third-person framing.** "What do you think other people in your situation do?" (Recognizes that people will project their own behavior onto "others" more honestly than onto themselves.)
- **Focus on the problem space, not the solution space.** Indi's *listening session* stays in purpose/cognition and avoids priming with specific products until very late.

---

## 3. Interview Structure by Study Type

### 3a. In-Depth Interview (IDI) — 60 min default

| Section | Time | Purpose |
|---------|------|---------|
| Consent + Recording | 2 min | Legal + set tone |
| Warm-Up | 5-7 min | Rapport, calibrate vocabulary |
| Core Discussion (3-4 topics) | 40-45 min | Main data |
| Wrap-Up / Debrief | 5-7 min | Catch-all, surprises, magic wand |

Funnel each topic: broad → specific → closed (NN/g Rosala).

### 3b. Usability Test (Think-Aloud) — 60 min default

| Section | Time | Purpose |
|---------|------|---------|
| Consent + Recording | 2 min | — |
| Warm-Up + Think-Aloud Intro | 5-7 min | Rapport + protocol training |
| Task 1 | 8-12 min | Observe |
| Task 2 | 8-12 min | Observe |
| Task 3 | 8-12 min | Observe |
| Post-task SEQ / SUS (optional) | 2-5 min | Quant |
| Wrap-Up | 8-10 min | Subjective reactions, what changed |

**Think-aloud intro script (Kate Moran / NN/g):**
> "As you use this, please think out loud — say whatever comes to mind. What are you looking for, what do you expect, what surprises or confuses you. There's no right way to do this; just narrate your thinking. If you go quiet for a bit, I may gently remind you to keep talking."

**Demo it** with a short example before Task 1 (NN/g: show a video or demonstrate).

**When they go silent:** after ~10 seconds, prompt with "What are you thinking?" or "What are you looking for?" — never "Do you see X?" (leading).

### 3c. Concept Test — 45 min default

| Section | Time | Purpose |
|---------|------|---------|
| Consent | 2 min | — |
| Warm-Up | 5 min | Baseline context |
| Stimulus 1 presentation + reactions | 10 min | First impressions + desirability |
| Stimulus 2 presentation + reactions | 10 min | Same |
| Comparison | 10 min | Trade-offs, preference |
| Wrap-Up | 5-8 min | — |

Use the **5-second rule** for first impressions: show stimulus for 5 seconds, hide, ask "what do you remember, what did it make you feel?"

### 3d. Diary Study Check-in — 30-45 min

| Section | Time | Purpose |
|---------|------|---------|
| Consent (only on session 1) | 2 min | — |
| Warm-Up / How did the week go | 3-5 min | Reconnect |
| Entry Review (pick 3-5 entries) | 20-30 min | Probe specific entries — "Tell me what was going on when you wrote this one" |
| Wrap-Up + Next Week Prompts | 5-7 min | Instructions for next phase |

Diary studies close the say-do gap structurally — you probe *recorded* behavior, not memory.

### 3e. Focus Group — 60-90 min

| Section | Time | Purpose |
|---------|------|---------|
| Consent + Ground Rules | 5 min | "One voice at a time, no wrong answers, disagreement welcome" |
| Intros around the table | 5-10 min | — |
| Divergent Discussion | 30-40 min | Broad topics, go-arounds |
| Convergent Activity | 15-20 min | Sort, rank, or prioritize together |
| Wrap-Up | 5-10 min | — |

**Manage dominant voices.** "Let's hear from someone who hasn't spoken yet." Call on quieter participants by name.

---

## 4. Full Bias-Mitigation Checklist

### 4a. In the guide (prevent upstream)
- [ ] **Open-ended phrasing** — "Tell me about…" not "Do you…?" (Hall, NN/g)
- [ ] **No compound questions** — one question at a time (NN/g 6 Mistakes)
- [ ] **No clarifier with interpretation** — "Tell me why you chose that" not "Was it because it was faster?" (NN/g)
- [ ] **Specific incidents, not typical patterns** (NN/g CIT)
- [ ] **No future-prediction hypotheticals** (NN/g; Sharon)
- [ ] **Vague study purpose in intro** — don't prime ("a chat about cooking" not "a chat about meal-kit preferences") (NN/g Rosala)

### 4b. In the room (prevent in-session)
- [ ] **Brain-dump hypotheses before starting** — so you're not hunting for confirmation (Portigal)
- [ ] **Moderator talk ≤ 20%** (NN/g)
- [ ] **Neutral body language** — no head-shakes, no "great!", no frowns (NN/g; Portigal)
- [ ] **Don't finish their sentences** — Columbo/Silence instead (Fessenden)
- [ ] **Normalize negative answers** — "I didn't design this, you won't hurt my feelings" (Portigal)
- [ ] **Third-person framing for sensitive topics** (Indi Young)
- [ ] **Max 2-3 silent observers**, out of frame (NN/g Rosala)
- [ ] **Avoid the word "interview"** — call it a "chat" (NN/g)

### 4c. Specific biases to name and counter

| Bias | What it looks like | Counter |
|------|--------------------|--------|
| **Social desirability** | "I always read ingredient labels" (when they don't) | Normalize undesirable answer; third-person framing; ground in artifact |
| **Acquiescence (yea-saying)** | "Yes" to every question regardless | Use open questions, avoid yes/no framing |
| **Recall bias** | Participants reconstruct rather than remember | Anchor to specific recent incidents (CIT), "in the last 7 days…" |
| **Query effect** (NN/g) | Preferences form *because* you asked | Don't ask about preferences for things they haven't used; observe instead |
| **Confirmation (moderator)** | Moderator hears what confirms hypothesis | Pre-session hypothesis brain-dump; have a note-taker; review tape |
| **Hawthorne / observer effect** | Behavior changes because observed | Small footprint; observers silent + out of frame |
| **Leading-question bias** | "Was it because X?" shapes answer | Neutral clarifiers: "Tell me why…" |
| **Sunk-cost rationalization** | Participants justify past choices | Ask about the choice *situation*, not whether it was "right" |

---

## 5. Moderator Do's and Don'ts (Quick Reference)

### Do
- ✅ **Shut up and listen.** Hall: "Conducting a good interview is actually about shutting up."
- ✅ **Use silence as a probe.** Count to 10.
- ✅ **Echo their words**, don't paraphrase into your framing.
- ✅ **Anchor to specific recent events.** "Tell me about the last time…"
- ✅ **Watch body language** — hesitation, squinting, emotional shifts — and probe them: "I noticed you paused — what was going through your mind?"
- ✅ **Write top 3 impressions within 5 minutes of session end** (memory decays fast).

### Don't
- ❌ **Don't use "interview"** — call it a "chat" (NN/g).
- ❌ **Don't answer their questions about the product.** Boomerang: "What would you normally do?"
- ❌ **Don't say "great!"** or react approvingly — you're rewarding the answer.
- ❌ **Don't rescue silence.** That's where the richest data is.
- ❌ **Don't ask hypotheticals about future behavior.** People are bad at predicting it.
- ❌ **Don't ask compound questions.** One at a time.
- ❌ **Don't reveal the hypothesis** — keep study purpose vague in the intro.

---

## 6. Opening and Closing Script Library (Swap In)

### 6a. Opening variations

**Default (60-sec consent + rapport):** See SKILL.md Consent + Recording Script.

**Short (30-sec — for follow-up sessions or low-stakes):**
> "Hi [name], thanks for joining. Quick recap: we're [brief topic], about [duration], recorded with your permission for internal research only. Any questions before we dive in?"

**Indi Young style (listening session — explicit problem-space frame):**
> "Today I'm not going to ask you about any specific product. I just want to understand how you think about [purpose — e.g., 'feeding your family during a busy week']. Whatever comes up, I want to hear it in your own words. There's no agenda I'm trying to confirm."

### 6b. Closing variations

**Default:** See SKILL.md Wrap-Up.

**Usability-test close:**
> "Before we wrap — on a scale of 1-7, how easy or difficult was that overall? What's the one thing you'd change? Anything else you want to flag?"

**Concept-test close:**
> "If a friend asked you to describe [concept] in one sentence, what would you say? Who is this for, in your mind? Is there anyone it's clearly *not* for?"

**Magic wand (works everywhere):**
> "If you had a magic wand and could change anything about [topic/product], what would you do?"

---

## 7. Sources — Full List

**Books (primary canon):**
- Portigal, S. (2023). *Interviewing Users: How to Uncover Compelling Insights* (2nd ed.). Rosenfeld Media.
- Young, I. *Practical Empathy* and *Mental Models*. Rosenfeld Media. [indiyoung.com](https://indiyoung.com/books/)
- Hall, E. (2019). *Just Enough Research* (revised ed.). A Book Apart.
- Sharon, T. (2016). *Validating Product Ideas: Through Lean User Research*. Rosenfeld Media.
- Flanagan, J. C. (1954). "The Critical Incident Technique." *Psychological Bulletin*.

**Nielsen Norman Group articles:**
- Rosala, M. — [User Interviews 101](https://www.nngroup.com/articles/user-interviews/)
- Rosala, M. — [6 Mistakes When Crafting Interview Questions](https://www.nngroup.com/articles/interview-questions-mistakes/)
- Rosala, M. — [Writing an Effective Guide for a UX Interview](https://www.nngroup.com/articles/interview-guide/)
- Rosala, M. — [The Funnel Technique in Qualitative User Research](https://www.nngroup.com/articles/the-funnel-technique-in-qualitative-user-research/)
- Rosala, M. — [5 Facilitation Mistakes to Avoid](https://www.nngroup.com/articles/interview-facilitation-mistakes/)
- Rosala, M. — [Why User Interviews Fail](https://www.nngroup.com/articles/why-user-interviews-fail/)
- Rosala, M. — [The Critical Incident Technique in UX](https://www.nngroup.com/articles/critical-incident-technique/)
- Pernice, K. & Moran, K. — [Thinking Aloud: The #1 Usability Tool](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/)
- Fessenden, T. — [Talking with Users in a Usability Test](https://www.nngroup.com/articles/talking-to-users/)
- Fessenden, T. — [Checklist for Moderating a Usability Test](https://www.nngroup.com/articles/usability-checklist/)
- NN/g — [Qualitative Usability Testing: Study Guide](https://www.nngroup.com/articles/qual-usability-testing-study-guide/)

**Author-led / community:**
- Anderson, N. — [User Research Academy](https://www.userresearchacademy.com/) / [UXR Strategist Substack](https://www.uxrstrategist.com/)
- dscout *People Nerds* — [17 Pro Tips to Perfect One-on-One Interviews](https://dscout.com/people-nerds/tips-master-researcher-participant-interviews), [Dig Deeper with Follow-Up Questions](https://dscout.com/people-nerds/generative-research-questions)
- Hall, E. — [Interviewing Humans (Medium)](https://medium.com/research-things/interviewing-humans-fa198f809c40)
