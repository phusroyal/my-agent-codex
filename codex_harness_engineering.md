---
tldr:
tags:
  - note
date: "202608211223"
aliases:
related:
---

# Repository Knowledge + Golden Principles

> Personal action sheet for AI-heavy software repos.

## 1. Make the Repository the System of Record

### Build This Layout

```text
AGENTS.md
ARCHITECTURE.md
docs/
├── design-docs/
│   ├── index.md
│   ├── core-beliefs.md
│   └── ...
├── exec-plans/
│   ├── active/
│   ├── completed/
│   └── tech-debt-tracker.md
├── generated/
│   └── ...
├── product-specs/
│   ├── index.md
│   └── ...
├── references/
│   └── ...
├── DESIGN.md
├── FRONTEND.md
├── PLANS.md
├── PRODUCT_SENSE.md
├── QUALITY_SCORE.md
├── RELIABILITY.md
└── SECURITY.md
```

### Keep `AGENTS.md` Small

- Use it as a map, not a handbook.
- Keep only:
  - what this repo is
  - what to read first
  - common commands
  - hard rules
  - where deeper docs live
- Point to the exact file that owns each topic.
- Remove explanations that belong in deeper docs.
- Keep it short enough to read on every task.

### Make `ARCHITECTURE.md` a Code Map

- Keep it short and stable.
- Start with what the system does.
- List the main folders/modules and what each owns.
- Show which parts may depend on which other parts.
- Name important files, modules, and types.
- State rules that must always stay true.
- State important boundaries between parts of the system.
- Add a short section for concerns that touch many areas.
- Make it answer:
  - “Where do I change X?”
  - “What does this part do?”
- Move detailed behavior into smaller docs or code comments.
- Avoid fast-changing details.
- Revisit it a few times per year.

### Put Durable Decisions in the Repo

- Copy important decisions out of chat, meetings, tickets, and people’s heads.
- Put product behavior in `docs/product-specs/`.
- Put design decisions in `docs/design-docs/`.
- Put long-running work in `docs/exec-plans/active/`.
- Move finished plans to `docs/exec-plans/completed/`.
- Record known cleanup work in `tech-debt-tracker.md`.
- Store generated references in `docs/generated/`.
- Store useful external reference material in `docs/references/`.
- Keep one clear source of truth for each topic.

### Index the Knowledge

- Add an `index.md` to every growing docs area.
- Give each doc a clear status.
- Mark whether the doc still matches the code.
- Link related docs together.
- Link each high-level rule to the place that enforces it.
- Delete or replace stale docs instead of leaving competing versions.

### Use Plans for long Work

- Keep small changes lightweight.
- Create a checked-in plan for large features or refactors.
- Write the goal and expected result.
- List the main steps.
- Record progress as work happens.
- Record important decisions and why they changed.
- Keep the plan usable without old chat history.
- Move it to `completed/` when done.

### Check the Knowledge Automatically

- Add CI checks for broken internal links.
- Add CI checks for missing required docs.
- Add CI checks for invalid doc structure.
- Add a simple freshness check for critical docs.
- Add checks that generated docs were regenerated when their source changed.
- Run a recurring doc-cleanup task.
- Have it:
  - find stale docs
  - compare docs with current code
  - open small fix PRs
  - remove dead references
  - repair indexes and links

### Keep Context Small

- Start every agent with the small map.
- Load deeper docs only when needed.
- Prefer several focused docs over one giant instruction file.
- Keep repeated rules in one place.
- Do not paste the same guidance into many files.

---

## 2. Turn “AI sLop” into gOlden pRinciples

### Create Golden Principles from Repeated Pain

- Watch for the same review comment appearing again.
- Watch for the same bad pattern appearing in multiple files.
- Watch for fixes that agents repeatedly undo.
- Turn each repeated problem into one short rule.
- Put the rule in the repo.
- Make the rule specific enough to check.
- Prefer rules about correctness and structure over style taste.
- Enforce the rule automatically when possible.

### Use This Rule Format

- **Rule:** one sentence saying what must happen.
- **Applies to:** folders/files covered by the rule.
- **Check:** command, linter, test, or script that detects a violation.
- **Fix:** one sentence telling the agent how to repair it.
- **Exception:** list the few allowed exceptions, or say none.

### Start with These Golden Principles

- Reuse a shared helper before creating a new local helper.
- Keep one source of truth for shared behavior.
- Check outside data as soon as it enters the system.
- Convert outside data into a known shape before using it.
- Do not build logic on guessed API fields.
- Use an API client or schema that knows the expected fields when available.
- Keep dependency direction fixed between major layers.
- Block imports that jump across forbidden layers.
- Route shared concerns through one clear entry point.
- Use one logging format everywhere.
- Use one naming pattern for schemas and important types.
- Set file-size limits and split files that keep growing.
- Make invalid states hard to create with clear data shapes and types.
- Do not duplicate mutable data unless one small module owns the syncing.
- Keep generated files generated; do not hand-edit them.
- Require tests or checks for every rule that can break silently.

### Enforce Rules, not Personal Style

- Enforce what must be true.
- Do not dictate every implementation detail.
- Let agents choose local code shape when the result stays correct.
- Reject changes that break architecture, data safety, or repeatability.
- Accept code that is correct, maintainable, and easy for the next agent to understand.
- Promote a written rule into code when documentation alone keeps failing.

### Make Rule Failures Self-explaining

- Make every custom check print:
  - what rule failed
  - where it failed
  - what good code should do
  - the fastest safe fix
  - the doc that explains the rule
- Prefer auto-fixes for simple mechanical problems.
- Fail early before a bad pattern spreads.

### Run Continuous Cleanup

- Scan for golden-principle violations on a regular schedule.
- Update `QUALITY_SCORE.md` from the scan.
- Add larger issues to `tech-debt-tracker.md`.
- Open small refactor PRs instead of giant cleanup PRs.
- Keep each cleanup PR focused on one rule.
- Run all tests and checks before merging.
- Auto-merge only low-risk, mechanical fixes.
- Send judgment calls to a human.
- Fix bad patterns daily or weekly, not in rare cleanup weeks.

### Feed Human Taste back into the System

- Turn useful review comments into docs or checks.
- Turn recurring bug causes into golden principles.
- Turn repeated refactors into automated rules.
- Turn missing context into repository docs.
- Turn unclear check failures into better error messages.
- Treat every repeated agent mistake as a missing repo rule, missing tool, or missing explanation.

### Avoid These Failure Modes

- Do not grow `AGENTS.md` into a giant manual.
- Do not keep important decisions only in chat.
- Do not maintain two sources of truth for the same rule.
- Do not rely on reviewers to remember every rule.
- Do not write vague rules such as “keep code clean.”
- Do not add rules that cannot be explained with a clear good/bad example.
- Do not wait for technical debt to become a large cleanup project.
- Do not let one bad generated pattern become the template for hundreds of new files.

---

## 3. Minimal Operating Loop

- Add or update the repository knowledge first.
- Give the agent the small repo map.
- Let it load only the docs needed for the task.
- Run architecture and golden-principle checks.
- Review failures.
- Fix the code or improve the rule.
- Record any new durable decision in the repo.
- Turn repeated feedback into an automatic check.
- Run recurring doc and code cleanup.
- Keep the next agent from repeating the same mistake.

---

## Sources

- OpenAI — Harness engineering: https://openai.com/index/harness-engineering/
- matklad — `ARCHITECTURE.md`: https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html
- OpenAI — Using `PLANS.md` for multi-hour problem solving: https://developers.openai.com/cookbook/articles/codex_exec_plans
- Alexis King — Parse, don’t validate: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/
- Steve Krenzel — AI Is Forcing Us To Write Good Code: https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code
