# Writing for an Unmoderated Audience

Rules specific to a script nobody will read aloud, adapt live, or use to rescue a confused participant. Every one of these exists because the moderated equivalent (see the `mod-guide` skill) has a live human who can absorb the failure mode below — an unmoderated script has to absorb it in the writing instead.

## The core difference from moderated writing

A moderation guide is written for a moderator: it can say "probe if relevant," "watch for hesitation," "use judgment on follow-up," because a person in the room fills the gap. An unmoderated script is written for the participant directly, with nobody standing by to:

- Notice they've gone to the wrong screen and correct it
- Clarify a word they didn't understand
- Rephrase a question that landed as leading or confusing
- Catch a participant who's gone quiet or given up
- Improvise a follow-up probe based on what they just said
- Reassure them mid-task that there's no wrong answer

Every one of those gaps has to be closed in advance, in the copy itself. That is the entire discipline of writing for unmoderated.

## Do

**Anchor every step to a known state.**
Open every task with a plain statement of where the participant should now be ("You should now be viewing…"). If a participant has drifted off-path, the anchor is the only thing that catches it — there's no moderator glancing at their screen. NNG's guidance on remote and unmoderated testing repeatedly flags disorientation as the single biggest driver of unusable unmoderated sessions; an anchor line costs one sentence and prevents most of it.

**Write the fallback, don't rely on recovery.**
If a step could plausibly not work as expected — a prototype hotspot that's easy to miss, a link that opens in a way the participant doesn't expect — write the recovery instruction directly into the script ("If you don't see X, try Y"). UserTesting's own task-writing guidance is explicit that self-guided testers abandon or misreport far more often when a task silently assumes success.

**Over-communicate context up front.**
State plainly, before anything else, that the participant isn't being evaluated, that there's no right or wrong answer, and that saying "I'm confused" out loud is exactly the kind of signal the study wants. A moderator can supply this reassurance mid-session if a participant tenses up; a script has to supply all of it before the session starts, because there's no second chance to say it live.

**Describe goals, not interface elements.**
"Find a way to…" survives a redesign, a different device, or a participant who can't find "the blue button" because their screen renders it differently. Interface-specific phrasing breaks silently and nobody's there to notice the participant is stuck on wording, not on the task.

**One instruction per step.**
A moderator can split a compound question into parts live if a participant only answers half of it. An unmoderated script can't — so it should never be compound in the first place. Split "what do you notice about the layout and the pricing?" into two questions or two rows.

**Capture first impressions before any interaction.**
This moment cannot be recovered once a participant starts clicking. Ask explicitly, before any task instruction, what they notice and what stands out.

**Write comprehension checks with genuinely plausible wrong answers.**
If a fixed-choice comprehension question ("what does this message mean?") has one obviously-correct answer and three throwaway distractors, it measures nothing. Distractors should represent real, plausible misreadings — the kind a skimming participant would actually produce.

**Pilot the script yourself, start to finish, before fielding.**
Read it exactly as a participant would encounter it, with no context beyond what's on the page. This is the closest available substitute for the live troubleshooting a moderator would otherwise provide.

**Keep warm-up separate from, and before, the scenario.**
General-habit questions asked before the scenario avoid priming the participant toward the "expected" reaction. Once the scenario is introduced, every subsequent answer is colored by it.

## Don't

**Don't leave a "click here" instruction unattached to what should happen next.**
"Click the link" without "you should now see X" leaves a participant with no way to confirm they're on track, and no moderator to reassure them they did it right.

**Don't use internal jargon, feature code names, or UI-team terminology.**
A moderator can translate on the fly if a participant looks confused by a term. A script can't — so participant-facing language has to already be in plain English before the study goes live.

**Don't rely on tone of voice or live rapport-building to soften a question.**
A question that sounds fine read aloud with warmth can read as blunt or judgmental in cold text on a screen. Err toward extra warmth and explicit reassurance in writing, since there's no vocal delivery to carry it.

**Don't ask "would you...?" as a primary evidence source.**
The say-do gap that NNG and Portigal both warn about in moderated interviews is worse unmoderated — there's no moderator present to redirect a hypothetical answer back to a concrete, remembered incident. Ground questions in what the participant just did or just saw; save hypotheticals for the reflective wrap-up only.

**Don't write a probe that assumes live judgment.**
"Probe further if their answer seems shallow" cannot execute unmoderated. Every follow-up a moderator might improvise has to instead be a second, pre-written question ("Why did you choose that answer?") that runs for every participant, not just the ones who seem to need it.

**Don't bury the time estimate or understate it.**
UserTesting Blog and NNG both note that self-guided participants disengage or rush when a study runs longer than promised, with nobody present to renegotiate expectations mid-session. State the real total up front and keep the welcome message's estimate in sync with the actual task list.

**Don't stack more than one new concept per task.**
A moderator can tell when a participant is overloaded and slow down. A script can't read the room — so it shouldn't ask a participant to absorb a new scenario, a new screen, and a new decision all in one step.

**Don't skip the warm, specific closing.**
A generic "thanks for completing this study" reads as colder in text than the same sentiment would sound spoken. Since the closing is the participant's last impression of the researcher, and there's no live warmth to compensate, write it as genuinely and specifically as the welcome.

## Quick contrast: moderated vs. unmoderated instinct

| Moderated instinct | Unmoderated requirement |
|---|---|
| "I'll probe if it feels relevant" | Pre-write the probe as a standing follow-up question every participant gets |
| "I'll notice if they're lost and redirect" | Anchor every task with a stated current-state line |
| "I'll rephrase if the wording lands wrong" | Pilot the wording yourself before fielding — there's no live rephrase |
| "I'll reassure them mid-session if they tense up" | Front-load all reassurance into the welcome message |
| "I'll read their tone and adjust warmth" | Write extra explicit warmth into the copy itself |
| "I'll catch it if the task doesn't work as expected" | Write the fallback instruction directly into the task |

## Sources

- Nielsen Norman Group — remote and unmoderated usability testing guidance (disorientation and drop-off as the leading unmoderated failure modes; task-wording clarity conventions)
- UserTesting Blog — task-writing conventions for self-guided testers; guidance on time-estimate accuracy and task completion
- Steve Portigal, *Interviewing Users* — rapport-building and say-do gap principles, applied here to a written, self-guided format
- dscout People Nerds — participant-experience conventions for self-serve research formats
