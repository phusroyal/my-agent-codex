---
name: research-plan-skill
description: Use when the task is to turn motivation docs, existing plans, and current repository state into a concrete research-engineering design or work-package plan. Best for GPU-first planning, architecture scoping, work-package decomposition, systems-risk surfacing, and implementation brainstorming when correctness, speed, memory, reproducibility, or mathematically sensitive logic matter. Prefer this skill when exploring multiple viable designs before coding, especially for CUDA/GPU-sensitive paths. Do not use for direct coding, narrow bug-only fixes, or final review.
---

# Research Plan Skill
## Purpose
Produce a design or execution plan that a later coding agent can follow reliably.
This skill is for research-engineering tasks where the work has mathematical intent, runtime constraints, GPU systems concerns, scaling risks, reproducibility requirements, or non-trivial repository integration.
This skill should not only make a safe plan. It should also help generate strong implementation ideas. When appropriate, it should brainstorm a small number of realistic designs, compare them, and converge on the most practical option for this repository and workload.

## Planning stance
Plan with three goals at the same time:
1. **Be implementation-ready**
   - The result should be specific enough that a later coding agent can execute without guessing.
2. **Be creatively useful**
   - Explore better-than-obvious approaches when they could materially improve speed, memory, simplicity, robustness, or extensibility.
3. **Be production-realistic**
   - Favor designs that will hold up under real GPU workloads, not just pass small tests or look elegant on paper.
Creativity here does **not** mean novelty for its own sake. It means searching for cleaner decompositions, cheaper runtime paths, better reuse opportunities, stronger runtime contracts, and more scalable experiment structure.

## System bias: GPU-first by default
Assume the target system is GPU-first unless evidence says otherwise.
That means planning should explicitly reason about:
- whether data stays resident on device
- host↔device transfer frequency and size
- kernel launch count and launch fragmentation
- memory bandwidth vs compute bottlenecks
- tensor layout, contiguity, and dtype choices
- repeated Python-side orchestration around tensor work
- avoidable synchronization points
- retained-state growth, replay growth, and checkpoint size
- real scaling with sequence length, feature count, contexts, batch size, and replay size
Do not accept CPU-shaped designs for GPU-sensitive paths without explicit justification.

## Optimization bias
When brainstorming or comparing options, explicitly optimize for:

### Correctness
- preserve mathematical intent
- make indexing, masking, scheduling, layout, persistence, and resume contracts explicit
- distinguish exact behavior from approximation
- call out failure modes that would silently corrupt experiments

### GPU / runtime quality
- reduce repeated computation
- avoid repeated small kernel launches when batching/fusion is feasible
- minimize host↔device movement
- reduce unnecessary synchronization
- keep hot paths tensorized, explicit, and throughput-friendly
- avoid Python-heavy inner loops around tensor work

### Memory quality
- avoid unnecessary retained tensors or state
- prefer streaming, chunking, bounded buffers, or amortization where appropriate
- call out peak-memory risks, not just steady-state usage
- identify serialization and checkpoint-size concerns early

### Algorithm / data-structure quality
- choose data structures intentionally for scale and access patterns
- avoid convenient but slow patterns in critical paths
- think about asymptotic cost and constant factors
- call out where the design may become launch-bound, memory-bound, or Python-bound

### Maintainability
- prefer repo-native extensions over one-off branches of logic
- reuse existing abstractions when they genuinely help
- avoid clever designs that are painful to debug or validate later
When there is tension between these goals, state the tradeoff clearly.

## When to use
Use this skill when the user asks to:
- make a design document
- draft a plan or work packages
- turn motivation docs into an implementation roadmap
- reconcile repo state with a research idea before coding
- identify likely touched files, risks, and acceptance criteria
- compare several implementation directions before choosing one
- plan a GPU-sensitive or scale-sensitive subsystem
Use this skill when the task involves any of:
- more than 3 meaningful steps
- architecture or interface choices
- performance, memory, or GPU-sensitive design
- reproducibility, checkpoint, or resume behavior
- correctness-sensitive math, indexing, masking, or scheduling logic
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
- any known performance, memory, reproducibility, compatibility, or device/runtime constraints
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
5. Identify likely hot paths, memory hotspots, and runtime-sensitive contracts.
6. Brainstorm 2-4 plausible implementation directions when design choice matters.
7. Compare those directions on:
   - correctness
   - GPU/runtime quality
   - memory behavior
   - algorithm / data-structure quality
   - maintainability
   - compatibility with the current repo
   - realism of the validation plan
8. Choose a preferred direction and explain why.
9. Break the work into a small number of work packages.
10. For each WP, define:
   - goal
   - outputs/artifacts
   - concrete TODOs
   - main risks
   - acceptance checks
11. Call out ambiguities that would force later agents to guess.
12. Surface performance, memory, correctness, reproducibility, integration, and validation risks.
13. Prefer maintainable repo-native changes over greenfield rewrites.

## Brainstorming rules
Use brainstorming only where it adds value.
Good times to brainstorm:
- there are multiple reasonable designs
- the obvious design may be too slow, too memory-heavy, too Python-heavy, or too GPU-unfriendly
- the repo already has abstractions that could be reused in different ways
- there is a risk of over-specializing to one experiment
- runtime contracts are unclear and need a better decomposition
- the validation plan is weak and needs a more realistic testing strategy
When brainstorming:
- generate a few concrete options, not a long vague list
- favor options with explicit hot-path reasoning
- include at least one conservative option
- include a more ambitious option only if it has a realistic path in this repo
- reject options that are elegant on paper but hard to validate, scale, or maintain
- explicitly say if an option is likely Python-bound, launch-bound, memory-bound, or sync-heavy

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
- If a design is GPU-sensitive, explicitly state:
  - what lives on GPU vs CPU
  - where synchronization may happen
  - what the likely bottleneck class is
  - what tests are needed to validate realistic behavior
- Prefer requirement-shaped validation plans over code-shaped tests.

## Test-planning rules
A planning skill must prevent weak tests from being baked into the design.
When defining acceptance checks:
- test intended behavior and invariants, not helper internals
- include realistic edge cases
- include malformed/adversarial cases where relevant
- include device/dtype/layout/indexing cases when the path is tensor- or GPU-sensitive
- include at least one stress-oriented or scale-aware check for performance-sensitive paths when feasible
- avoid tiny toy-only tests that can pass while real workloads fail
- where useful, compare against a slower but trustworthy reference path
Be suspicious of:
- tests that mirror implementation structure
- assertions on incidental internal sequencing
- heavily mocked tests with little behavioral coverage
- validations that prove semantics on tiny inputs but say nothing about scaling, sync, or memory cliffs

## Output format
Use this exact structure unless the user asks otherwise.

### Goal
### Constraints and assumptions
### Non-goals
### Relevant repo surfaces
### Hot paths and runtime-sensitive contracts
### Design options considered
For each option include:
- Core idea
- Pros
- Cons
- GPU/runtime implications
- Memory implications
- Algorithm / data-structure implications
- Validation implications
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
- what the main memory and GPU risks are
- what data structures and runtime contracts matter
- how success will be checked
A strong plan should also make it clear that:
- alternative ideas were considered
- the chosen design is practical at real experiment scale
- the validation strategy checks real behavior, realistic edge cases, and likely failure modes rather than merely matching the code shape