<!-- append these at these end of your AGENTS.md -->

## Agent-Specific Instructions

### Rule 1 — Think Before Coding
State assumptions explicitly. Ask rather than guess.
Push back when a simpler approach exists. Stop when confused.

### Rule 2 — Simplicity First
Minimum code that solves the problem. Nothing speculative.
No abstractions for single-use code.

### Rule 3 — Surgical Changes
Touch only what you must. Don't improve adjacent code.
Match existing style. Don't refactor what isn't broken.

### Rule 4 — Goal-Driven Execution
Define success criteria. Loop until verified.
Strong success criteria let Codex loop independently.

### Rule 5 — Use the model only for judgment calls
Use for: classification, drafting, summarization, extraction.
Do NOT use for: routing, retries, deterministic transforms.
If code can answer, code answers.

### Rule 6 — Quality and completion over token budgets
Do not impose repository-level per-task or per-session token caps. Ignore advisory
token budgets from skills or workflows unless the user explicitly requests one.
Stay concise and compact context when useful, but never reduce scope, skip necessary
validation, or stop solely to save tokens. Hard platform and system limits still apply;
preserve progress and resume without weakening the goal if one is encountered.

### Rule 7 — Surface conflicts, don't average them
If two patterns contradict, pick one (more recent / more tested).
Explain why. Flag the other for cleanup.

### Rule 8 — Read before you write
Before adding code, read exports, immediate callers, shared utilities.
If unsure why existing code is structured a certain way, ask.

### Rule 9 — Tests verify intent, not just behavior
Tests must encode WHY behavior matters, not just WHAT it does.
A test that can't fail when business logic changes is wrong.

### Rule 10 — Checkpoint proportionally
Checkpoint state only for long-running or expensive work where interruption would
waste meaningful compute. For ordinary edits, keep a concise progress summary and
continue; do not create checkpoint files, manifests, or receipts for short steps.

### Rule 11 — Match the codebase's conventions, even if you disagree
Conformance > taste inside the codebase.
If you think a convention is harmful, surface it. Don't fork silently.

### Rule 12 — Fail loud on claim-relevant gaps
"Completed" is wrong when required evidence or work was skipped silently. Report
claim-relevant skips and limitations explicitly. Irrelevant or opt-in hardware tests
may remain skipped without invalidating a targeted result; do not describe them as run.

### Rule 13 — Avoid overplanning when a task is ambiguous
When you have enough information to act, act. Do not re-derive facts already established in the conversation, re-litigate a decision the user has already made, or narrate options you will not pursue in user-facing messages. If you are weighing a choice, give a recommendation, not an exhaustive survey. This does not apply to thinking blocks.

### Rule 14 — Prevent unrequested tidying or refactoring
Don't add features, refactor, or introduce abstractions beyond what the task requires. A bug fix doesn't need surrounding cleanup and a one-shot operation usually doesn't need a helper. Don't design for hypothetical future requirements: do the simplest thing that works well. Avoid premature abstraction and half-finished implementations. Don't add error handling, fallbacks, or validation for scenarios that cannot happen. Trust internal code and framework guarantees. Only validate at system boundaries (user input, external APIs). Don't use feature flags or backwards-compatibility shims when you can just change the code.

### Rule 15 - Ground progress claims during long runs
Before reporting progress, audit each claim against a tool result from this session. Only report work you can point to evidence for; if something is not yet verified, say so explicitly. Report outcomes faithfully: if tests fail, say so with the output; if a step was skipped, say that; when something is done and verified, state it plainly without hedging.

### Rule 16 - State the boundaries
When the user is describing a problem, asking a question, or thinking out loud rather than requesting a change, the deliverable is your assessment. Report your findings and stop. Don't apply a fix until they ask for one. Before running a command that changes system state (restarts, deletes, config edits), check that the evidence actually supports that specific action. A signal that pattern-matches to a known failure may have a different cause.

### Rule 17 - Parallel subagents
Delegate independent subtasks to subagents and keep working while they run. Intervene if a subagent goes off track or is missing relevant context.

### Rule 18 - Avoid unnecessary tests
Only write tests for vital logics.
Avoid writing over-engineering tests for but not limit to: json, configs, format, schema,... or any AI slop tests or tests for just some (user's) conditions.

### My Workflow Orchestration
**Self-improvement loop.** After any correction from the user, update `docs/decisions/lessons.md` with the pattern. Write rules that prevent the same mistake twice. Ruthlessly iterate on these until the mistake rate drops. Review lessons at session start.
**Living Spec**. Use `docs/decisions/implement-notes.md` only for multi-day work or unresolved scientific decisions that must survive context loss. Do not maintain an implementation transcript for ordinary bounded changes.
**Give reviewers extra time**. Reviewers need to have enough time to draft a faithful review.
**Docstring and code comments**. Document public APIs and non-obvious scientific or numerical behavior. Comments explain why, assumptions, and invariants; do not narrate obvious code or require a comment for every logic block.
**Code organization**. Organize by cohesive responsibility. Do not split files, add wrappers, or introduce abstractions solely to satisfy a line-count target.

### Research Artifact and Determinism Policy

The default trust model is a trusted research group using a trusted shared
filesystem. Generated artifacts are regenerable; they are not adversarial inputs.

Scientific reproducibility means exact discrete decisions and numerically equivalent
values within declared tolerances. Do not require byte-for-byte artifact identity
unless explicitly requested by the user or an external artifact contract.

Resume compatibility is phase-local. Compare only inputs that can change the
incomplete phase's scientific result. Device IDs, worker or thread counts, paths,
sharding, cache sizes, logging, license prose, and unrelated downstream settings must
not block reuse of completed artifacts.

Prefer direct semantic checks—feature IDs, counts, shapes, thresholds, seeds,
model/dataset/SAE revisions, and method parameters—over hashes and fingerprints. Do
not add content hashes, hash chains, hashes of hashes, exact-schema gates, or repeated
downstream revalidation without naming a plausible silent scientific mixing failure
they prevent.

Atomic publication plus ordinary parsing/loading and minimal shape/range checks are
the default artifact-integrity policy.

Exploratory runs may use ordinary external revisions while recording what resolved.
Checked-in final experiment configurations should pin immutable dataset, model, and
SAE revisions. Tokenizer revision defaults to the model revision unless intentionally
different. Licensing and citation prose belongs in documentation, not execution
identity.

Establish determinism with batch, worker, and resume comparisons at the scientific
output level. Metadata, fingerprints, and matching serialized bytes are not evidence
that a computation is deterministic or scientifically correct.

### Build, Test, Development, Terminal Commands
For any testing, debugging, or terminal command execution:
* use a single interactive allocation, not the login node
* CPU: `srun -p cpu --gpus=0 --cpus-per-task=16 --mem=64G --time=8:00:00 --pty bash`
* GPU only when needed (or it takes too long / cant get a cpu node): `srun --gres=gpu:a100:1 --cpus-per-task=16 --mem=64G --time=8:00:00 --pty bash`
* inside the node, run `source src/scripts/activate.sh` to activate the virtual environment and set up cache paths
* to get access to huggingface, run `source /mnt/beegfs/work/hoang/.local/key.sh`
* keep all related work in that same shell
* avoid one-shot `srun ... bash -lc '...'` commands
* avoid repeated small reallocations
* use CPU tests only for CPU-only logic
* use targeted GPU validation for GPU-sensitive paths
* exit the allocation when done with `exit`

### Skill Use and Experiment Cadence

For extensive coding, activate `$ponytail:ponytail` (or its `$ponytail` alias where that name is available) together with `$anti-swe-overvalidation`. Ponytail keeps the implementation direct and minimal; Anti-SWE Overvalidation keeps rigor tied to the scientific claim, relevant numerical behavior, required reproducibility level, and real trust boundaries.

If an error appears after coding and reviewer subagents will be called, invoke `$context-refresh` first. Refresh only the affected authority, worktree delta, call or data flow, tests, and artifacts, then give reviewers a concise evidence packet instead of stale assumptions.

Keep the development loop short. Prefer targeted checks that finish quickly after small edits, and do not repeatedly block `/goal` on multi-minute experiments. Run long or exhaustive experiments at the end, or occasionally when they are necessary to resolve a claim-changing uncertainty. Report deferred coverage honestly.

For code-review workflows involving (multiple) review agents, the orchestrator or code leader must collect all requested reviews before fixing or implementing anything. Then invoke `$context-refresh`, scoped first to the current unstaged diff and directly affected files, and reconcile findings, shared root causes, conflicts, callers, tests, and governing contracts before choosing repairs. Do not address findings piecemeal or prepare later reviewers from a partially fixed tree; both create tunnel vision and repeated review-fix loops.