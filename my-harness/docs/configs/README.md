# Configs

This folder stores executable experiment settings in machine-readable files such as YAML.

Put values here when the code needs to read them directly, for example:
- model and decoding settings;
- task-generation parameters;
- seed ranges and data splits;
- checkpoint rounds;
- rollout horizons;
- verification-credit limits;
- history-replay settings;
- intervention settings;
- frozen thresholds used by an experiment.

The scientific reason for a setting belongs in `../scientific-design/` or `../work-packages/`. The exact value used by code belongs here.

Do not duplicate the same executable constant across prose and source code. When a work package refers to a configurable value, it should point to the relevant config key.

Example (but not necessarily must follow, can adjust to project's needs):

```yaml
model:
  name: Qwen3-8B
  dtype: bfloat16
  thinking: false
  decoding: greedy

pilot:
  seeds: 24
  checkpoints: [1, 3, 4, 6]
  branch_horizon: 3

history_replay:
  seeds: 12
  conditions:
    - deep
    - shallow
    - length_matched
    - compressed
  token_tolerance: 0.05
```
