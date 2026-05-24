# Doctrine Lock

**Status:** Phase 3 / Shared Machine-Readable Contracts Complete
**Doctrine Version:** 0.3.0-machine-contract-baseline
**Last Updated:** 2026-05-23

## Canonical statement

This repository is the SecureTheCloud doctrine control plane.

It is the source of truth for portfolio-level authority, suite composition, module boundaries, status taxonomy, product packaging, and SOC 2-aligned doctrine evidence.

## Current frozen rules

### Repository scope

- This repository owns doctrine, schemas, contracts, and evidence traceability.
- This repository does not own runtime adapter code.
- This repository does not own Helm templates.
- This repository does not own UI or website assets.
- This repository does not own module-specific enforcement logic.

### Agent rule

Other agents must not invent suite membership, module authority, callable interfaces, enforcement ownership, forbidden actions, or product packaging rules outside this doctrine.

### Agent sharing rule

- Share the repository and root `AGENTS.md` immediately.
- Share Phase 1 and Phase 2 Markdown doctrine files.
- Phase 3 JSON contracts are now active shared portfolio contracts.
- Agents may consume `contracts/portfolio/*.json` for programmatic doctrine checks.
- Agents must still treat `doctrine.lock.md` and Markdown doctrine files as the human-readable authority source.

### Active machine-readable contracts

The active shared contracts are:

- `contracts/portfolio/suite_catalog.json`
- `contracts/portfolio/module_registry.json`
- `contracts/portfolio/authority_matrix.json`
- `contracts/portfolio/composition_rules.json`
- `contracts/portfolio/status_taxonomy.json`

The active schemas are:

- `schemas/portfolio/suite_catalog.schema.json`
- `schemas/portfolio/module_registry.schema.json`
- `schemas/portfolio/authority_matrix.schema.json`

Validation tooling exists at:

- `tools/validate_doctrine_contracts.py`
- `.github/workflows/doctrine-validate.yml`

### Frontend rule

A frontend is not required for the initial doctrine control-plane role.

If a frontend is ever added, it must be read-only documentation visualization generated from canonical Markdown and JSON contracts. It must not become the source of truth and must not implement runtime enforcement.

### SOC 2 rule

This repository may provide SOC 2-aligned evidence and traceability, but it does not claim SOC 2 certification.

### Customer-offerable suite rule

The four customer-offerable SecureTheCloud suites are:

1. SecureTheCloud Agent Blackbox Suite
2. SecureTheCloud Compliance Evidence Suite
3. SecureTheCloud Runtime Assurance Suite
4. SecureTheCloud Risk Intelligence Suite

Shared Trust Fabric is not a fifth customer-offerable suite.

### Shared Trust Fabric rule

Shared Trust Fabric is the shared doctrine, registry, schema, contract, taxonomy, metadata, and traceability substrate used across suites.

Shared Trust Fabric participation does not grant runtime authority.

### Composition Layer rule

Composition may package, present, route read-only evidence views, and assemble customer-safe suite surfaces.

Composition may not create authority, bypass SENTINEL, issue tokens, grant authorization, mutate runtime systems, or convert evidence/explanation modules into enforcement modules.

### SENTINEL control-point rule

SENTINEL is the canonical control point for runtime-impacting allow, deny, admission, policy-decision, enforcement, and production-control outcomes.

No suite, module, agent, Composition Layer package, evidence surface, explanation surface, or customer packaging surface may bypass SENTINEL when a runtime-impacting control decision is in scope.

### Product packaging rule

Packaging is not authority.

Customer packages may combine suite visibility, but they must not merge suite roles, expand module authority, hide forbidden actions, bypass SENTINEL, or claim SOC 2 certification from SOC 2-aligned documentation.

### Status taxonomy rule

Agents must use the status values defined in `docs/portfolio/STATUS_TAXONOMY.md` and `contracts/portfolio/status_taxonomy.json`.

Agents must not invent local module lifecycle, suite/packaging, authority, evidence, interface, or category values.

### Module authority rule

No module may claim authority outside `docs/portfolio/MODULE_AUTHORITY_MATRIX.md` and `contracts/portfolio/authority_matrix.json`.

Any module not listed in the matrix is an `unregistered_candidate` with `no_runtime_authority`.

Suite membership does not create authority.

Packaging does not create authority.

Composition does not create authority.

Evidence does not create enforcement authority.

Explanation does not create authorization authority.

## Unfrozen pending doctrine

The following areas are not yet frozen and must be completed in later phases:

- SOC 2 traceability documents
- agent consumption guide
