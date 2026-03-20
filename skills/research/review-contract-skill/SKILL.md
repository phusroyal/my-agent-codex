---
name: review-contract-skill
description: Use when reviewing or validating an implementation against an approved plan or acceptance criteria. Best for GPU-first production-grade review: functionality, completeness, runtime realism, algorithm/data-structure quality, hotspot analysis, realistic tests, edge cases, documentation/tests audit, and PASS-or-REVISE validation. Do not use for initial planning or direct implementation.
---

# Review Contract Skill

## Purpose

Review an implementation against its intended contract.

This skill supports both broad code review and strict completion validation.

The goal is not just to check whether code looks reasonable or whether tests pass. The goal is to decide whether the implementation is trustworthy for real workloads, especially GPU-sensitive or scale-sensitive paths.

## Review stance

Review like a production-grade GPU systems gate.

Assume the implementation may:
- pass toy tests but fail at realistic scale
- be semantically correct but operationally poor
- hide Python hotspots, sync points, or host-device transfers
- have tests shaped around the code rather than the real requirement

Be strict. Passing tests is evidence, not proof.

## When to use

Use this skill when the user asks to:
- review a completed WP
- check whether implementation matches the plan
- look for major or critical issues
- audit tests and docs
- decide PASS or REVISE
- check whether a performance-sensitive or GPU-sensitive path is actually ready

## When not to use

Do not use this skill for:
- generating the first plan
- exploratory repo reading before scope is understood
- implementing code changes directly
- broad architecture brainstorming before a concrete contract exists

## Review dimensions

Always check these dimensions unless the user narrows scope.

### 1. Functionality
- Is the code likely correct on the intended path?
- Are indexing, masking, scheduling, shape, dtype, and state semantics correct?
- Are edge cases and failure modes handled explicitly?

### 2. Completeness
- Is the requested phase actually done?
- Are all promised artifacts, configs, tests, docs, and validation surfaces present?
- Is the implementation genuinely complete, or merely plausible-looking?

### 3. GPU / runtime realism
Assume GPU-first execution unless evidence says otherwise.
Check:
- unnecessary host↔device movement
- hidden synchronization points
- Python-heavy control flow in hot paths
- repeated tiny kernel launches
- repeated allocation, cloning, conversion, or materialization
- poor device/dtype/layout/contiguity handling
- paths that are likely memory-bound, launch-bound, sync-heavy, or Python-bound

### 4. Algorithm / data-structure quality
- Are the algorithm and asymptotics appropriate for real workloads?
- Are data structures chosen intentionally for access pattern and scale?
- Is there hidden quadratic or worse behavior masked by tiny tests?
- Is the code using convenient but slow patterns in critical paths?

### 5. Consistency and maintainability
- Does it fit existing abstractions and repo conventions?
- Is there unnecessary complexity, duplication, or one-off logic?
- Is the design easy to extend and debug later?

### 6. Guesswork and hidden assumptions
- Does the implementation rely on unverified assumptions?
- Are runtime contracts explicit?
- Are resume/checkpoint/logging/config expectations satisfied when relevant?

### 7. Documentation
- Do comments/docs/config descriptions match reality?
- Are constraints, caveats, and behavior explained where needed?

### 8. Testing quality and realism
Tests must validate the intended behavior, not merely the current implementation shape.

Check:
- primary behavior coverage
- realistic edge cases
- malformed/adversarial cases where relevant
- realistic device/dtype/layout/indexing coverage for tensor/GPU-sensitive code
- stress-oriented or scale-aware checks for performance-sensitive paths when feasible
- whether tests compare against a trustworthy reference path when helpful

Be especially suspicious of:
- tiny toy-only tests
- tests that mirror helper internals
- assertions on incidental sequencing or formatting
- heavily mocked tests with weak behavioral coverage
- tests that collaborate with the implementation to pass
- “green” tests that say nothing about runtime cliffs, sync costs, or memory spikes

## Procedure

1. Re-read the approved plan or acceptance criteria.
2. Inspect the implementation with the contract in mind.
3. Identify the intended hot paths and runtime-sensitive surfaces.
4. Separate major issues from medium issues.
5. Distinguish true blockers from nice-to-have improvements.
6. Check whether tests and docs actually support the implementation claims.
7. Decide whether the work should PASS or REVISE.
8. Give the minimal next actions needed to reach PASS.

## Review rules

- Prioritize correctness and completeness over style nits.
- Do not approve work that is only “almost done.”
- Do not approve work whose tests are too code-oriented or unrealistic.
- Be explicit when evidence is weak.
- Prefer concrete failure modes over vague discomfort.
- If the code differs from the plan, say whether the deviation is justified or risky.
- Be skeptical of implementations that look clean but are operationally poor.
- For GPU-sensitive code, do not treat CPU-shaped validation as sufficient evidence.

## Output format

Use this exact structure unless the user asks otherwise.

### Verdict
PASS or REVISE

### Major findings

### Medium findings

### GPU / runtime / scaling findings

### Algorithm / data-structure findings

### Missing tests or docs

### Mismatch with approved plan

### Minimal next actions

### Most likely code review flags

## Quality bar

A good review should help the next agent know exactly:
- what is wrong
- how serious it is
- whether it is a correctness issue, runtime issue, validation issue, or completeness issue
- what must be fixed before moving on

A strong review should also make clear:
- whether the code is trustworthy under realistic workloads
- whether the tests prove the intended behavior instead of mirroring the implementation
- whether the hot path is production-grade or only toy-grade

# Build, Test, and Development Commands

Do not run commands on the login node.
Get either a CPU or GPU interactive node first.

1. CPU interactive bash:
   `srun --pty bash -i`
   Or one-shot `srun -p cpu bash -lc '...'` commands for brief inspection/work;

2. GPU interactive bash (only gpu related tasks):
   `srun --gres=gpu:1 --pty bash -i`

3. Activate environment:
   `source scripts/activate.sh`

4. Use CPU tests only for genuinely CPU-only logic:
   `CUDA_VISIBLE_DEVICES="" pytest ...`

5. For GPU-sensitive paths, prefer targeted GPU validation in addition to small CPU checks.

6. Remember to close the node after use: `exit`