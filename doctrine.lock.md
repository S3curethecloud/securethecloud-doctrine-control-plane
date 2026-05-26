# Doctrine Lock

**Status:** Phase 6 / Optional Read-Only Doctrine Portal Evaluation Complete
**Doctrine Version:** 0.6.0-read-only-portal-evaluation
**Last Updated:** 2026-05-23

## Canonical statement

This repository is the SecureTheCloud doctrine control plane.

It is the source of truth for portfolio-level authority, suite composition, module boundaries, status taxonomy, product packaging, SOC 2-aligned doctrine evidence, and agent-consumable portfolio contracts.

## Current frozen rules

### Repository scope

- This repository owns doctrine, schemas, contracts, SOC 2-aligned readiness evidence, and evidence traceability.
- This repository does not own runtime adapter code.
- This repository does not own Helm templates.
- This repository does not own UI or website assets.
- This repository does not own module-specific enforcement logic.

### Agent adoption rule

All downstream agents must read `docs/portfolio/AGENT_CONSUMPTION_GUIDE.md` before building or changing SecureTheCloud modules, suites, evidence surfaces, runtime surfaces, product packaging, authority boundaries, or customer-facing claims.

Agents must consume active machine-readable contracts from `contracts/portfolio/*.json` for programmatic checks.

Agents must not create local substitute doctrine.

Agents must stop and request doctrine clarification if Markdown doctrine and JSON contracts appear to conflict.

### Agent rule

Other agents must not invent suite membership, module authority, callable interfaces, enforcement ownership, forbidden actions, product packaging rules, status taxonomy values, or SENTINEL bypasses outside this doctrine.

### Active machine-readable contracts

The active shared contracts are:

- `contracts/portfolio/suite_catalog.json`
- `contracts/portfolio/module_registry.json`
- `contracts/portfolio/authority_matrix.json`
- `contracts/portfolio/composition_rules.json`
- `contracts/portfolio/status_taxonomy.json`

Agents may consume these files for programmatic doctrine checks.

Agents must still treat `doctrine.lock.md` and Markdown doctrine files as the human-readable authority source.

### SOC 2 readiness rule

The SOC 2 files under `docs/soc2/` provide SOC 2-aligned readiness evidence.

They do not claim SOC 2 certification.

They do not replace an independent SOC 2 examination.

They do not prove production operating effectiveness over an audit period.

### Phase 4 correction record

- Phase 4 SOC 2 files restored to doctrine-control-plane: true
- Misplaced Kubernetes Sentinel copies removed: true
- Doctrine PR merged: true
- Sentinel cleanup PR merged: true
- Phase 4 status: complete

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

### Read-only doctrine portal rule

A frontend portal is not required for the doctrine baseline.

A future doctrine portal may be approved only as a read-only generated documentation surface.

A portal must not become the source of truth.

A portal must not edit doctrine, mutate contracts, alter schemas, create authority, change phase status, bypass SENTINEL, claim SOC 2 certification, connect to live backends, create runtime sessions, issue tokens, grant authorization, or implement enforcement logic.

Git remains the canonical source of truth.


## Unfrozen pending doctrine

No pending doctrine phases remain in the initial doctrine-control-plane baseline.
