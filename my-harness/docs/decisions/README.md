# Decisions

This folder records project decisions that are useful to preserve over time but do not belong in the scientific design or implementation specification.

Create a decision note when:
- an important design choice changes after earlier work already depended on it;
- several plausible options were considered and the reason for choosing one will matter later;
- a decision affects multiple parts of the repository and would otherwise be difficult to reconstruct from Git history.

Do not create a decision note for every ordinary implementation choice.

Each note should state:
1. the decision;
2. the alternatives considered;
3. the reason for the choice;
4. what files or experiments it affects;
5. whether the decision can be revisited.

Use numbered filenames such as:

```text
001-model-choice.md
002-renderer-policy.md
003-history-replay-design.md
```

Current scientific claims remain in `../scientific-design/`. Exact implementation rules remain in `../implementation/`.
