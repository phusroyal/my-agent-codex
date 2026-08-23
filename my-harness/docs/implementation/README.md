# Implementation

This folder contains the exact implementation specifications needed to turn the scientific design into code and reproducible experiments.

Use these documents when implementing or testing the corresponding subsystem.

Current files:

- `tools-plans-interventions.md` — tool schemas, planner/actor objects, randomized tool-output payloads, and controlled plan interventions.
- `runtime-and-generator.md` — latent task generation, surface rendering, prompt/history serialization, simulator boundary, checkpoint reconstruction, and runtime invariants.
- `behavioral-estimators.md` — checkpoint replay construction and behavioral causal estimators.
- `neural-interventions.md` — representation measurements, neural interchange, blocking/restoration, and cross-condition tests.
- `statistical-tests.md` — confirmatory statistical tests, power rules, and follow-up screening rules.

Scientific motivation and interpretation belong in `../scientific-design/`.

Execution order belongs in `../work-packages/`.

Current progress belongs in `../exec-plan/`.

When a work package requires an implementation detail, it should link directly to the file and section that owns that detail rather than restating it.
