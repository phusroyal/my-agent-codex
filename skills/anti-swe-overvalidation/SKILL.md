---
name: anti-swe-overvalidation
description: "Keep research-code implementation, execution, and review centered on scientific correctness, sound inference, deterministic claims, and the smallest meaningful validation. Use when an agent is at risk of importing production-SWE, security, release-integrity, or process ceremony that does not protect a stated research claim or real trust boundary."
argument-hint: "<research coding, execution, or review task>"
---

# Anti-SWE Overvalidation

Use this skill as a **research-code overlay** while coding, executing experiments, or reviewing work. Its purpose is not to lower the quality bar. Its purpose is to put rigor in the right place: the scientific method, evaluated population, numerical procedure, decision rule, uncertainty, and stated claim.

The default question is:

> What scientifically meaningful failure, reproducibility failure, or real boundary violation would this check prevent?

If there is no concrete answer, do not add the check merely because it would be conventional in production software, security engineering, release management, or compliance work.

## Activate When

- The repository is primarily a research project, experiment pipeline, analysis codebase, or paper implementation.
- The user asks for scientific correctness, soundness, deterministic claims, statistical evidence, simplicity, or minimal validation.
- The user says not to invent new science or not to apply software-style overvalidation.
- Coding is accumulating speculative guards, compatibility layers, manifests, schemas, or tests unrelated to a scientific decision.
- Execution is being blocked by exact-environment, byte-identity, exhaustive-suite, or provenance ceremony beyond the intended reproducibility claim.
- Reviewers are treating production-readiness conventions as scientific acceptance criteria.

This skill may accompany an implementation, execution, debugging, planning, or review workflow. It does not replace that workflow; it changes how rigor and blockers are chosen.

## Do Not Activate When

- The task concerns an actual production service, public API, authentication, authorization, payments, secrets, or regulated data.
- Inputs cross a real untrusted boundary, such as arbitrary uploaded files, shell fragments, network requests, unsafe deserialization, or user-controlled code execution.
- The user explicitly requests a security audit, supply-chain audit, tamper detection, compliance evidence, release attestation, or bitwise reproduction.
- A published artifact contract explicitly requires exact byte identity or cryptographic verification.
- Failure could cause destructive external effects rather than only an incorrect or failed experiment.

When one of these cases applies, use the appropriate security or production-engineering standard for that boundary. Do not use this skill to dismiss a real vulnerability.

## Governing Standard

Prefer the **minimum sufficient validation** that establishes the intended research claim.

Prioritize, in order:

1. **Scientific meaning** — the implemented quantity, population, assumptions, and comparison match the method.
2. **Decision correctness** — thresholds, tie rules, selection logic, fallbacks, and denominators match the approved plan or paper.
3. **Claim-level determinism** — the same declared inputs and method lead to the same reported decision, within the declared numerical policy.
4. **Numerical and statistical adequacy** — tolerances, uncertainty, power, significance, or equivalence are appropriate for the claim being made.
5. **Runtime feasibility** — the intended experiment can finish with truthful resource and coverage reporting.
6. **Maintainability needed for the present task** — the code is understandable and scoped without speculative infrastructure.
7. **Artifact identity or security controls** — only when identity or an actual threat boundary can change the scientific conclusion.

Do not reverse this order by allowing software ceremony to block direct evidence of scientific correctness.

## Required Distinctions

### Scientific reproducibility is not bitwise identity

State which level the claim needs:

- **Semantic determinism:** the same scientific conclusion or selected label is obtained.
- **Numerical repeatability:** reported values agree within a justified tolerance.
- **Statistical reproducibility:** repeated samples support the same inferential conclusion under the declared procedure.
- **Bitwise reproducibility:** outputs are byte-for-byte identical.

Do not silently promote a semantic, numerical, or statistical claim into a bitwise requirement. Require bitwise identity only when the method, artifact contract, or user explicitly needs it.

### Accidental error is not adversarial sabotage

Assume collaborators act in good faith unless the task establishes another threat model. Validate plausible implementation mistakes, stale artifacts, population mismatches, and unsupported claims. Do not design defenses against hypothetical source tampering, coherent rehashing, hidden obfuscation, or malicious collaborators by default.

### Provenance is not scientific evidence

Provenance can identify what ran. It does not establish that the method is correct. Record enough provenance to interpret and reproduce the result, but do not substitute manifests, hashes, environment dumps, or workflow receipts for mathematical and empirical validation.

### More tests are not automatically more rigor

Tests are valuable when they protect a decision-changing invariant or a scientifically meaningful behavior. Test count, branch coverage, schema coverage, and exhaustive input matrices are not research results.

### Statistical ceremony is not statistical validity

Use the inferential procedure required by the research question. Do not demand a significance test for every scalar, add unplanned corrections, manufacture zero-valued results for empty populations, or expand the sampling design merely to make the pipeline appear rigorous. Never invent new science during validation.

## Default Trusted Research Artifact Policy

Unless the user establishes an untrusted or externally distributed artifact boundary,
assume generated experiment artifacts live on a trusted filesystem and can be
regenerated. This is the default for internal research pipelines.

- Resume authority belongs only to the incomplete phase. Never compare the complete
  resolved configuration to authorize reuse of completed phases.
- Compare only scientific inputs that can change the incomplete phase's result.
  Runtime topology, device IDs, workers, threads, paths, sharding, cache settings,
  logging, license prose, and unrelated phase settings are observational.
- Default artifact integrity is atomic publication, successful parse/load, and minimal
  shape, count, range, and required-field checks.
- Do not add content hashes, checksum chains, hashes of hashes, signatures, content
  addressing, exact-schema equality, or artifact-wide downstream revalidation without
  a stated corruption or untrusted-input requirement.
- A reviewer requesting an integrity gate must name the plausible silent scientific
  error it detects and explain why a direct semantic check is insufficient.
- Pin external scientific inputs for final evidence. Exploratory runs may use ordinary
  refs when the resolved revisions are recorded; tokenizer revision should inherit the
  model revision unless intentionally different.
- Licensing and citation prose belongs in documentation and must not participate in
  execution identity or resume compatibility.
- A hash is justified when it is part of the scientific algorithm, or when it compactly
  represents a decision-changing value that is impractical to compare directly.
- One representation is enough. Do not require both identity and content digests or
  propagate nested fingerprints through every downstream phase.
- Establish batch and worker invariance through exact discrete outputs and justified
  numerical tolerances, not matching serialized bytes.

Artifact-integrity-only findings are non-blocking for trusted, regenerable research
outputs unless the user explicitly requests publication, distribution, tamper
resistance, or byte-level reproduction.

## Common SWE-Overvalidation Smells

Treat the following as prompts to reconsider, not as absolute bans:

### Security and integrity theater

- Source hashes that make any code edit fail regardless of behavior.
- Tests intended to detect sabotage, disguised spellings, or unauthorized source changes.
- Tamper-proof manifests or attestations without an untrusted distribution boundary.
- Fail-closed behavior whose only missing input is internal verification ceremony.
- Applying a generic security checklist to code with no relevant external attack surface.

### Defensive programming against impossible internal states

- Revalidating values at every internal function boundary after they were already established.
- Guards for states excluded by the caller, type system, library contract, or experiment construction.
- Broad exception handling, fallback values, or retry machinery that hides a scientifically meaningful failure.
- Duplicate validation logic that can drift away from the actual method.

Validate real external boundaries. Trust explicit internal contracts unless repository evidence shows they are unreliable.

### Schema, format, and serialization ceremony

- Tests that only restate YAML, JSON, dataclass, or parser behavior.
- Snapshot tests for incidental formatting, field order, log wording, or comments.
- Versioning and migration machinery for an internal artifact that can simply be regenerated.
- Formal schemas for a small, stable, single-producer research artifact when direct use is clearer.

Test these surfaces only when a format mistake can silently change the population, formula, decision, or reported result.

### Speculative compatibility and abstraction

- Feature flags for a method replacement that should have one production path.
- Backward-compatibility shims for unpublished or regenerable artifacts.
- Plugin systems, adapters, registries, or policy layers with one current use.
- Generalized abstractions added for hypothetical future experiments.
- Fallback implementations kept merely because removing them feels unsafe.

Prefer the smallest direct implementation of the approved method.

### Release and provenance overreach

- Hashing every source, config, log, checkpoint, plot, and report as an acceptance gate.
- Requiring a clean Git tree or exact commit identity for exploratory or bounded evidence.
- Treating environment manifests as proof that results are correct.
- Binding review approval to one exact source digest rather than the reviewed behavior.
- Requiring publication-grade packaging for an internal research run.

Use artifact identity only when mixing artifacts would invalidate the claim. When practical, prefer a semantic identity check over a byte hash.

### Numerical overconstraint

- Exact floating-point equality when a justified tolerance answers the scientific question.
- Requiring identical CUDA, BLAS, driver, or reduction order without evidence that small numerical differences change the conclusion.
- Rejecting a valid backend because its intermediate values differ while its declared outputs remain within tolerance.
- Conflating a changed final scientific decision with harmless last-bit variation.

If platform differences can change the reported conclusion, disclose the supported environment or calibrate a claim-level policy. Do not promise device independence without evidence.

### Exhaustive QA without claim relevance

- Running the entire repository suite for an isolated scientific change when targeted checks establish the affected behavior.
- Testing every configuration key, malformed internal object, or impossible combination.
- Repeating runs “just in case” without a stated uncertainty or nondeterminism question.
- Blocking partial, coverage-limited evidence after the user has explicitly accepted that limitation.
- Treating skipped irrelevant checks as a failure of the scientific result.

Run the smallest check that can prove or falsify the current claim, then stop.

### Agent-process ceremony

- Requiring several agents, reviewers, or approval rounds for a small, well-bounded change.
- Producing checkpoints, ledgers, receipts, or evidence bundles that do not help assess the scientific result.
- Asking permission before every reversible local action.
- Re-deriving decisions the user has already made.
- Using a model for routing, retries, parsing, or deterministic transforms that ordinary code can perform exactly.

Use judgment where judgment is needed. Use deterministic code for deterministic work. Delegate only when independent expertise materially improves correctness.

## Coding Procedure

1. **Read the scientific authority.** Identify the paper, approved plan, author decision, or inherited method that bounds the implementation. Do not invent formulas, thresholds, fallbacks, or inferential procedures.
2. **State the claim contract.** Name the quantity, population, decision rule, necessary determinism level, and evidence that would establish correctness.
3. **Identify plausible failures.** Focus on errors that could change the scientific meaning or conclusion, not hypothetical malicious behavior.
4. **Implement the direct path.** Prefer existing utilities, deletion, and simple control flow. Avoid speculative abstractions, compatibility layers, and alternate paths.
5. **Validate at meaningful boundaries.** Check external inputs and decision-changing identities. Trust established internal invariants.
6. **Test vital logic.** Add or run tests for formulas, population selection, denominators, threshold boundaries, seeded decisions, and scientifically meaningful failure states.
7. **Stop when the contract is established.** Do not continue adding guards or tests merely to make the change look production-grade.

## Execution Procedure

1. **Define what the run can establish.** Distinguish exploratory, bounded, partial, calibration, and final-paper evidence.
2. **Use the smallest representative execution.** Preserve real dimensions and the relevant numerical route, but do not expand the run beyond the claim.
3. **Control declared sources of variation.** Seed stochastic procedures where appropriate and record decision-changing inputs.
4. **Compare at the correct level.** Use semantic, numerical, statistical, or bitwise comparison according to the declared requirement.
5. **Report coverage honestly.** Partial or device-limited evidence is acceptable when labeled as such and when no broader claim is made.
6. **Surface real failures.** Do not hide empty denominators, backend failures, missing populations, or unsupported comparisons behind defaults.
7. **Stop after sufficient evidence.** Do not add repeated reruns, exhaustive suites, environment attestations, or artifact bundles without a concrete unresolved question.

## Review Procedure

1. **Review against the scientific contract.** Start from the approved method and intended claim, not a generic production checklist.
2. **Trace each blocker to impact.** A blocking finding must show how it can change the formula, population, decision, inference, reproducibility claim, runtime feasibility, or a real security boundary.
3. **Separate categories clearly:**
   - **Scientific blocker:** the result or claim can be wrong, undefined, unsupported, or methodologically inconsistent.
   - **Implementation defect:** code does not implement the intended behavior or fails on a relevant execution path.
   - **Research limitation:** evidence is valid but narrower, noisier, or less general than desired; report rather than disguise it.
   - **Real security or operational blocker:** an established external boundary creates concrete risk.
   - **Non-blocking SWE preference:** maintainability, packaging, style, or production-hardening suggestion that does not affect the present claim.
4. **Reject invented requirements.** Do not upgrade preferences into blockers, add new science, or require unplanned statistics and experiments.
5. **Prefer direct verification.** Check the relevant equation, selection, denominator, cached-artifact compatibility, or output decision instead of relying only on provenance metadata.
6. **Approve bounded evidence as bounded.** Do not demand universal claims when the task only claims the measured coverage.
7. **Recommend the smallest repair.** Fix the scientific or execution defect without surrounding refactors or infrastructure.

## Hashes and Fingerprints

Hashes are one instance of the broader issue, not the central rule.

Do not use a hash to prove scientific correctness. A changed hash proves that bytes changed; an unchanged hash proves that the same bytes were observed. Neither proves that the method or conclusion is valid.

A fingerprint is justified when exact identity is itself decision-changing, for example:

- preventing a Gram matrix from being paired with a different readout matrix;
- distinguishing model, dataset, or SAE artifacts whose mismatch changes the evaluated population;
- invalidating a cache when its scientifically relevant inputs change.

Even then, prefer a direct semantic check when it is cheap and reliable. For example, verify the relevant matrix relationship or artifact identifiers rather than locking a source file’s digest.

## Real Security Boundary Exception

Do not suppress security work when a real boundary exists. Examples include:

- user-controlled shell commands, paths, uploads, network payloads, or serialized objects;
- authentication, authorization, secrets, credentials, or private data;
- package publication or artifacts consumed outside the trusted research group;
- destructive filesystem, scheduler, cloud, or production actions;
- downloaded executable code or dependencies with a stated supply-chain threat model.

For such a boundary, state the threat model and apply security controls locally to that boundary. Do not spread security ceremony through unrelated numerical and analytical code.

## Decision Test for Any Proposed Gate

Before adding a validation, test, manifest, reviewer requirement, or execution gate, answer:

1. Which stated scientific claim, decision, or real boundary does it protect?
2. What plausible failure would it detect?
3. Is that failure already excluded by an existing contract or direct check?
4. Is there a simpler semantic validation?
5. Would failure of this check mean the result is scientifically unsupported, or merely that software ceremony is incomplete?

If questions 1 and 2 have no concrete answer, omit the gate. If a simpler semantic validation exists, prefer it.

## Output Contract

When this skill materially changes the work, report:

```md
## Anti-SWE-Overvalidation Result

**Active work:** coding | execution | review
**Scientific contract:** <quantity, population, decision, and claim>
**Required determinism:** semantic | numerical | statistical | bitwise
**Minimum sufficient validation:** <checks run or required>
**Overvalidation omitted or downgraded:** <what and why>
**Evidence:** <direct result>
**Scientific limitations:** <coverage or uncertainty that remains>
**Real security boundaries:** <none, or boundary and control>
**Status:** supported | revise | blocked
```

Do not list omitted ceremony exhaustively when a one-line explanation is enough.

## Examples

**Good — coding:** Test that the selected family and dimension follow the approved decision rule, including meaningful threshold boundaries. Do not add tests for JSON field order or impossible internal objects.

**Good — execution:** Compare a numerical backend across supported devices at the level of reported metrics and final decisions using justified tolerances. Report device coverage. Do not claim bitwise portability or require identical BLAS and CUDA stacks unless that is the declared result.

**Good — review:** Block a zero eligible denominator being reported as a zero effect. Treat the absence of a formal schema version for a regenerable internal artifact as non-blocking.

**Good — identity check:** Ensure a cached Gram matrix belongs to the readout matrix used by the experiment because a mismatch changes the geometry. Prefer a direct identity or relationship check when practical.

**Bad — integrity theater:** Fail tests whenever a function’s source SHA changes, or attempt to detect a collaborator disguising an edit, when no security threat model was requested.

**Bad — defensive clutter:** Add nested validation, retries, fallbacks, and compatibility shims around an internal deterministic transform whose inputs are already established.

**Bad — review inflation:** Request changes because a research script lacks production deployment controls, exhaustive malformed-config tests, a full provenance manifest, and multiple independent approvals even though none affects the claim.

**Bad — weakened rigor:** Skip a population mismatch, unstable scientific decision, invalid statistical denominator, or genuine injection boundary under the label of simplicity. This skill removes irrelevant rigor, not relevant rigor.

## Stop Rule

Stop when the approved scientific contract is implemented, the smallest sufficient evidence has been read, limitations are stated truthfully, and no unresolved claim-changing or real security failure remains.

Do not continue merely to accumulate tests, reviewers, hashes, manifests, retries, abstractions, or generic quality signals.

Task: {{ARGUMENTS}}
