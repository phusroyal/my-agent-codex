---
name: research-plan-skill
description: Use when the task is to turn motivation docs, existing plans, and current repository state into a concrete research-engineering design or work-package plan. Best for planning, architecture scoping, work-package decomposition, and risk surfacing, especially when speed, memory, reproducibility, or mathematically sensitive logic matter. Prefer this skill when brainstorming implementation strategies and exploring multiple viable designs before coding. Do not use for direct coding, narrow bug-only fixes, or final review.
---

# Research Plan Skill

## Purpose

Produce a design or execution plan that a later coding agent can follow reliably.

This skill is for research-engineering tasks where the work has mathematical intent, runtime constraints, scaling concerns, reproducibility requirements, or non-trivial repository integration.

This skill should not only make a safe plan. It should also help generate strong implementation ideas. When appropriate, it should brainstorm multiple plausible designs, compare them, and then converge on the most practical option for this repository.

## Planning stance

Plan with two goals at the same time:

1. **Be implementation-ready**
   - The result should be specific enough that a later coding agent can execute without guessing.

2. **Be creatively useful**
   - Explore better-than-obvious approaches when they could materially improve speed, memory, simplicity, or extensibility.

Creativity here does **not** mean novelty for its own sake. It means searching for cleaner decompositions, cheaper runtime paths, better reuse opportunities, more robust state handling, and more scalable experiment structure.

## Optimization bias

When brainstorming or comparing options, explicitly optimize for:

- **Speed**
  - reduce repeated computation
  - avoid redundant passes
  - exploit batching, caching, reuse, or amortization when safe
  - keep hot paths small and explicit

- **Memory**
  - avoid unnecessary retained tensors or state
  - prefer streaming, chunking, or bounded buffers where appropriate
  - call out peak-memory risks, not just steady-state usage
  - identify serialization/checkpoint size concerns early

- **Correctness**
  - preserve mathematical intent
  - make indexing, masking, scheduling, and persistence contracts explicit
  - distinguish exact behavior from approximation

- **Maintainability**
  - prefer repo-native extensions over one-off branches of logic
  - reuse existing abstractions when they genuinely help
  - avoid clever designs that will be painful to debug later

When there is tension between these goals, state the tradeoff clearly.

## When to use

Use this skill when the user asks to:
- make a design document
- draft a plan or work packages
- turn motivation docs into an implementation roadmap
- reconcile repo state with a research idea before coding
- identify likely touched files, risks, and acceptance criteria
- compare several implementation directions before choosing one

Use this skill when the task involves any of:
- more than 3 meaningful steps
- architecture or interface choices
- performance or memory-sensitive design
- reproducibility, checkpoint, or resume behavior
- correctness-sensitive math, indexing, or scheduling logic
- touching multiple modules or subsystems
- uncertainty about the best decomposition or execution path

## When not to use

Do not use this skill for:
- straightforward local bug fixes
- implementing an already-approved WP
- final code review
- simple documentation-only edits
- tiny refactors with no real planning component

## Required inputs

Before planning, gather:
- the main task or motivation doc
- relevant existing plans, notes, or prior alignment docs
- the current repo surfaces that would be touched
- any explicit constraints from the user
- any known performance, memory, reproducibility, or compatibility constraints

If some of this is missing:
- state what is missing
- proceed from confirmed evidence only
- distinguish hard facts from inferred assumptions

## Procedure

1. Restate the goal in repository terms.
2. Separate:
   - constraints
   - assumptions
   - non-goals
3. Identify the minimal architecture or change surface needed.
4. Map likely touched files or subsystems.
5. Brainstorm 2-4 plausible implementation directions when design choice matters.
6. Compare those directions on:
   - speed
   - memory
   - correctness risk
   - maintainability
   - compatibility with the current repo
7. Choose a preferred direction and explain why.
8. Break the work into a small number of work packages.
9. For each WP, define:
   - goal
   - outputs/artifacts
   - concrete TODOs
   - main risks
   - acceptance checks
10. Call out ambiguities that would force later agents to guess.
11. Surface performance, memory, correctness, reproducibility, and integration risks.
12. Prefer maintainable repo-native changes over greenfield rewrites.

## Brainstorming rules

Use brainstorming only where it adds value.

Good times to brainstorm:
- there are multiple reasonable designs
- the obvious design may be too slow or memory-heavy
- the repo already has abstractions that could be reused in different ways
- there is a risk of over-specializing to one experiment
- runtime contracts are unclear and need a better decomposition

When brainstorming:
- generate a few concrete options, not a long vague list
- favor options with explicit hot-path reasoning
- include at least one conservative option
- include a more ambitious option only if it has a realistic path in this repo
- reject options that are elegant on paper but hard to validate or maintain

## Planning rules

- Prefer 3-5 work packages unless the task is truly smaller.
- Keep WPs bounded and implementation-friendly.
- Do not make later coding agents infer hidden runtime contracts.
- Explicitly specify state ownership, scheduling units, persistence, validation expectations, and failure modes when relevant.
- Prefer generic reusable surfaces over experiment-specific naming debt.
- Keep new modules focused and reasonably small.
- Archive code may be read as reference only; do not depend on it at runtime.
- When performance matters, identify the likely hot path and design around it.
- When memory matters, identify both retained-state growth and peak allocation risks.
- When proposing an optimization, state whether it is:
  - exact
  - equivalent by construction
  - an approximation
  - a future optimization idea only

## Output format

Use this exact structure unless the user asks otherwise.

### Goal

### Constraints and assumptions

### Non-goals

### Relevant repo surfaces

### Design options considered
For each option include:
- Core idea
- Pros
- Cons
- Speed / memory implications
- Why it does or does not fit this repo

### Preferred architecture proposal

### Work packages
For each WP include:
- Goal
- Outputs / artifacts
- TODOs
- Risks
- Acceptance checks

### Open questions

### Recommended next step

## Quality bar

A good plan should let a future coding agent start work without guessing about:
- what to build
- where to build it
- what must remain unchanged
- which option was chosen and why
- where the hot path is
- what the main memory risks are
- how success will be checked

A strong plan should also make it clear that alternative ideas were considered, and that the chosen design is not just safe but practical for real experiment-scale execution.