# Agent Consumption Guide

**Status:** Phase 5 / Agent Adoption Gate Complete
**Doctrine Version:** 0.5.0-agent-adoption-baseline
**Last Updated:** 2026-05-23

## Purpose

This guide tells every SecureTheCloud agent how to consume the Doctrine Control Plane before building, modifying, packaging, exposing, or enforcing any SecureTheCloud module, suite, evidence surface, runtime surface, product boundary, or control path.

## Canonical repository

The canonical doctrine repository is:

`S3curethecloud/securethecloud-doctrine-control-plane`

Agents must not create local substitute doctrine in downstream repositories.

## Required read-before-build order

Before making changes, agents must read the doctrine in this order:

1. `AGENTS.md`
2. `doctrine.lock.md`
3. `docs/portfolio/SUITE_CATALOG.md`
4. `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`
5. `docs/portfolio/STATUS_TAXONOMY.md`
6. `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md`
7. `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`
8. `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md`
9. `docs/soc2/SOC2_ALIGNMENT_OVERVIEW.md`
10. `docs/soc2/SOC2_CONTROL_TRACEABILITY.md`
11. `docs/soc2/SOC2_EVIDENCE_REGISTER.md`
12. `docs/soc2/SOC2_CHANGE_MANAGEMENT.md`

## Machine-readable contract consumption

After reading the human-readable doctrine, agents may consume these active JSON contracts:

- `contracts/portfolio/suite_catalog.json`
- `contracts/portfolio/module_registry.json`
- `contracts/portfolio/authority_matrix.json`
- `contracts/portfolio/composition_rules.json`
- `contracts/portfolio/status_taxonomy.json`

Human-readable doctrine remains authoritative for interpretation.

Machine-readable contracts are used for programmatic consistency checks.

If a Markdown doctrine file and JSON contract appear to conflict, stop and request a doctrine update. Do not guess.

## Non-negotiable agent rules

Agents must not invent:

- suite names
- suite membership
- module ownership
- module authority
- callable interfaces
- forbidden actions
- enforcement ownership
- product packaging boundaries
- status taxonomy values
- SOC 2 claims
- SENTINEL bypasses
- runtime authority not granted by doctrine

## Default unregistered-module rule

Any module not listed in the module registry or authority matrix is:

- `unregistered_candidate`
- `no_runtime_authority`
- not customer-offerable
- not allowed to enforce
- not allowed to mutate runtime systems
- not allowed to claim canonical product status

## Composition rule

Composition is packaging and presentation.

Composition does not create authority.

Composition must preserve:

- suite boundaries
- module authority
- callable interfaces
- forbidden actions
- SENTINEL control-point doctrine
- SOC 2 claim boundaries

## SENTINEL rule

SENTINEL is the canonical control point for runtime-impacting allow, deny, admission, policy-decision, enforcement, and production-control outcomes.

No agent may bypass SENTINEL when a runtime-impacting control decision is in scope.

No agent may create a local substitute control point.

## SOC 2 claim boundary

The SOC 2 files in this repository provide SOC 2-aligned readiness evidence only.

They do not claim:

- SOC 2 certification
- an independent SOC 2 audit
- production operating effectiveness
- Type 1 or Type 2 audit completion
- auditor attestation

Agents must update SOC 2 traceability when changing:

- suite membership
- module authority
- callable interfaces
- forbidden actions
- product packaging boundaries
- SENTINEL control-point doctrine
- evidence scope
- customer-facing compliance claims

## Runtime non-scope

Unless future doctrine explicitly approves otherwise, this doctrine repository does not authorize agents to add:

- runtime adapter code
- Helm templates
- UI or website assets
- module-specific enforcement logic
- live backend integrations
- token issuance
- authorization behavior
- runtime session creation
- production deployment scripts
- production enforcement

## Downstream repository rule

Every downstream SecureTheCloud repository should include a read-before-build pointer to this doctrine control plane.

Recommended pointer:

```text
Before building or changing this repository, read:
S3curethecloud/securethecloud-doctrine-control-plane

Required first-read files:
- AGENTS.md
- doctrine.lock.md
- docs/portfolio/AGENT_CONSUMPTION_GUIDE.md
- contracts/portfolio/*.json
Agent decision flow

Before making a change, an agent must answer:

Is the module registered?
Is the suite membership defined?
Is the authority type defined?
Are callable interfaces defined?
Are forbidden actions defined?
Does the change affect SENTINEL?
Does the change affect SOC 2 traceability?
Does the change affect customer packaging?
Does the change introduce runtime behavior?
Does the change require a doctrine phase update?

If any answer is uncertain, stop and request doctrine clarification.

Phase 5 adoption status
Agent consumption guide created: true
Doctrine-read-before-build instructions created: true
Markdown and JSON contract consumption order clarified: true
SOC 2 claim boundaries clarified: true
Local substitute doctrine forbidden: true
Agent adoption gate complete: true
