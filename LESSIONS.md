# Lessons

- At session start, check the repo-root `LESSIONS.md`; do not assume the lessons file lives under `tasks/` or uses different casing.
- Before running repo commands or tests, read `AGENTS.md` and follow the repo flow.
- Never run commands on the login node.
- Narrow exception: read-only commands that only inspect local Codex skill `.md` files or agent `.toml` files may run outside the Slurm allocation, including on the login node, when those paths are unavailable on compute nodes. Keep that exception to simple path/file reads only, never repo work or mutating commands.
- For that narrow login-node exception, prefer a plain non-login shell; login-shell init can touch Slurm state and pollute otherwise simple read-only output.
- If command execution is needed, obtain exactly one interactive allocation at the beginning of the session and run subsequent shell work inside that same allocation:
  - CPU work: `srun -p cpu --gpus=0 --pty bash -i`
  - GPU work only when genuinely required: `srun --gres=gpu:1 --pty bash -i`
- Immediately after entering the allocated bash shell, run `source scripts/activate.sh` before any repo commands so the environment is active from the start of the session.
- Do not use one-shot `srun ... bash -lc '...'` commands; reuse the same interactive allocation for subsequent commands in that session.
- If an interactive allocation needs to be replaced, explicitly `exit` the old shell before opening the new one; do not leave stale CPU/GPU sessions behind after interrupted runs.
- After finishing shell-based inspection, testing, or data pulls, explicitly `exit` the interactive allocation in the same turn; do not rely on the user to clean up stale bash sessions.
- Inside the allocated node, source `scripts/activate.sh` when the command actually needs the repo environment, such as `pytest` or training entrypoints.
- Use CPU tests only for genuinely CPU-only logic, for example `CUDA_VISIBLE_DEVICES="" pytest ...`.
- For GPU-sensitive paths, prefer targeted GPU validation in addition to small CPU checks.
- Only request a GPU node for genuinely GPU-related work, and close the interactive shell with `exit` as soon as the needed work is done.
- If the user has already pre-authorized CPU/GPU use for the session, allocate it when needed without asking again; still keep the allocation scoped and short-lived.
- Prefer `rg` for file and text search when it is available.
- Try to reuse existing subagents for the same task thread instead of spawning new ones repeatedly; keep context warm and avoid duplicate review/planning threads unless the task is genuinely different. If a new subagent is needed, close the most related existing one first before spawning the replacement.

- If a work package promises concrete output artifacts, implement the runner or writer that materializes them in the same phase; helper-only code is incomplete even if the helpers are individually tested.
- Validation guardrails should fail closed: if an audit, exactness check, or reconstruction path validates zero examples, report failure instead of silently passing.
- For fidelity-critical audit or reconstruction paths, do not add approximate or convenience fallbacks that silently keep the run alive; if the exact contract cannot be met, fail closed with a clear error.
- When a report or cohort definition depends on run-level validity, such as a passed replay audit, enforce that rule in the reported cohort counts themselves, not only in a separate warning flag.
- Reproducibility snapshots must record the actually resolved runtime choices after overrides are applied, and may include checkpoint defaults separately for provenance.
- Offline artifact or checkpoint loaders should include small, targeted compatibility shims for retired config blocks when older checkpoints still need to be analyzed; do not assume every historical checkpoint matches the current schema.
- When the user explicitly asks for an upgrade rather than legacy compatibility, do not preserve the old behavior behind fallback modes or compatibility flags; implement the new contract directly and update the affected tests and docs.

- If an offline comparison harness exposes a padding, hook, target-position, or similar contract bug, audit the shared or live training path for the same assumption in parallel and patch it there too if it exists.
- When buffered capture rows are partitioned across active and storage subsets, assign each capture entry a single owner before emit logic runs; otherwise one context can straddle both subsets, be emitted twice, and silently break first-eligible capture semantics.
- Deferring `PendingContextSample` creation is not enough if a helper still slices or CPU-materializes replay rows early; for exact capture-start contracts, replay-row materialization and CPU handoff must happen only at the acceptance boundary.
- If FERS logs stop at the last pre-warmup step, do not assume the run is stuck there or keep iterating on config blindly; first inspect the control flow around `tokens_seen` updates and FERS logging, because the first post-warmup batch can be hidden when `maybe_run_fers_update(...)` blocks before metrics are emitted.

- When reusing a shared math helper in new validation code, match its actual return signature instead of assuming it mirrors a nearby helper; `GramMatrixCache.normalize(...)` returns `(directions, norms)`, unlike local row-normalization helpers that also return a mask.
- When a shared adapter API exposes a tensor via a property such as `unembedding_weight`, do not hard-code method-call syntax in new comparison helpers; normalize property-vs-callable access once so the real adapter and lightweight test doubles both work.

- File and test names should describe the behavior or artifact under test; avoid generic `wp*` names that do not help future readers understand intent.
- Tests must be requirement-shaped, not code-shaped.
- Do not write unrealistic toy tests that only satisfy the current implementation.
- Cover real behavior, realistic edge cases, malformed or adversarial cases when relevant, and stress or scale-aware scenarios for hot paths.
- For GPU- or tensor-sensitive logic, include realistic device, dtype, layout, indexing, and contract-sensitive cases where relevant.

## Investigation discipline

- Do not jump to a high-level conclusion first when a run regresses. Before blaming the math, method, or abstract policy, inspect the concrete code path and look for bad implementations or failing logic in the live path: sampling weights, prefilters, readiness gates, post-sampling partition, assignment logic, and window-commit/update behavior.
- When delegating after diagnosing an implementation-level bug, preserve that framing in the subagent brief. Do not silently escalate an implementation/scheduler bug into “change the math” or “change the method” unless that escalation is explicitly justified and confirmed first.
- When the user asks for a minimal live regression fix, do not change the underlying sampling or math contract without explicit approval. First exhaust narrower scheduler/control-path fixes, and if the remaining fix requires changing the method law itself, stop and surface that tradeoff before editing.
- In this repo, do not use `exec_command` on the login node for file reads/diffs once the workflow requires interactive allocations. Stay inside the active compute allocation for shell work.
