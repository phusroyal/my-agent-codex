# Work Packages

This folder defines **what to do, in order**.

Each work-package file describes one bounded stage of the project and should be understandable without reading the entire design document.

Work-package files describe:
- the question being answered;
- required prior results and implementation pieces;
- inputs;
- exact experiment or analysis to run;
- measurements to record;
- outputs;
- conditions for continuing, narrowing, or stopping;
- links to the scientific and implementation documents that define the details.

They do **not** track current progress. Progress belongs in `../exec-plan/`.

Current sequence:

- `roadmap-rules.md` — shared execution order and rules.
- `wp0-experimental-setup.md` — build and validate the experimental substrate.
- `wp1-behavioral-pilot.md` — behavioral pilot and condition discovery.
- `wp2-behavioral-confirmation.md` — powered confirmation on new seeds.
- `wp3-representation.md` — test whether goal information remains available internally.
- `wp4-neural-mechanism.md` — test causal neural use and downstream transmission.
- `wp5-repair-cause.md` — conditional repair and preceding-cause follow-up.
- `wp6-robustness.md` — surface, architecture, and domain robustness.

A work package can use this structure when useful (but not necessarily must follow, can adjust to project's needs):

```markdown
# WP1 — Behavioral Pilot

## Question
What does this package test?

## Requires
- links to the relevant scientific-design files
- links to the relevant implementation files
- required config files

## Input
What must already exist?

## Run
1. ...
2. ...
3. ...

## Record
What outputs and diagnostics are saved?

## Output
What does the next package receive?

## Continue when
What result supports the next step?

## Narrow when
What result preserves a smaller claim but changes the next step?

## Stop when
What result makes the next claim unidentifiable?
```

When using Codex, give it the specific subsection being implemented rather than asking it to implement an entire work package at once. The task prompt should point to:
- `AGENTS.md`;
- the relevant work-package section;
- the implementation documents it references;
- the relevant config and source files;
- explicit acceptance criteria for that bounded task.
