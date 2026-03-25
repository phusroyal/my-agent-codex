# Repository Guidelines

## What is this project about?
We train SAE:
- read `tasks/sae_training/plan.md` for how we train it
We fine-tune SAE:
- idea: `tasks/vjp_fers/VJP - FERS.md`
- implementation: `tasks/vjp_fers/plan.md`
- write-up: `tasks/vjp_fers/FESA.pdf`
Irrelevant things:
- folders in `archive/` is just reference, we can inherit their logic but we MUST NOT USE THEM (call any function from them)

## Workflow Orchestration
**Plan mode by default.** Enter plan mode for any non-trivial task (3+ steps or architectural decisions). If something goes sideways, stop and re-plan immediately — don't keep pushing. Use plan mode for verification steps, not just building. Write detailed specs upfront to reduce ambiguity.
**Subagent strategy.** Use subagents liberally to keep your main context window clean. Offload research, exploration, and parallel analysis. For complex problems, throw more compute at it. One task per subagent for focused execution.
**Self-improvement loop.** After any correction from the user, update `LESSIONS.md` with the pattern. Write rules that prevent the same mistake twice. Ruthlessly iterate on these until the mistake rate drops. Review lessons at session start.
**Demand elegance (balanced).**
- For non-trivial changes, pause and ask "is there a more elegant way?" If a fix feels hacky: "Knowing everything I know now, implement the elegant solution." Skip this for simple, obvious fixes - don't over-engineer.
- Try to reuse functions, class,... that are already there when possible. If functions, class,... that are similar for your use case, do not create new ones for that use case only (or wrapper of them) you can edit the existing ones so the codebase easier to maintain.

**Core Principles**
- Simplicity first — make every change as simple as possible. Minimal code impact.
- No laziness — find root causes. No temporary fixes. Senior developer standards.
- Minimal blast radius — only touch what's necessary. Don't introduce new bugs.

## Build, Test, and Development Commands
Never run commands on the login node.
Exception:
- Read-only inspection commands for local Codex skill `.md` files and agent `.toml` files may run outside the Slurm allocation, including on the login node, if those paths are only available there.
- Keep this exception narrow: use it only for simple reads such as `cat`, `sed`, `ls`, or equivalent path inspection.
- When using this exception, prefer a plain non-login shell so login-shell init does not trigger Slurm-related startup noise or other unrelated side effects.
- Do not use this exception for repository files, tests, training commands, writes, installs, or any command that mutates state or touches cluster resources.
If command execution is needed, first obtain exactly one interactive allocation and do all shell work inside that same allocation:
1. CPU work: `srun -p cpu --gpus=0 --pty bash -i`
2. GPU work only when genuinely required: `srun --gres=gpu:1 --pty bash -i`
3. Do not use one-shot `srun ... bash -lc '...'` commands; reuse the same interactive allocation for subsequent commands in that session.
4. After entering the allocated node, activate the environment (so you can use rg): `source scripts/activate.sh`
5. Run CPU tests only for genuinely CPU-only logic: `CUDA_VISIBLE_DEVICES="" pytest ...`
6. For GPU-sensitive paths, prefer targeted GPU validation in addition to small CPU checks.
7. When finished, close the allocation with `exit`.
