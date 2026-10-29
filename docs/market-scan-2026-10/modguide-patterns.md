# Reusable patterns for a moderation-guide skill

Every idea below comes from a source I opened (see catalog.md). Each excerpt is verbatim and at most 5 lines. I put the specific, less common ideas first within each theme.

---

## 1. Inputs and intake (before drafting anything)

**1.1 Ask what decision the research feeds, not only the topic.**
> "What specific questions does the team need answered? / What decisions will this research inform? / What assumptions need validation?"
Source: https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/interview-script/SKILL.md

**1.2 Run an adaptive intake: at most 4 questions, each with numbered options plus "Other".** Anything the user already supplied in the invocation counts as answered.
> "Anything supplied with the invocation itself ... counts as answers already given. Use it and skip whatever it covers; don't re-ask."
> "This interactive skill asks **up to 4 adaptive questions**, offering **3-4 enumerated options** at each step."
Source: https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/discovery-interview-prep/SKILL.md

**1.3 Write the moderator's own hypotheses into the guide header,** so confirmation and disconfirmation are visible.
> "**Hypotheses I'm holding loosely:** - [What I think I'll find. Naming this helps me notice when I confirm vs disconfirm it.]"
Source: https://github.com/rampstackco/claude-skills/blob/main/skills/ux-research/references/interview-guide-template.md

**1.4 Remove from the guide any question that the screener or analytics can answer.**
> "We should not ask this question in our interview. Instead, we should recruit people who use (or don't use) Netflix ... Rather than asking this question in an interview, we can (and should) answer this question by using behavioral analytics."
Source: https://www.producttalk.org/2022/09/story-based-customer-interviews/

**1.5 Fail honestly when inputs are missing.** State the gap rather than invent stimuli, tasks, or prototype details.
> "When a required input, tool, or data source is unavailable or unverifiable, the sanctioned output is the deliverable with the gap stated ... A stated gap is a complete answer."
Source: https://github.com/rampstackco/claude-skills/blob/main/skills/usability-testing/SKILL.md

---

## 2. Guide structure, header and timing

**2.1 Make the guide header a mini research plan,** so stakeholders review one document: project, date, stakeholders, researcher, session length, background, objectives, must-have questions, nice-to-have questions.
> "Section 4: Must-have questions/criteria to cover / Section 5: Nice-to-have questions/topics to explore / Section 6: Introduction (5 minutes) / Section 7: Warm-up (10 minutes) / Section 8: Digging deeper (25 minutes)"
Source: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

**2.2 Tier questions as Must / Nice-to-have, and cut probes before core questions when time runs short.**
> "Cut probing before you cut core questions ... Mark which core questions are essential before the interview starts so you know what you can't skip."
Source: https://greatquestion.co/blog/how-to-write-a-discussion-guide-for-user-interviews

**2.3 Don't leave the most important questions to the end. Time-box each topic.**
> "don't leave your most important questions until the very end in case a user spends more time than you anticipate ... By allocating time to each topic ahead of time, you can assess when you've spent too much time on one topic and need to skip ahead"
Source: https://handbook.gitlab.com/handbook/product/ux/ux-research/discussion-guide-user-interviews/
For usability tasks: "As a general rule, start with the tasks that matter most to you." (https://handbook.gitlab.com/handbook/upstream-studios/experience-research/writing-usability-testing-script/)

**2.4 Cap core questions at 4-6. If there are 10, you won't get to them.**
> "Your core questions should be four to six questions. Not ten. You won't get to ten."
Source: https://greatquestion.co/blog/how-to-write-a-discussion-guide-for-user-interviews

**2.5 Order questions by chronology or journey phase, and save reflective questions for late in the session.**
> "Save reflective questions for later, since introducing them too early may produce stereotypical responses." (NN/g, as summarized by WebFetch)
Source: https://www.nngroup.com/articles/interview-guide/

**2.6 Set length guardrails.** Moderated usability sessions run 30-45 minutes (60 max). Unmoderated sessions run 15-20 minutes. Use 3-4 tasks (GitLab), or 5-7 tasks for 45-60 minutes (dscout).
> "unmoderated test sessions should be 15 - 20 minutes max and moderated sessions 60 minutes max."
Sources: https://handbook.gitlab.com/handbook/product/ux/ux-research/usability-testing/ , https://dscout.com/people-nerds/usability-task-writing

**2.7 Include a "bonus" section and a parking lot** for when you run ahead of time or something comes up for later.
> "Incorporate a bonus section into your script that covers some nice-to-have questions."
Source: https://thoughtbot.com/blog/user-testing-gone-wild-a-guide-to-course-correction ; parking lot: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

**2.8 Mark segment variants explicitly.** If one line differs per segment, call it out inline. If more than one line differs, duplicate the whole guide per segment.
> "If it's just one line of questions, I find it's ok to call them our per segment. If it's more than that, I repeat the entire guide for the second segment"
Source: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

---

## 3. Intro / consent script

**3.1 Distance the moderator from the design.**
> "Do not present yourself as the person who is involved in creating the concept that's being tested (even if you were). Emphasize that the participant won't hurt your feelings regardless of what they say"
Source: https://handbook.gitlab.com/handbook/upstream-studios/experience-research/writing-usability-testing-script/
Variant: "you can simply say you're on the product team (as opposed to the design team...)" (https://www.lyssna.com/blog/ux-research-discussion-guide-template/)

**3.2 Pre-empt questions you won't answer during the session (Krug).**
> "If you have any questions as we go along, just ask them. I may not be able to answer them right away, since we're interested in how people do when they don't have someone sitting next to them to help."
Source: https://sensible.com/downloads/test-script-web.pdf

**3.3 Use a "no vested interest" line.**
> "Please know that there are no right or wrong responses to anything we're going to discuss. And I have no vested interest in how you respond to anything today. In fact, the more candid and detailed you can be, the easier my job will be."
Source: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

**3.4 Remote consent: confirm name pronunciation, then have the participant read the consent form aloud and say their full name.**
> "Before we begin, is [name] the correct way to pronounce your name? ... Please read this out loud, and then if you agree, please say your full name out loud."
Source: https://www.nngroup.com/articles/moderated-remote-usability-test/

**3.5 Disclose observers and their limits.**
> "there are a few people from the Web design team observing this session in another room. (They can't see us, just the screen.)"
Source: https://sensible.com/downloads/test-script-web.pdf

**3.6 Script stage directions in a different format from spoken lines,** for example "[Wait for consent]" or "START the SCREEN RECORDER".
> "Give them a recording permission form and a pen / While they sign it, START the SCREEN RECORDER"
Source: https://sensible.com/downloads/test-script-web.pdf

---

## 4. Warm-up

**4.1 Warm-up questions must not be data collection in disguise.**
> "Common mistakes: asking warm-up questions that are actually research questions in disguise. 'How long have you used our product?' is not warm-up. It's data collection."
Source: https://greatquestion.co/blog/how-to-write-a-discussion-guide-for-user-interviews

**4.2 Capture the participant's mental model before they see the design.**
> "We have a page called Security Dashboard. What tasks would you expect to be able to accomplish with the help of that page?"
Source: https://handbook.gitlab.com/handbook/upstream-studios/experience-research/writing-usability-testing-script/

**4.3 Use the warm-up as a calibration check** on verbosity and on audio and video framing.
> "Use this warm-up time to gauge how interested your participant is in the topic and whether they're verbose or more withdrawn. Also check that they're framed and lit properly"
Source: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

**4.4 Ask at least 2 warm-up questions even when you need no data from them.**
> "Even if you don't have anything you want to ask, have at least 2 quick questions here"
Source: https://handbook.gitlab.com/handbook/upstream-studios/experience-research/writing-usability-testing-script/

**4.5 Krug's home-page tour (look, don't click)** for first impressions before any tasks.
> "tell me what you make of it: what strikes you about it, whose site you think it is, what you can do here, and what it's for ... You can scroll if you want to, but don't click on anything yet."
Source: https://sensible.com/downloads/test-script-web.pdf

---

## 5. Question-writing rules

**5.1 Research questions are not interview questions.** The skill should output both and show the mapping.
> "Research questions are what we want to learn from our customers. However, they don't always make the best interview questions."
Source: https://www.producttalk.org/2022/09/story-based-customer-interviews/

**5.2 Anchor questions in a specific past instance, not a general experience.** "Tell me about your experience with X" is open but still speculative.
> "We need to add a new piece of advice to our question criteria: Keep the interview grounded in specific instances of past behavior."
Source: https://www.producttalk.org/2022/09/story-based-customer-interviews/

**5.3 "How often" and "how many" questions are closed too,** not only yes/no questions.
> "It's easy to think only yes or no questions are closed questions. But that's not true. A closed question is one that is designed to collect a limited response."
Source: https://www.producttalk.org/2022/09/story-based-customer-interviews/

**5.4 Respect memory limits.**
> "As a best practice, don't ask about past behavior that occurred more than 2 months ago."
Source: https://handbook.gitlab.com/handbook/product/ux/ux-research/discussion-guide-user-interviews/

**5.5 Never ask participants what they want, or what they would do in the future.** Use a rewrite rule.
> "Instead of asking 'Would you use this feature?' ask instead 'How are you currently accomplishing this task?'"
Source: https://handbook.gitlab.com/handbook/product/ux/ux-research/discussion-guide-user-interviews/

**5.6 Give each question a Rationale / Follow-up / Avoid triplet** in the output format.
> "1. **[Question 1]** — [Rationale for asking this] / - **Follow-up:** [Dig deeper with...] / - **Avoid:** [Don't ask leading version like...]"
Source: https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/discovery-interview-prep/SKILL.md

**5.7 When several moderators share a guide, write core questions word for word** and write conditional probes, not principles.
> "Write core questions word-for-word, not as concepts ... Instead of 'probe for detail,' write 'if they mention frustration, ask: what was the impact, who else experienced that, what would fix it?'"
Source: https://greatquestion.co/blog/how-to-write-a-discussion-guide-for-user-interviews

**5.8 Ask indirect questions sparingly and interpret them carefully** (Kvale and Brinkmann question types: probing, specifying, direct, indirect, interpreting). Save direct questions (your own topics) for the end, so the participant's framing comes first.
Source: https://ixdf.org/literature/article/how-to-moderate-user-interviews (WebFetch summary)

---

## 6. Leading-question detection (lint rules the skill can apply)

**6.1 NN/g's four traps, with rewrites.**
> "Do not rephrase in our own words. ... Improvement: 'You mentioned the picture…?'"
> "Do not suggest an answer. 'How well would this save time for you...' Improvement: 'How might this affect your efficiency, if at all?'"
> "Do not name an interface element. ... Improvement: 'This area on the side of the page… [point to area]. What is that?'"
> "Do not assume you know what the user is feeling. ... Improvement: 'What was easy or difficult about completing that task?'"
Source: https://www.nngroup.com/articles/leading-questions/

**6.2 A balanced-pair rewrite and the "if at all" suffix.**
> "| 'Did you find it easy?' | 'How easy or difficult was that for you?' | ... | 'Would you use this?' | 'How would you use this in your work, if at all?' |"
> "If the question can be answered with yes or no, extend it ('...and why?')."
Source: https://github.com/owl-listener/designer-skills/blob/main/design-research/skills/interview-script/SKILL.md

**6.3 Audit with a question table and pattern list** (Verdict / Problem / Rewrite).
> "| Question | Verdict | Problem | Mom Test Rewrite |"
> "**Hypotheticals**: 'Would you...' / 'If we built...' / 'Could you see yourself...' ... **Pitching disguised as asking**: 'What if there was a product that [your product]...'"
Source: https://github.com/amplitude/builder-skills/blob/main/product-skills/skills/mom-test/SKILL.md

**6.4 The "could they give the opposite answer?" test.**
> "Read them out loud. Does the question already contain an answer? Could a reasonable participant give you the opposite response? If not, it's leading."
Source: https://greatquestion.co/blog/how-to-write-a-discussion-guide-for-user-interviews

**6.5 Questions that blame the user count as leading too.**
> "It also puts the blame on the user, rather than on the site."
Source: https://www.nngroup.com/articles/leading-questions/

**6.6 Moderator recovery line for a leading question already asked.**
> "| You realize the question was leading | 'Let me ask that differently. What's been your experience with [topic], in your own words?' |"
Source: https://github.com/rampstackco/claude-skills/blob/main/skills/ux-research/references/interview-guide-template.md

---

## 7. Probes and follow-ups

**7.1 Separate follow-ups (detail) from probes (elaboration) in the guide.**
> Follow-ups add detail ("Where were you when this happened?"). Probes encourage elaboration ("Why is that important to you?").
Source: https://www.nngroup.com/articles/interview-guide/ (WebFetch summary)

**7.2 Write conditional "if not mentioned" probes for priority topics.**
> "If they haven't mentioned budget constraints, ask: 'How do budget cycles affect these kinds of decisions?' / If they haven't mentioned internal champions, ask: ..."
Source: https://greatquestion.co/blog/how-to-write-a-discussion-guide-for-user-interviews

**7.3 Pull the participant from generalities back to the specific story,** at a natural pause.
> "most people will flip-flop between the specific story and generalities ... The interviewer's job is to gently guide the participant back to the specific instance ... wait for a natural pause"
Source: https://www.producttalk.org/2022/09/story-based-customer-interviews/

**7.4 Probe contradictions.**
> "Earlier you said X, now you're saying Y. Help me understand."
Source: https://github.com/rampstackco/claude-skills/blob/main/skills/ux-research/references/interview-guide-template.md

**7.5 Cap the "why" chain.**
> "Asking 'why' more than 2 to 3 times in a row (becomes interrogation)"
Source: rampstack interview-guide-template (above). Also "Ask 'What were you thinking?' not 'Why did you do that?'" (https://github.com/slgoodrich/agents/blob/main/plugins/ai-pm-copilot/skills/usability-frameworks/references/think-aloud-protocol-guide.md)

**7.6 Use silence as a scripted probe** (3-5 seconds after an answer).
> "Researcher: 'What's frustrating about your current process?' / Participant: 'Oh, it's pretty annoying.' / [Researcher: STAYS SILENT, nods] / Participant: 'Actually ... I almost quit over it last month.'"
Source: https://github.com/slgoodrich/agents/blob/main/plugins/ai-pm-copilot/skills/interview-frameworks/references/interviewing-best-practices-guide.md

---

## 8. Task design for usability tests

**8.1 Add a grey "What we expect them to do" note per task,** plus the prototype link. This helps the moderator rescue a failed prerequisite task.
> "Consider noting under each task, in light gray, 'What we expect them to do' ... This will assist the moderator in helping participants to recover, in case they fail a task which is a prerequisite for the following task."
Source: https://handbook.gitlab.com/handbook/upstream-studios/experience-research/writing-usability-testing-script/

**8.2 Write success criteria for the notes only, not for the participant.**
> "**Success criteria** (for your notes, not shared with participant):"
Source: https://github.com/slgoodrich/agents/blob/main/plugins/ai-pm-copilot/skills/usability-frameworks/assets/usability-test-script-template.md

**8.3 Elicit the participant's vocabulary, then use it in the task wording.**
> "Start each task by asking the participant to describe the thing you are wanting them to do in the system and walk you through how they would normally do that task. Then you can use the words the participant has just used"
Source: https://handbook.gitlab.com/handbook/upstream-studios/experience-research/writing-usability-testing-script/

**8.4 NN/g's 10 task mistakes as a lint list:** words from the UI, revealing steps, out-of-date dates, too simple, elaborate backstory, ad copy, emotional triggers (Mother's Day), jokes or famous names, offensive topics, "How would you…".
> "Potentially upsetting task: Mother's Day is coming up. Find a bouquet to send your mother. / Improvement: Send your friend flowers to celebrate her new job."
> "Instructing the user to talk instead of perform: How would you find the symptoms of the flu?"
Source: https://www.nngroup.com/articles/better-usability-tasks/

**8.5 Specific is not leading.** Give the data participants need for the task.
> "Poor task: Make an appointment with your dentist. / Better task: Make an appointment for next Tuesday at 10am with your dentist, Dr. Petersen."
Source: https://www.nngroup.com/articles/task-scenarios-usability-testing/

**8.6 Make "too simple" tasks require processing, not just locating.**
> "Too-easy task: Who scored the most points ... Improvement: Who scored more points ... Russell Westbrook or LeBron James?"
Source: https://www.nngroup.com/articles/better-usability-tasks/

**8.7 Include a deliberate error-recovery task.**
> "**Task 3 (Error recovery):** 'Try to invite a colleague using the email address: not-an-email' - Success: User sees error message and corrects it"
Source: https://github.com/nickcrew/claude-ctx-plugin/blob/main/skills/ux-researcher/SKILL.md

**8.8 Avoid task-setup pitfalls:** tasks the participant has already done ("I already have an account"), tasks needing data the participant doesn't have (provide a test account), and role-play ("Imagine you're a CFO").
> "If the participant is not a CFO, they're roleplaying. Findings tell you about roleplay, not real CFO behavior."
Source: https://github.com/rampstackco/claude-skills/blob/main/skills/usability-testing/references/task-script-patterns.md

**8.9 Order tasks by difficulty** (warm-up task, then primary, secondary, stretch), and have the participant read the task back.
> "I'll read each task aloud and you'll also have it written down. Please read it back to me so I know we're on the same page."
Source: https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/main/.claude/skills/ux-research/usability-testing/SKILL.md

**8.10 Use a "no Search" constraint when testing navigation (Krug).**
> "I'm also going to ask you to do these tasks without using Search. We'll learn a lot more about how well the site works that way."
Source: https://sensible.com/downloads/test-script-web.pdf

**8.11 Post-task questions: ask the SEQ, then "Why that rating?", then probe one observed behaviour.** Don't ask participants whether they completed the task.
> "'I noticed you [behavior]—what were you thinking there?'"
Source: slgoodrich script template (above)
> "Why should I not ask in user testing if a participant completed a task successfully? It's a self-reported measure which may or may not be true."
Source: https://handbook.gitlab.com/handbook/product/ux/ux-research/usability-testing/

---

## 9. Think-aloud prompts

**9.1 Demonstrate think-aloud, then run a practice task on something unrelated.**
> "Let's practice with a quick warm-up. Imagine you're on Google and want to find what time the library closes. Just think out loud as you'd do that."
Source: https://github.com/slgoodrich/agents/blob/main/plugins/ai-pm-copilot/skills/usability-frameworks/references/think-aloud-protocol-guide.md

**9.2 Neutral nudge prompts vs banned prompts.** Prompt after 10-15 seconds of silence, and rotate the prompts.
> Good: "What are you looking at?" / "What are you looking for?" / "Keep talking out loud, please"
> Bad: "Are you confused?" (Leading) / "Did you see the button?" (Helping) / "Is this hard?" (Suggesting difficulty)
Source: think-aloud-protocol-guide (above)

**9.3 Flag segments your own prompt may have biased and discard them.**
> "At the very least, try to identify those cases where you've biased the user so you can discard that small part of the study."
Source: https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/

**9.4 Choose concurrent, retrospective or hybrid think-aloud by task type.** Use retrospective for fast tasks or tasks where you measure time.
Source: https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/main/.claude/skills/ux-research/usability-testing/SKILL.md

---

## 10. Handling participant questions, silence, "stuck" and off-track

**10.1 Echo / Boomerang / Columbo (NN/g).**
> Echo: "Not sure what?" or "Table is weird?" / Boomerang: "What do you think?" or "What would you normally do?" / Columbo: "You are wondering if [pause] you might [pause]."
> Avoid hedges such as "I guess so," "I don't think so," or "Try it." When unsure, "count to 10 silently."
Source: https://www.nngroup.com/articles/talking-to-users/ (WebFetch summary)

**10.2 Stuck ladder with timings.**
> "Wait at least 30 seconds before intervening. Real frustration is signal. ... If they're still stuck after another 30 seconds, you can offer a hint: 'What might happen if you scrolled?' But this is a last resort."
Source: https://github.com/rampstackco/claude-skills/blob/main/skills/usability-testing/references/task-script-patterns.md

**10.3 When the participant says "I give up", acknowledge it, then ask about real-world fallback behaviour.**
> "**Ask**: 'What would you do if this were real and you really needed to do this?' - They might say 'I'd Google it' or 'I'd ask someone'"
Source: think-aloud-protocol-guide (above)

**10.4 Self-blame reframe.**
> "**Signs**: 'Oh, that's probably just me' ... **Reassure**: 'If it confused you, that's exactly what we need to know'"
Source: think-aloud-protocol-guide (above)

**10.5 When asked "What do you think?" or "What are you working on?", defer until the end.**
> "'I want to hear your unbiased thoughts first. Happy to share more at the end.'"
Source: rampstack interview-guide-template (above)

**10.6 Polite-lying detection.**
> "'You seem hesitant. What's actually going through your mind?'"
Source: https://github.com/slgoodrich/agents/blob/main/plugins/ai-pm-copilot/skills/interview-frameworks/references/interviewing-best-practices-guide.md

**10.7 Off-track redirect: acknowledge first, then use a structuring question.** Let a tangent run only if it serves the objective. One threshold: redirect after 10+ minutes off-topic.
> "'That's really interesting. I want to make sure I get to [topic] in our time together. Can I steer us back to [question]?'"
Source: slgoodrich best-practices guide (above). Also https://ixdf.org/literature/article/how-to-moderate-user-interviews

**10.8 For the "expert" participant who redesigns as they go, note the suggestion and refocus on the task.**
> "**Acknowledge**: 'That's a great suggestion, I'll note it' / **Refocus**: 'For now, just focus on trying to complete the task as a user'"
Source: think-aloud-protocol-guide (above)

**10.9 Emotional moments: pause and acknowledge before moving on.**
> "| Participant has emotional reaction | Pause. Acknowledge. 'That sounds like it was really frustrating. Take your time.' Don't rush past. |"
Source: rampstack interview-guide-template (above)

---

## 11. Prototype and stimulus caveats

**11.1 Set expectations for low-fidelity prototypes,** and say you weren't involved in making them.
> "If it's a low-fidelity prototype, explain that some things won't be working properly, and that's okay."
> "it's important to let them know that you either didn't contribute to the design or creation in any way (assuming you didn't). If you did contribute, don't mention this."
Source: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

**11.2 Prepare a broken-prototype fallback.** Use print-outs or sketches, or ask the participant to draw their current tool.
> "Bring print-outs of your screens as a backup plan. Have the user tap on elements and ask what they would expect to happen next."
Source: https://thoughtbot.com/blog/user-testing-gone-wild-a-guide-to-course-correction

**11.3 Show the stimulus, then wait.**
> "[Wait. Don't fill the silence.] / 'What's your initial reaction?' / 'What questions does this raise?'"
Source: rampstack interview-guide-template (above)

**11.4 Cover current behaviour before showing any design.**
> "Showing the design before understanding current behavior"
Source: https://github.com/nickcrew/claude-ctx-plugin/blob/main/skills/ux-researcher/SKILL.md (Common Mistakes)

**11.5 Put screenshots of the stimulus inline in the guide** next to the questions about them.
> "For evaluative research projects, insert screenshots into your guide alongside your questions and activities."
Source: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

**11.6 Pilot in incognito, or with someone who has no internal access.**
> "pilot all tasks/activities in advance with a participant who either doesn't have internal access to your tools and platforms, or with someone in incognito mode."
Source: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

**11.7 Keep tasks current, and the prototype too.** Re-date tasks the day before; host prototype files locally; test on the same device.
Sources: https://www.nngroup.com/articles/better-usability-tasks/ (mistake #3), thoughtbot (above)

---

## 12. Wrap-up

**12.1 Play back what you heard on the must-have questions,** so the participant can correct it.
> "I also repeat what I think I heard in response to the must-have questions and ask the participants to correct or confirm for accuracy."
Source: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

**12.2 Collect observer questions before closing.** Krug calls the observation room; remotely, check the side channel.
> "If you'll excuse me for a minute, I'm just going to see if the people on the team have any follow-up questions they'd like me to ask you."
Source: https://sensible.com/downloads/test-script-web.pdf

**12.3 Use the same closing ritual every session,** with a catch-all question and a snowball referral.
> "Is there anything I should have asked but didn't?" / "Who else should I talk to about this?"
Sources: rampstack interview-guide-template; https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/interview-script/SKILL.md

**12.4 Ask permission to recontact the participant,** and include incentive logistics.
> "would it be okay if I reached out for follow-up research? I won't bombard you"
Source: rampstack interview-guide-template (above)

---

## 13. Mapping questions back to research questions

**13.1 Build a coverage matrix.** Every question, task, and activity supports at least one objective. Optionally add a second matrix mapping questions to assumptions.
> "Every question, task, and activity should support at least one goal or objective ... you can also create a separate table to align your questions to your assumptions."
Source: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

**13.2 Check coverage in both directions:** orphan questions get cut, and uncovered research questions get new questions.
> "If you can't answer that, cut the question." (Great Question) ; NN/g: align each question with a research question and write new questions for gaps.
Sources: https://greatquestion.co/blog/how-to-write-a-discussion-guide-for-user-interviews , https://www.nngroup.com/articles/interview-guide/

**13.3 Turn the guide into a notes grid:** questions in a frozen column A, one column per participant.
> "Column A is 'frozen' so it's always visible. The rest of the columns, for example B-J, are used for participant notes."
Source: https://www.lyssna.com/blog/ux-research-discussion-guide-template/

---

## 14. Remote vs in-person

**14.1 Task delivery order of preference for remote sessions:** paste the task in chat and have the participant read it aloud, then a PDF with one task per page, then the moderator reads it (least advisable).
> "The ideal way to deliver tasks is one at a time, and by asking participants to read the task out loud themselves. That way: You know they've read the entire task. They won't look ahead to later tasks."
Source: https://www.nngroup.com/articles/moderated-remote-usability-test/

**14.2 Hold a 15-minute tech-practice session the day before** on an unrelated site, plus a participant reminder checklist (charger, headset, quiet place, wired connection).
Source: https://www.nngroup.com/articles/moderated-remote-usability-test/

**14.3 Remote think-aloud needs to be more explicit,** and you need a backup channel.
> "Be more explicit about think-aloud since you can't see them"
Source: https://github.com/slgoodrich/agents/blob/main/plugins/ai-pm-copilot/skills/usability-frameworks/assets/usability-test-script-template.md

**14.4 In person, sit beside the participant, not across.**
> "If you are sitting across from them, swing around and sit next to them."
Source: https://thoughtbot.com/blog/user-testing-gone-wild-a-guide-to-course-correction

**14.5 Unmoderated variant: make tasks more specific, include written follow-ups, and add an escape hatch.**
> "**Provide escape hatch** ('If you can't complete this, click I'm stuck')"
Source: Prorise usability-testing (above). Also Great Question: "add follow-up prompts in writing".

---

## 15. Note-taker and observer roles

**15.1 Keep the team to at most 2 people in the room.** One person talks. Observers pass questions on post-its or through a side channel.
> "A usability test should have no more than two people from your team ... If you are an observer and have a question you'd like to ask, write it on a post-it and pass it to the facilitator."
Source: https://thoughtbot.com/blog/user-testing-gone-wild-a-guide-to-course-correction

**15.2 Include an observer brief and ground rules in the guide:** read the brief, join early, stay muted, route questions through the moderator, hold off on solutions, join the debrief.
Source: https://www.lyssna.com/blog/how-to-observe-user-interviews/

**15.3 Give each observer a lens.**
> "One person might capture quotes, another track usability problems, and another note anything related to a specific feature or business question."
Source: https://www.lyssna.com/blog/how-to-observe-user-interviews/

**15.4 Add a co-host to watch the chat when observers are active.** Timestamp notes, and use a shared template.
Source: https://www.lyssna.com/blog/how-to-observe-user-interviews/

**15.5 Per-task observer fields:** start/end time, Complete/Partial/Fail, errors, assists, path taken.
Source: https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/main/.claude/skills/ux-research/usability-testing/SKILL.md

**15.6 Two-column notes: observations vs interpretations.**
Source: https://github.com/slgoodrich/agents/blob/main/plugins/ai-pm-copilot/skills/interview-frameworks/SKILL.md

---

## 16. Quality checks (pre-flight and post-session)

**16.1 Pre-flight review questions:** Does the guide cover the objectives? Does the timing work? Then a stakeholder review, then a pilot with a colleague.
Source: https://handbook.gitlab.com/handbook/upstream-studios/experience-research/writing-usability-testing-script/

**16.2 Rules for changing the guide mid-study.**
> "is this question broken because it's poorly worded, or because my research objective was unclear? Have I asked it in enough interviews to know it's not working? If I change it, can I still compare data across sessions?"
Source: https://greatquestion.co/blog/how-to-write-a-discussion-guide-for-user-interviews

**16.3 Moderator self-scorecard after each session.**
> "- Did I talk more than 20%? (Y/N) / - Did I ask leading questions? (Y/N) / - Did I probe surface-level answers? (Y/N) / - Did I use silence effectively? (Y/N)"
Source: slgoodrich interviewing-best-practices-guide (above)

**16.4 Post-session capture within an hour:** 3-5 vivid moments, quotes, and new questions that should change later sessions. Start synthesis immediately.
Source: rampstack interview-guide-template (above)

**16.5 Calibrate across moderators:** run one interview together and debrief before the study starts.
Source: https://greatquestion.co/blog/how-to-write-a-discussion-guide-for-user-interviews

---

## 17. Anti-patterns (for a "don't" section or a lint pass)

- Interviews that turn into sales pitches: "our first several 'interviews' were actually sales pitches (e.g. 'here's this cool new thing, what do you think?')" (https://github.com/refoundai/lenny-skills/blob/main/skills/customer-interviews/SKILL.md)
- Counting compliments and future promises as signal: "Compliments are NOT commitment. 'That sounds cool' means nothing." (amplitude mom-test)
- Treating participant suggestions as features (rampstack usability-testing)
- A question list instead of a guide, with no transitions or time allocation (Great Question)
- Reading the guide verbatim: "If you're reading questions verbatim, you're not listening." (Great Question)
- Multi-part questions, and multiple tasks in one: "Sign up, create a project, and invite a teammate. This is three tasks." (rampstack task-script-patterns)
- Defending the design, or helping too early (rampstack usability-testing)
- Staying completely silent instead of probing skilfully (NN/g talking-to-users)
- Running observers as visible call participants, especially senior ones: "I don't know if I want to say the wrong thing with the CEO here in front of me" (Lyssna observers)
- Using "awesome discount"-style biasing content in tasks (dscout)
