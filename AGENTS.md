# Agent Operating Instructions

This repository is the SecureTheCloud doctrine control plane.

All agents working on SecureTheCloud products, modules, suites, evidence surfaces, enforcement surfaces, adapters, or portfolio packaging must obey this repository as the canonical source of truth.

## Mandatory read-before-build files

Before proposing or implementing any suite, module, authority, callable interface, enforcement pathway, evidence surface, or product-packaging change, agents must read the following files:

1. `doctrine.lock.md`
2. `docs/portfolio/SUITE_CATALOG.md`
3. `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`
4. `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md`
5. `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`
6. `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md`
7. `contracts/portfolio/suite_catalog.json`
8. `contracts/portfolio/module_registry.json`
9. `contracts/portfolio/authority_matrix.json`
10. `contracts/portfolio/composition_rules.json`
11. `contracts/portfolio/status_taxonomy.json`

## Active machine-readable contracts

Phase 3 made the following files active shared portfolio contracts:

- `contracts/portfolio/suite_catalog.json`
- `contracts/portfolio/module_registry.json`
- `contracts/portfolio/authority_matrix.json`
- `contracts/portfolio/composition_rules.json`
- `contracts/portfolio/status_taxonomy.json`

Agents may consume these files for programmatic checks, but must continue to treat `doctrine.lock.md` and the Markdown doctrine files as the human-readable authority source.

## Validation requirement

Contract and schema changes must preserve the validation rules implemented in:

- `tools/validate_doctrine_contracts.py`
- `.github/workflows/doctrine-validate.yml`

## Non-negotiable rules

Agents must not invent:

- suite names
- suite membership
- module ownership
- authority type
- enforcement ownership
- callable interfaces
- product packaging boundaries
- SENTINEL bypasses
- status taxonomy values
- runtime authority not granted by this doctrine

## Required behavior

When another repository or agent needs product or authority guidance, it must consume this repository's doctrine files instead of creating a local substitute.

When a downstream implementation conflicts with this doctrine, the implementation is wrong unless this repository is updated through a doctrine phase gate first.

## Forbidden in this repository

This repository must not contain:

- runtime adapter code
- Helm templates
- customer-facing website assets
- product frontend source code
- module-specific enforcement logic
- live backend integrations
- credential material
- generated secrets
- production deployment scripts

## SOC 2 alignment expectation

Changes that alter authority, suite membership, enforcement boundaries, callable interfaces, or product packaging must update SOC 2 traceability documents once those documents exist.

## Doctrine change rule

Doctrine changes must be deliberate, reviewable, and traceable. Changes that affect authority or product packaging should update:

- `doctrine.lock.md`
- relevant `docs/portfolio/*` doctrine files
- relevant `contracts/portfolio/*.json` files
- relevant `schemas/portfolio/*.schema.json` files
- SOC 2 traceability documents when applicable
- `docs/phases/PHASE_TRACKER.md`
