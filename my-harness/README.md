pipeline:
1. populate docs/
2. init AGENTS.md based on the constraints
3. append project AGENTS.md with the outside AGENTS.md (../AGENTS.md)
4. ask codex to write architecture
5. Ask codex to add this at the end
```markdown
## Living Documentation

Treat the repository maps as maintained interfaces, not one-time setup files:

- `docs/index.md` is the top-level human and agent map. Update it when documents move, ownership or status changes, or a new documentation area becomes authoritative.
- `docs/*/README.md` files are local folder maps. Update the relevant map when that folder's purpose, contents, read order, or relationship to neighboring folders changes.
- `ARCHITECTURE.md` records stable subsystem ownership, dependency direction, boundaries, and invariants. Update it when those architectural facts change, but not for ordinary implementation progress, small refactors, or fast-changing details.

A change that makes one of these maps inaccurate includes the corresponding documentation update. Keep transient status in `docs/exec-plan/`, detailed behavior in the owning design or implementation document, and code-local facts in code comments or docstrings. Revisit `ARCHITECTURE.md` less often than the navigation maps so it remains a dependable long-lived overview.
```