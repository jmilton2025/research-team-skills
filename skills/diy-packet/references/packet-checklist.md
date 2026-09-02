# Packet Checklist — What Makes It Truly Self-Serve

A DIY packet has failed at its one job if the requester still needs to ping a researcher to understand the document itself. Use this checklist before handing a packet off. If any row fails, fix it before sharing — don't ship a packet that's really a research plan with a friendlier font.

## The core test

Read the packet as if you have never run a study before and no one is sitting next to you. At every point, ask: **do I know exactly what to do next, or do I have a question only a researcher could answer?** If the second thing happens even once, the packet isn't done.

## Checklist

- [ ] **Content traces back to an upstream output, not a fresh guess.** The learning goal, audience, and questions should match what's in the `/diy-research-plan`, `/screener`, and `/unmod-script` outputs for this study — this packet assembles those, it doesn't invent them. If a section was hand-authored inline because no upstream output existed yet, that should be stated plainly, not disguised as if it came from a plan.
- [ ] **No unexplained jargon.** Every research term that appears (screener, unmoderated, fit gate, wrap-up) is either defined inline the first time it's used, or replaced with plain language entirely. A requester should never need to look up a word to understand their own packet.
- [ ] **Every fill-in field has a guidance sentence right next to it.** Not above it, not in a separate legend — next to it, so there's no ambiguity about what's wanted when the requester sits down to fill it in.
- [ ] **The fit gate comes first and is impossible to skip past.** A requester who doesn't belong in the DIY track should find that out in the first section, not discover it halfway through building a test that was never going to answer their question.
- [ ] **One learning goal, stated once, in plain language.** If the packet is quietly carrying three or four goals dressed up as one, that's a scope problem the packet should have caught, not passed along.
- [ ] **Tasks describe goals, not interface elements.** "Find a way to add this to your list," not "tap the plus icon." A requester writing their own tasks will default to UI language unless the packet's examples show them otherwise.
- [ ] **The wrap-up safety-net questions are present and unmodified.** These exist precisely because a first-time test-writer won't know what they forgot to ask. They're not optional filler.
- [ ] **Escalation triggers are concrete examples, not a vague "if you get stuck."** A non-researcher doesn't reliably know what "stuck" means in a research context. Name the actual signals (confused by the test itself, wants to ask a follow-up, results feel bigger than the original question).
- [ ] **The findings section is a summary table, not a research report.** If it's grown Finding/Insight/Recommendation rungs, evidence-density rules, or a priority-emoji system, it has quietly become a `/report` output and should route there instead.
- [ ] **Length stays around a quarter of a full Research Project Plan.** If the document is creeping toward RPP length, some section is doing more than a DIY packet should — cut it back or admit the request has outgrown DIY scope.
- [ ] **It's one document.** Everything the requester needs to actually run the test lives in this one packet, or is a single clear pointer away (`/screener`, `/unmod-script`). No suite of five linked docs to assemble themselves.
- [ ] **Multi-item or comparison studies list every stimulus, not just one link.** If the study reacts to more than one item or compares two versions, Section 4a names each one with its link/asset and any variant-specific notes — a requester shouldn't have to guess which asset goes with which question. Two-version comparisons also note the alternating order so one version doesn't get an unfair "seen first" advantage.
- [ ] **A person with zero research background could hand this to someone else and have them run it identically.** This is the real bar — not "would a researcher approve of this," but "would two different non-researchers produce the same study from the same packet."

## Common failure signs (fix these before calling it done)

| Symptom | What it means |
|---|---|
| A field's guidance uses a term the field itself is defining | The explanation is circular — rewrite in plainer words |
| The packet has grown past ~2 pages | Some section has research-plan-level depth; trim or escalate |
| A task asks the participant to do more than one thing | Split it, or it'll produce data no one can cleanly read |
| The findings table has more than ~8 rows | It's becoming a report; route to `/report` instead |
| The escalation section reads like a disclaimer, not a checklist | Rewrite with the same fill-in-friendly concreteness as the rest of the packet |
