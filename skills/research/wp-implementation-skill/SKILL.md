---
name: wp-implementation-skill
description: Use when implementing one approved work package in a research codebase. Trigger for bounded coding tasks that must stay aligned with an existing plan, reuse existing abstractions where possible, and preserve correctness, speed, memory discipline, and maintainability. Do not use for high-level planning or independent review.
---

# Work Package Implementation Skill

## Purpose

Implement exactly one approved work package with minimal blast radius.

This skill is for coding after the plan is already accepted.

## When to use

Use this skill when the user asks to:
- implement WP0/WP1/etc.
- code one bounded phase from an approved plan
- add the tests/docs/config needed for one specific work package
- refine an implementation after review findings, while staying within the WP boundary

## When not to use

Do not use this skill for:
- making the initial architecture plan
- broad exploratory repo reading without coding
- general review or validation
- sweeping refactors outside the approved WP scope

## Required inputs

Before coding, re-read:
- the approved plan
- the task or math note if relevant
- the current code paths being modified
- any existing review findings that constrain the fix

## Procedure

1. Confirm the exact WP boundary.
2. Identify the minimal set of files that need to change.
3. Reuse or generalize existing abstractions where that improves maintainability.
4. Avoid one-off wrappers unless they are clearly the cleanest option.
5. Implement the core logic.
6. Add or update tests needed for the WP.
7. Update docs/config/logging only where the WP requires it.
8. Check for correctness, performance, memory, and maintainability risks in the touched path.
9. Summarize touched files, design choices, and unresolved concerns.

## Implementation rules

- One work package only unless a tiny cross-WP change is required to unblock correctness.
- Do not silently pull future work into the current task.
- Do not import from archive/reference code.
- Prefer repository-native utilities over new special-purpose helpers.
- Make runtime assumptions explicit when touching scheduling, state, dtype, device placement, checkpoint, or resume behavior.
- Optimize hot paths where relevant, but not at the expense of correctness or clarity.
- Keep new modules focused and reasonably small.

## Output format

Use this exact structure unless the user asks otherwise.

### Scope confirmed

### Files changed
For each file:
- what changed
- why it changed

### Main design choices

### Tests added or run

### Risks / unresolved concerns

### Recommended next step

## Quality bar

A good WP implementation should:
- satisfy the approved WP scope
- avoid unrelated churn
- be understandable by a later reviewer
- include the minimal tests and docs needed to make the change trustworthy

