# Phase Tracker

**Project:** SecureTheCloud Doctrine Control Plane
**Repository:** `S3curethecloud/securethecloud-doctrine-control-plane`
**Current Status:** Phase 0 / Repository Baseline In Progress
**Last Updated:** 2026-05-23

## Phase 0 — Repository Baseline

**Goal:** Establish the repository as the doctrine control-plane source of truth.

### Checklist

- [x] Repository verified
- [x] Root README created
- [x] Agent operating instructions created
- [x] Governance rules created
- [x] Doctrine lock created
- [ ] Changelog created
- [ ] CODEOWNERS created
- [ ] Pull request template created
- [ ] Phase 0 evidence recorded

### Exit criteria

- [ ] Repository declares scope and non-scope
- [ ] Agents know how to consume doctrine
- [ ] Governance process is explicit
- [ ] Phase tracker exists

## Phase 1 — Portfolio Doctrine Baseline

**Goal:** Define customer-offerable suites, Shared Trust Fabric, Composition Layer doctrine, SENTINEL control-point doctrine, authority separation, and product packaging boundaries.

### Checklist

- [ ] Create `docs/portfolio/SECURETHECLOUD_ENTERPRISE_PRODUCT_PORTFOLIO.md`
- [ ] Create `docs/portfolio/SHARED_TRUST_FABRIC.md`
- [ ] Create `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md`
- [ ] Create `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`
- [ ] Create `docs/portfolio/SUITE_CATALOG.md`
- [ ] Create `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md`
- [ ] Define four customer-offerable suites
- [ ] Define Shared Trust Fabric
- [ ] Freeze Composition Layer rules
- [ ] Canonicalize SENTINEL control-point doctrine
- [ ] Record Phase 1 evidence

## Phase 2 — Module Authority Matrix

**Goal:** Assign every module to category, status, authority type, callable interfaces, forbidden actions, and suite membership.

### Checklist

- [ ] Create `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`
- [ ] Create `docs/portfolio/STATUS_TAXONOMY.md`
- [ ] Define module categories
- [ ] Define module status values
- [ ] Define module authority types
- [ ] Define callable interfaces
- [ ] Define forbidden actions per module
- [ ] Assign all modules to suites, Shared Trust Fabric, or internal doctrine ownership
- [ ] Record Phase 2 evidence

## Phase 3 — Shared Machine-Readable Contracts

**Goal:** Create schemas and JSON contracts that all agents can consume.

### Checklist

- [ ] Create `schemas/portfolio/module_registry.schema.json`
- [ ] Create `schemas/portfolio/suite_catalog.schema.json`
- [ ] Create `schemas/portfolio/authority_matrix.schema.json`
- [ ] Create `contracts/portfolio/module_registry.json`
- [ ] Create `contracts/portfolio/suite_catalog.json`
- [ ] Create `contracts/portfolio/authority_matrix.json`
- [ ] Create `contracts/portfolio/composition_rules.json`
- [ ] Create `contracts/portfolio/status_taxonomy.json`
- [ ] Validate contracts against schemas
- [ ] Record Phase 3 evidence

## Phase 4 — SOC 2 Alignment Evidence

**Goal:** Map doctrine and change-control artifacts to SOC 2-aligned control evidence.

### Checklist

- [ ] Create `docs/soc2/SOC2_ALIGNMENT_OVERVIEW.md`
- [ ] Create `docs/soc2/SOC2_CONTROL_TRACEABILITY.md`
- [ ] Create `docs/soc2/SOC2_EVIDENCE_REGISTER.md`
- [ ] Create `docs/soc2/SOC2_CHANGE_MANAGEMENT.md`
- [ ] Map doctrine files to SOC 2 trust service categories
- [ ] Map authority boundaries to risk/control objectives
- [ ] Map change-management workflow to evidence
- [ ] Record Phase 4 evidence

## Phase 5 — Agent Adoption Gate

**Goal:** Ensure other agents know how to consume and obey the doctrine.

### Checklist

- [ ] Create `docs/portfolio/AGENT_CONSUMPTION_GUIDE.md`
- [ ] Add CI workflow for schema validation
- [ ] Add doctrine PR checklist
- [ ] Add rule requiring agents to use shared contracts
- [ ] Add rule forbidding local substitute doctrine
- [ ] Record Phase 5 evidence

## Phase 6 — Optional Read-Only Doctrine Portal Evaluation

**Goal:** Decide whether a read-only generated documentation portal is useful.

### Checklist

- [ ] Evaluate frontend need
- [ ] Confirm frontend is not required for doctrine baseline
- [ ] If approved, define read-only generated-docs scope only
- [ ] Confirm no runtime control or enforcement logic is added
- [ ] Record Phase 6 evidence
