# Execution Plans

This folder tracks **where the project currently is**.

It is separate from `../work-packages/`:

- `work-packages/` defines what each work package requires and produces;
- `exec-plan/` records the current implementation and experimental progress while carrying out those work packages.

Use `active/` for work that is currently in progress and `completed/` for finished execution plans.

An execution plan should track:
- current state;
- completed tasks;
- unresolved questions or blockers;
- next tasks;
- relevant commits;
- experiment or result references when they exist.

Do not copy the full scientific rationale or work-package specification into an execution plan. Link to the owning documents instead.

Example (but not necessarily must follow, can adjust to project's needs):

```markdown
# WP1 Implementation Status

## Current state
Harness complete; implementing four-history replay.

## Completed
- [x] factual trajectory runner
- [x] checkpoint save/restore
- [x] G × P branching
- [ ] neutral history serializer
- [ ] compressed history serializer
- [ ] pilot launcher

## Current blocker
Neutral serializer exceeds the required token-length tolerance on some histories.

## Next
1. Fix the neutral serializer.
2. Add the invariant test.
3. Run the smoke test.
4. Launch the pilot after the smoke test passes.

## Relevant commits
- `abc123` checkpoint restore
- `def456` G × P runner
```
