---
name: review-contract-skill
description: Use when reviewing or validating an implementation against an approved plan or acceptance criteria. Trigger for functionality review, completeness checks, consistency review, documentation/tests audit, and PASS-or-REVISE validation. Do not use for initial planning or direct implementation.
---

# Review Contract Skill

## Purpose

Review an implementation against its intended contract.

This skill supports both broad code review and stricter completion validation.

## When to use

Use this skill when the user asks to:
- review a completed WP
- check whether implementation matches the plan
- look for major or critical issues
- audit tests and docs
- decide PASS or REVISE

## When not to use

Do not use this skill for:
- generating the first plan
- exploratory repo reading before scope is understood
- implementing code changes directly

## Review dimensions

Always check these dimensions unless the user narrows scope:
- Functionality: is the code likely correct on the intended path and edge cases?
- Completeness: is the requested phase actually done?
- Consistency: does it fit existing abstractions and repo conventions?
- Clarity: is there unnecessary complexity or hacky logic?
- Guesswork: does the implementation rely on unverified assumptions?
- Documentation: do comments/docs/config descriptions match reality?
- Testing: do tests cover primary behavior and likely failure modes?
- Other risks: anything likely to get flagged in code review or during experiments

## Procedure

1. Re-read the approved plan or acceptance criteria.
2. Inspect the implementation with the contract in mind.
3. Separate major issues from medium issues.
4. Distinguish true blockers from nice-to-have improvements.
5. Check whether tests and docs support the implementation claims.
6. Decide whether the work should PASS or REVISE.
7. Give the minimal next actions needed to reach PASS.

## Review rules

- Prioritize correctness and completeness over style nits.
- Do not approve work that is only “almost done.”
- Be explicit when evidence is weak.
- Prefer concrete failure modes over vague discomfort.
- If the code differs from the plan, say whether the deviation is justified or risky.

## Output format

Use this exact structure unless the user asks otherwise.

### Verdict
PASS or REVISE

### Major findings

### Medium findings

### Missing tests or docs

### Mismatch with approved plan

### Minimal next actions

### Most likely code review flags

## Quality bar

A good review should help the next agent know exactly:
- what is wrong
- how serious it is
- what must be fixed before moving on

# Build, Test, and Development Commands
Please, do not run commands on login-node (even for getting the code), it will be really noisy, get either a cpu/gpu node to run.
1. Get interactive bash `srun --pty bash -i` (cpu only) if you need gpu: `srun --gres=gpu:1 --pty bash -i` (only gpu related tasks) in the begining of your session.
2. Activate env first: `source scripts/activate.sh`
3. Run test on cpu: `CUDA_VISIBLE_DEVICES="" pytest ...`