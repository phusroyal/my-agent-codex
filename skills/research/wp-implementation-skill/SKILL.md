---
name: wp-implementation-skill
description: Use when implementing one approved work package in a research codebase, especially for GPU-sensitive or scale-sensitive paths. Trigger for bounded coding tasks that must stay aligned with an existing plan, produce production-grade code, use strong algorithm and data-structure choices, respect CUDA/GPU runtime realities, and add realistic behavior-first tests. Do not use for high-level planning or independent review.
---

# Work Package Implementation Skill
## Purpose
Implement exactly one approved work package with minimal blast radius.
This skill is for coding after the plan is already accepted.
The goal is not just to make the code pass tests. The goal is to produce code that is trustworthy under realistic workloads, maintainable in the repository, and appropriate for GPU-first research systems.

## Implementation stance
Implement like a production-grade GPU systems engineer.
Assume the path is GPU-first unless evidence says otherwise.
Be suspicious of:
- Python-heavy orchestration around tensor work
- unnecessary host↔device movement
- repeated tiny kernel launches
- hidden synchronization points
- poor layout/contiguity/dtype handling
- convenient but slow data structures in critical paths
- tests shaped around the code rather than the intended behavior
Passing small tests is evidence, not proof.

## When to use
Use this skill when the user asks to:
- implement WP0/WP1/etc.
- code one bounded phase from an approved plan
- add the tests/docs/config needed for one specific work package
- refine an implementation after review findings, while staying within the WP boundary
- implement a GPU-sensitive or performance-sensitive subsystem from an approved design

## When not to use
Do not use this skill for:
- making the initial architecture plan
- broad exploratory repo reading without coding
- general review or validation
- sweeping refactors outside the approved WP scope
- speculative optimization work that is not part of the approved WP

## Required inputs
Before coding, re-read:
- the approved plan
- the task or math note if relevant
- the current code paths being modified
- any existing review findings that constrain the fix
- any runtime, device, dtype, checkpoint, or validation constraints mentioned in the plan
If something important is underspecified, call it out explicitly instead of guessing silently.

## Procedure
1. Confirm the exact WP boundary.
2. Identify the minimal set of files that need to change.
3. Identify the hot path, runtime-sensitive contracts, and likely memory-sensitive surfaces.
4. Reuse or generalize existing abstractions where that improves maintainability and does not degrade runtime quality.
5. Avoid one-off wrappers unless they are clearly the cleanest option.
6. Implement the core logic with explicit attention to:
   - correctness
   - GPU/runtime quality
   - algorithm / data-structure quality
   - memory behavior
7. Add or update tests needed for the WP.
8. Update docs/config/logging only where the WP requires it.
9. Check the touched path for correctness, performance, memory, maintainability, and validation realism.
10. Summarize touched files, design choices, tests, and unresolved concerns.

## Implementation rules
- One work package only unless a tiny cross-WP change is required to unblock correctness.
- Do not silently pull future work into the current task.
- Do not import from archive/reference code.
- Prefer repository-native utilities over new special-purpose helpers.
- Make runtime assumptions explicit when touching scheduling, state, dtype, device placement, layout, checkpoint, or resume behavior.
- Optimize hot paths where relevant, but not at the expense of correctness.
- Keep new modules focused and reasonably small.

## GPU / runtime rules
Assume GPU-first execution unless evidence says otherwise.
Actively optimize for:
- device residency
- fewer launches
- less Python orchestration
- fewer unnecessary allocations/materializations
- lower sync pressure
- layout- and dtype-aware tensor flows
Be especially careful about:
- Python loops over tokens/features/contexts in hot paths
- repeated `.item()`, `.cpu()`, `.numpy()`, logging, or debug branching in performance-sensitive code
- repeated cloning, casting, concatenation, reshaping, or conversion in inner loops
- CPU-side bookkeeping that stalls or fragments throughput
- non-contiguous flows that quietly hurt performance
- hidden quadratic work that tiny tests will not reveal
If a path is intentionally CPU-side, justify why.
Choose algorithms and data structures intentionally:
- consider access patterns and real scale
- do not default to convenient but slow patterns
- prefer simpler exact code over clever brittle code
- prefer readable fast code over abstract slow code

## Testing rules
Tests must validate intended behavior, invariants, and failure modes, not merely mirror the implementation.
Prefer requirement-shaped tests over code-shaped tests.
Tests should cover, where relevant:
- primary behavior
- realistic edge cases
- malformed/adversarial cases
- device/dtype/layout/indexing-sensitive behavior
- at least one stress-oriented or scale-aware check for performance-sensitive paths when feasible
- comparison against a slower but trustworthy reference path when useful
Be suspicious of:
- tiny toy-only tests
- tests that mirror helper internals
- assertions on incidental sequencing or formatting
- heavily mocked tests with weak behavioral coverage
- tests that collaborate with the current implementation to pass
- green tests that say nothing about runtime cliffs, memory spikes, or sync-heavy behavior
Do not create tests that are only good at proving the code did what the code already does.

## Output format
Use this exact structure unless the user asks otherwise.

### Scope confirmed
### Files changed
For each file:
- what changed
- why it changed

### Main design choices
Include:
- correctness choices
- GPU/runtime choices
- algorithm / data-structure choices

### Tests added or run
Include:
- what behavior they validate
- which edge cases or stress cases they cover
- whether they exercise GPU-sensitive behavior when relevant

### Risks / unresolved concerns
### Recommended next step

## Quality bar
A good WP implementation should:
- satisfy the approved WP scope
- avoid unrelated churn
- be understandable by a later reviewer
- be appropriate for realistic GPU workloads, not just toy inputs
- use reasonable algorithms and data structures for the expected scale
- include the minimal but realistic tests and docs needed to make the change trustworthy
A strong WP implementation should also make it hard for future reviewers to say:
- the hot path is Python-shaped
- the data structures are convenient but suboptimal
- the tests only validate the implementation shape
- the code will fall over at real batch/sequence/context scale

# Build, Test, and Development Commands
Do not run commands on the login node.
Always obtain a single interactive allocation first, then run all needed commands inside that same allocated shell.
Do not use one-shot `srun ... bash -lc '...'` commands for brief inspection, testing, or development work.

### 1. Start an interactive shell
For CPU work:
` srun -p cpu --gpus=0 --pty bash -i `
For GPU work, only when the task is actually GPU-related:
` srun --gres=gpu:1 --pty bash -i `

### 2. Activate the environment inside the allocated shell
` source scripts/activate.sh `

### 3. Run commands inside that same interactive session
Examples:
- inspection
- tests
- debugging
- small scripts
- repeated iterations during development
Do not repeatedly request fresh allocations for small follow-up commands if the current interactive session is still appropriate.

### 4. Testing guidance
Use CPU tests only for genuinely CPU-only logic:
` CUDA_VISIBLE_DEVICES="" pytest ... `
For GPU-sensitive paths, prefer targeted GPU validation in addition to small CPU checks.

### 5. Close the allocation when finished
` exit `

## Execution rule
Use one interactive allocation per work chunk whenever possible.
Preferred pattern:
1. request an interactive node
2. activate the environment
3. run all related commands inside that session
4. exit when done
Avoid:
- one-shot `srun ... bash -lc '...'` commands
- repeated short allocations for closely related commands
- doing command execution directly on the login node