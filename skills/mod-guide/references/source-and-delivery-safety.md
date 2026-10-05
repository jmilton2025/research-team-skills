# Source and Delivery Safety — Moderation Guide

Read this reference whenever a run uses non-public material, sends content to a reviewer, or creates a Google Doc. It is the source of truth for authorization, minimization, consent-language boundaries, Drive permissions, idempotency, and write recovery.

## 1. Authorize sources before access

Connector access is not requester authorization. Before opening, searching, copying, quoting, linking, or handing off a non-public source, confirm and record:

- the requester's authority to use it for this study and its approved AI-processing status;
- the intended audience and source access boundary;
- whether links or excerpts may be disclosed to that audience;
- the minimum necessary content and required redaction or de-identification; and
- provenance: canonical URL/file ID, owner or source system, revision/version, and retrieval time when available.

Pasting or attaching content does not establish the requester's authority or approved AI-processing status. Apply the same confirmation, minimization, and redaction gate to pasted non-public material before using it. If source authority or AI-processing approval is unknown, stop before access and ask the researcher to confirm it or omit the source. A skipped source remains unverified and cannot support a claim.

Connection checks run at the start of Step 1, before this gate, so they must be non-content-bearing authentication, capability, or metadata checks. Do not retrieve source content merely to test a connector; when a connector's only tools return content, rely on its sign-in status instead.

Do not ingest participant names, emails, phone numbers, addresses, recruiting profiles, raw recordings, or schedule/recording links to draft a guide. Ask for a de-identified study brief instead. Moderation-guide generation normally needs the plan, stimuli, research questions, participant criteria, and approved protocol language—not participant-level data.

## 2. Minimize working and reviewer data

Prefer session-only processing with no persistent source extracts. When persistent working files are necessary, authorize their retention plan before creation: what will be retained, why, the private non-repository location, owner-only access, deletion date or event, and who may access it. Keep only the approved draft, minimum necessary de-identified extracts, manifest, fresh document snapshots, request batches, and render needed for the run.

Never place credentials, source text, document bodies, or other sensitive material directly in command-line arguments that you type or paste into a shell. Create the Doc from a protected file (for example, `gws drive files create --upload FILE`, run from the private working directory, with only the name, Doc type, and parent folder in `--json`). Apply each Google Docs request body through the first of these that the integration offers:

1. a connector tool's request-body parameter, only when that tool takes the native Google Docs batch requests unchanged and sends `writeControl.requiredRevisionId` with them. A connector edit tool with its own simplified operation format, or with no revision binding, does not qualify;
2. the CLI's own file or standard-input option;
3. the bundled `send` helper (`python3 scripts/option4_guide_layout.py send BATCH.json --document-id ID --response FILE`), for a CLI such as `gws` that takes the body only as an argument. The helper reads the batch from its protected file and starts `gws` directly, without a shell, so the body never appears in a typed command, the shell history, or the chat transcript, and it saves the reply with owner-only permissions. While that `gws` call runs, the body is in its process arguments, which other programs on the same computer may be able to read (for example, with `ps`). Use the helper only when the researcher approved it in Section 1 (`SKILL.md`, “Google Docs write route”).

If none of these is available or approved, block the write.

A connector that cannot carry these batches can still create, read back, and trash the Doc. A connector Markdown importer that takes the file's contents as a tool parameter is a protected create route. Checked on 2026-10-05, Runlayer's Google Workspace connector worked this way: `import_to_google_doc` produced native headings, tables, and bullets, and `update_drive_file` trashed the Doc, but its `batch_update_doc` uses a simplified format with no revision binding. A connector's readback can feed `normalize` and `format` only when it returns the document's `revisionId` (Runlayer's `readDocument` did not); otherwise fetch those snapshots through the route that applies the batches.

Send content to a critique agent or multi-agent reviewer only when approved AI processing and reviewer access cover that packet. Pass the minimum necessary de-identified guide plus source excerpts—not complete source files by default. Otherwise run the mandatory self-contained baseline audit and disclose that the enhanced panel did not run.

Participant schedules, biographies, recording links, and session-summary links belong in a separately permissioned ResOps artifact. Never add them to the moderation guide by default.

## 3. Bound consent and privacy language

The plan or approved ResOps protocol is the only authority for recording modalities, observer disclosure, recording access, clip use, anonymity/de-identification, retention/deletion, early-exit incentives, and screen-out incentives.

- Include an explicit consent line whenever recording or live observation is planned.
- If approved language is unavailable, use `[TBD — confirm ResOps standard language]`; do not improvise a promise.
- Never claim “internal only,” “anonymous,” “identifying details removed,” “PII removed,” a deletion timeline, clip sharing, or incentive eligibility unless the source explicitly commits to it.
- Use one consent pass per format. Interview guides use their Consent table; prototype guides use the Introduction & Think-Aloud list. Do not duplicate consent.
- Diary/photo pre-work and participant artifact collection are off unless the approved plan and protocol explicitly define the collection, participant permission/consent, transfer channel, audience/access, and retention/deletion. A participant may describe an artifact without being asked to upload or show it.

## 4. Confirm destination and permissions before creation

Confirm the exact Drive folder, intended audience, and effective destination permissions before any write. Perform a fresh permissions read that covers inherited access, groups when visible, and link-sharing scope. The destination must be no broader than the approved source and study audience.

If permissions cannot be read or are broader than authorized, stop before creation. Ask for a compliant destination or separately authorized sharing change. Never silently change sharing.

In the same planned destination sequence, preauthorize exactly one partial-artifact recovery path: trash the created Doc by verified ID, or restrict and move/retitle it in an exact permission-checked quarantine folder. If neither path is authorized and supported, block before creation. Do not infer cleanup authority from permission to create the intended deliverable.

## 5. Preflight the delivery capabilities

Before creating the study Doc, verify that the connected integration can:

1. create/import one Doc in the confirmed folder;
2. return its ID, URL, active tab, raw structure, and revision;
3. apply revision-bound native batch updates;
4. re-fetch content, links, parent folder, and effective permissions;
5. export/render a PDF or thumbnail; and
6. perform the approved trash or quarantine action for a partial artifact.

A listed tool or successful sign-in does not prove these capabilities. If proof would require an unauthorized disposable write, treat the capability as unverified and block before creation.

For capability 3, name the request-body route from §2 that the run will use. Step 6 asks no questions, so when the route is the `send` helper, the researcher must already have approved it in Section 1's “Google Docs write route” pop-up. If they declined, or the route changes to `send` after Section 1, block before creation and report it.

Run `scripts/option4_guide_layout.py` in place from the installed skill. Store manifests, snapshots, and batch files in an owner-only private working directory outside every repository (for example, a fresh `mktemp -d` directory); do not copy the formatter away from its package-relative visual contract. The formatter rejects repository paths and group/world-accessible output directories, writes new JSON outputs atomically with owner-only permissions, and refuses to overwrite an existing path; use a new explicit output filename for every stage.

## 6. Create idempotently

Before creation, record the confirmed folder, exact approved title, and attempt time. If creation/import has an ambiguous result because of a timeout, disconnect, or lost response, stop and reconcile before another write:

- fetch a known document ID when one was returned; or
- search only the confirmed folder using exact title plus the attempt-time window, then inspect candidate IDs and content.

Reuse one verified match. If there is no match, more than one plausible match, or no safe inspection path, block and report the uncertainty. Never blindly retry a create.

## 7. Bind and reconcile writes

Immediately before every normalize or format write:

1. fetch fresh raw document JSON and its `revisionId`;
2. generate the batch against that snapshot;
3. bind it with `writeControl.requiredRevisionId` (the formatter requires this);
4. apply it through a protected request body, using the first available route in §2's order; and
5. re-fetch and verify the expected state.

On a revision mismatch, ambiguous response, or concurrent edit, never resend the stale batch. Re-fetch the known Doc. If the expected state already exists, record success and do not resend. Otherwise regenerate against the new revision. Reapprove material content changes; formatting-only reconciliation is allowed only when meaning and links remain unchanged.

## 8. Handle partial documents

A failed or incomplete Doc is not a deliverable. Execute only the partial-artifact recovery path preauthorized before creation: trash the verified Doc ID, or restrict and move/retitle it in the approved quarantine location. Record its ID, location, and status. If the authorized action becomes unavailable, stop and report the blocker without improvising another mutation. Never leave an unlabeled partial document in the stakeholder folder or return it as final.

After formatting, read back the content, parent folder, and effective permissions; run the visual verifier; export/render and inspect the opening page, one dense interior page, and the final page. Only then return the link.
