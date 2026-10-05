# Source and Delivery Safety — Research Plan

Read this reference whenever a run uses non-public material or creates a Google Doc. It defines the authorization, minimization, storage, sharing, and write-recovery rules that the main workflow summarizes.

## 1. Authorize sources before access

**Connector access is not requester authorization.** A working connector proves technical access only. Before opening, searching, copying, quoting, linking, or handing off a non-public source or bounded source class, confirm and record:

- the requester's authority to use it for this study and its **approved AI processing** status, including consent, contractual, policy, or residency restrictions;
- the **intended audience** and **source ACL** (access control list);
- **quote/link disclosure** permission for that audience;
- the **minimum necessary** content and how to redact or **de-identify** it before local storage, model processing, or reviewer handoff; and
- provenance: canonical URL or file ID, owner/system, **source revision** or version, **retrieval timestamp**, and **content hash** when available.

Record the authorization basis available for the study, such as a researcher attestation with role and project context, an approved protocol or data-use policy, or source-owner/data-governance confirmation. Mark unavailable provenance fields as unavailable. Never infer permission from technical access.

If any required authorization is unknown, stop before reading that source. Ask the researcher to confirm it or skip the source. A skipped source remains unverified, cannot support a claim, and stays out of the plan, including its link in the Appendix. An authorization given later in the run counts from then on; record it like the others.

Connection checks run at the start of Step 1, before this gate, so they must be non-content-bearing authentication, capability, or metadata checks. Do not retrieve source content merely to test a connector; when a connector's only tools return content, rely on its sign-in status instead.

## 2. Minimize local and reviewer data

Create working files in a **private, non-repository working directory** with owner-only permissions. Do not use `/tmp` for files that later steps require. Before copying content, define a **retention and cleanup plan**: what is retained, why, where, until when, and who may access it.

Keep only the approved plan and minimum necessary de-identified source extracts, manifests, raw document snapshots, request batches, and render needed for the run. At verified handoff or a blocked run, remove files no longer authorized or needed and record any approved retention exception.

Never place credentials, source text, document bodies, or other **sensitive content in command-line arguments** that you type or paste into a shell. Apply each Google Docs request body through the first of these that the integration offers:

1. a connector tool's request-body parameter;
2. the CLI's own file or standard-input option;
3. the bundled `send` helper (`python3 scripts/option4_layout.py send BATCH.json --document-id ID --response FILE`), for a CLI such as `gws` that takes the body only as an argument. The helper reads the batch from its protected file and starts `gws` directly, without a shell, so the body never appears in a typed command, the shell history, or the chat transcript, and it saves the reply with owner-only permissions. While that `gws` call runs, the body is in its process arguments, which other programs on the same computer may be able to read (for example, with `ps`). Disclose that once at the §4 preflight and use the helper only when the researcher approves it for the run.

If none of these is available or approved, block the write.

Run a separate critique agent or `multi-agent-check` only when both approved AI processing and reviewer access cover the packet and audience. Provide minimum necessary de-identified extracts, never a complete source file unless the recorded authorization explicitly covers sending that whole file to reviewers. Otherwise run the self-critique and disclose a critique-only result, using the exact review status from `SKILL.md` Step 5 (for example, `critique-only review — reviewer processing not authorized`).

## 3. Confirm the destination boundary

Confirm the **destination ACL** and **intended audience before any write or creation**, along with the exact folder. Perform a fresh permissions read that covers effective Drive permissions, inherited access, group access when visible, and link-sharing scope. The destination must be no broader than the permitted source and plan audience.

If permissions cannot be read, or access is broader, stop before writing. Ask for a compliant destination, or for the folder's owner to narrow its sharing. Never change sharing yourself or inherit a broader link-sharing policy. Assembly, critique, and review don't depend on the destination and may continue; only creation waits.

## 4. Preflight every required capability

Before creating the study Doc, verify that the authenticated integration can:

1. create or import a dedicated one-tab Doc in the confirmed folder;
2. return its ID, URL, active tab ID, raw structure, and revision;
3. apply revision-bound native batch updates;
4. re-fetch and read back content and links;
5. export or render a PDF; and
6. perform the approved cleanup or quarantine action for a partial artifact.

A listed tool or successful sign-in is not proof of these capabilities. Use documented capability metadata and non-content-bearing checks. If proof requires a disposable write that was not authorized, treat the capability as unverified and block before creating the study Doc.

For capability 3, name the request-body route from §2 that the run will use. When it is the `send` helper, ask once per run, in a pop-up labeled **“Google Docs write route”** with no “Brainstorm with me” option. Say: *“Your Google Docs tool (`gws`) can't read edits from a file, so a bundled helper passes each batch of edits to it directly. While each batch is sent, other programs on this computer could briefly see it.”* Offer **“Use the helper (Recommended)”** and **“Don't create the Doc”**. If they decline and no other route exists, block before creating the study Doc.

## 5. Create idempotently

Before creation, record the confirmed folder, exact approved title, and attempt timestamp. If creation or import has an ambiguous result because of a timeout, disconnect, or lost response, stop and reconcile before another write:

- fetch a known document ID when the response supplied one; or
- search only the confirmed folder using the exact folder, title, and attempt-time window, then inspect candidate IDs and contents.

Reuse one verified match. If there is no match, more than one plausible match, or no safe inspection path, block and report the uncertainty. **Never blindly retry a create or update.**

If import loses the required horizontal rule or produces another malformed structure, mark the Doc partial and perform approved cleanup or quarantine before a new import attempt. Make at most one new attempt, through a different import route when one exists (for example, the connector's import instead of `gws`, or the reverse). If that is malformed too, block.

## 6. Bind and reconcile writes

Immediately before every normalization or formatting write:

1. fetch fresh raw JSON and its revision;
2. generate the batch against that snapshot;
3. bind it to the **required revision ID** or equivalent atomic precondition;
4. apply it through a protected request body, using the first available route in §2's order; and
5. re-fetch and verify the expected post-state.

On a revision mismatch, ambiguous response, or concurrent edit, never reuse or resend the old batch. Re-fetch the known Doc. If the expected post-state is verified, record success and do not resend. Otherwise regenerate against the new snapshot.

A material content change requires researcher reapproval: show the other editor's change and ask whether to keep it (then update `APPROVED.md` and the manifest to match) or restore the approved text. Never keep or revert it silently. A formatting-only concurrent edit may be reconciled without reapproval only when approved meaning, evidence, and links remain unchanged. When a material change is kept, rerun the critique pass on that row; if it adds a claim the reviewers didn't see, say so when returning the Doc. Block when the state cannot be reconciled.

## 7. Handle partial documents

A failed or incomplete Doc is not a deliverable. Apply the preflighted policy:

- trash it when that action is authorized; or
- restrict it and move or retitle it in the approved quarantine location.

Record its ID, location, and status, then give the blocked result described under “Blocked result” in `SKILL.md`, unless the workflow allows a new attempt (one re-import after a malformed import, §5, or a new Doc after a mid-run skill update, `SKILL.md` Step 6.1). Never leave an unlabeled partial document in the stakeholder destination or return it as final.
