# SecureTheCloud Doctrine Control Plane

**Status:** Phase 0 / Repository Baseline

This repository is the canonical doctrine control plane for the SecureTheCloud enterprise portfolio.

It owns the source of truth for:

- customer-offerable suite definitions
- Shared Trust Fabric doctrine
- Composition Layer rules
- SENTINEL control-point doctrine
- module authority boundaries
- callable interface declarations
- forbidden-action boundaries
- product packaging boundaries
- SOC 2-aligned control traceability
- shared machine-readable contracts used by other agents

## Scope

This repository is documentation, schema, and contract oriented. It does **not** own runtime adapter code, Helm templates, UI/website assets, or module-specific enforcement logic.

## Canonical contract files

Agents and contributors must treat the following files as canonical once created:

- `doctrine.lock.md`
- `docs/portfolio/SECURETHECLOUD_ENTERPRISE_PRODUCT_PORTFOLIO.md`
- `docs/portfolio/SHARED_TRUST_FABRIC.md`
- `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md`
- `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`
- `docs/portfolio/SUITE_CATALOG.md`
- `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`
- `docs/portfolio/STATUS_TAXONOMY.md`
- `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md`
- `contracts/portfolio/suite_catalog.json`
- `contracts/portfolio/module_registry.json`
- `contracts/portfolio/authority_matrix.json`
- `contracts/portfolio/composition_rules.json`
- `contracts/portfolio/status_taxonomy.json`

## SOC 2 alignment posture

This repository is intended to produce SOC 2-aligned governance evidence for authority separation, change management, risk traceability, control ownership, and agent adherence.

This repository does **not** claim SOC 2 certification or replace an independent SOC 2 examination.

## Phase model

Implementation proceeds through phase gates tracked in `docs/phases/PHASE_TRACKER.md`.

Each phase must be marked complete only after its exit criteria are satisfied.

## Current phase

- [x] Phase 0 — Repository Baseline
- [ ] Phase 1 — Portfolio Doctrine Baseline
- [ ] Phase 2 — Module Authority Matrix
- [ ] Phase 3 — Shared Machine-Readable Contracts
- [ ] Phase 4 — SOC 2 Alignment Evidence
- [ ] Phase 5 — Agent Adoption Gate
- [ ] Phase 6 — Optional Read-Only Doctrine Portal Evaluation
