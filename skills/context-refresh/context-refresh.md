---
name: context-refresh
description: "[OMX] Refresh broad repository context within existing authority and scope before difficult reasoning, delegation, or review"
argument-hint: "<task|problem|review scope>"
---

# Context Refresh — Bounded Brownfield Reorientation

Use this skill to deliberately replace accumulated assumptions with fresh repository evidence. It is a **read-only preparatory helper**, not an execution mode: it produces a concise context packet for the leader, subagents, or reviewers, then stops.

## Activate When

- a long goal or several work packages have made the leader's context stale
- a difficult problem, blocker, repair, or brainstorming session depends on cross-file behavior
- delegation needs a clean, bounded packet rather than inherited conversation history
- review needs the current worktree, governing contract, and affected behavior reconciled first
- repeated failures suggest that a local assumption, caller, artifact, config, or package boundary was missed

## Do Not Activate When

- a simple fact can be answered from one known file
- the relevant context was just refreshed and no material repository state changed
- the downstream workflow already has fresh, sufficient context and a refresh would not change its framing
- “more context” would only add unrelated files or polish an already-grounded answer

## Non-Negotiable Boundaries

- Broad reading expands **evidence**, never authority or edit scope.
- Governing user instructions, applicable `AGENTS.md`, approved plans, and controlling paper, PRD, or spec artifacts remain hard boundaries.
- Do not invent science, requirements, acceptance criteria, fallbacks, or authority from repository patterns.
- Treat worktree state and `HEAD` as distinct evidence. Do not mistake existing, staged, untracked, or unrelated changes for the current task's work.
- Label material conclusions as **Evidence**, **Inference**, or **Unknown**. Never promote an inference because it is convenient.
- Do not edit files, mutate workflow state, launch execution, fix findings, or silently broaden the task. Context refresh prepares the next lane; it does not perform it.

## Concentric Context Rings

Read outward only until the next decision is grounded:

1. **Authority ring** — current request, success criteria, non-goals, applicable instructions, approved plans, paper, PRD, and specs.
2. **Delta ring** — `git status`, changed/untracked paths, rename state, and the worktree diff against `HEAD`; separate current-task changes from pre-existing work.
3. **Local behavior ring** — touched exports, immediate callers, dependencies, shared utilities, types, and nearby tests.
4. **Lifecycle ring** — trace producers → transformations → consumers, including configs, runners, serialization, logs, generated artifacts, and realistic tests.
5. **Boundary ring** — entry points, orchestrators, package/install boundaries, external copies or patches, public APIs, docs, and downstream consumers.

Do not scan the whole repository by default. Expand a ring only to resolve a named unknown, conflict, or decision.

## Workflow

1. **Freeze the task capsule.** Record the target result, allowed scope, hard boundaries, known evidence, open questions, and stop condition before reading broadly.
2. **Establish the baseline.** Compare the current worktree with `HEAD`, including staged, unstaged, untracked, deleted, and renamed paths. Note unrelated changes without absorbing them.
3. **Walk the rings.** Start with governing artifacts and the changed surface, then follow symbols and data flow outward only where the task requires it.
4. **Trace end to end.** For each relevant behavior, identify callers, producers, consumers, configs, tests, logs, artifacts, and package boundaries. Prefer direct references over architectural guesses.
5. **Reconcile conflicts.** State doc/code, plan/worktree, test/implementation, or artifact/provenance conflicts explicitly. Follow the governing authority; do not average contradictory sources.
6. **Classify findings.** Separate direct evidence, supported inference, and unresolved unknowns. Identify which unknowns actually block the next lane.
7. **Build prompt-safe packets.** Give each subagent or reviewer only its objective, scope, governing boundaries, starting evidence, required artifacts, deliverable, and stop rule. Reference full sources instead of forwarding oversized raw context.
8. **Hand off and stop.** Route unresolved requirements to clarification, architecture/test-shape decisions to planning, external current-practice questions to bounded research, execution to the implementation lane, and merge-readiness judgments to independent review.

## Output Contract

```md
## Context Refresh: <task>

### Task Capsule
- Target result:
- In scope / out of scope:
- Governing boundaries:
- Stop condition:

### Worktree vs HEAD
- Relevant changes:
- Pre-existing or unrelated changes:
- Baseline caveats:

### Trace Map
- Entry/caller → producer → transformation → consumer:
- Config/test/log/artifact/package boundaries:

### Evidence
- `path/to/file:line-line` — what it directly establishes

### Inference
- conclusion — evidence supporting it and confidence

### Unknowns / Conflicts
- unresolved item — why it matters and the smallest next probe

### Context Packet for <leader|agent|reviewer>
- Objective:
- Scope and non-goals:
- Governing sources:
- Starting files/artifacts:
- Required deliverable:
- Stop/escalation rule:
```

Keep the packet concise, task-specific, and independently usable. A reviewer packet must include the review scope, relevant diff against `HEAD`, governing plan/spec, validation evidence, and unresolved risks. A subagent packet must not delegate broader authority than the leader has.

## Stop Rules

- Stop when the next problem-solving, delegation, or review decision is grounded by sufficient fresh evidence.
- Stop at an authority or requirements ambiguity; report it as an unknown rather than guessing.
- Stop expanding when another context ring would not change the decision.
- If context is oversized, preserve goals, constraints, non-goals, decision boundaries, evidence references, and unknowns in a prompt-safe summary; do not forward a raw dump.
- If validation or external evidence is still needed, name the exact next lane or probe. Do not perform that downstream work under this helper.
- Never treat context refresh as approval, implementation, review, or permission to edit.

Task: {{ARGUMENTS}}
