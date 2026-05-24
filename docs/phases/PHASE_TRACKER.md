# Phase Tracker

**Project:** SecureTheCloud Doctrine Control Plane
**Repository:** `S3curethecloud/securethecloud-doctrine-control-plane`
**Current Status:** Phase 2 / Module Authority Matrix Complete
**Last Updated:** 2026-05-23

## Phase 0 — Repository Baseline

**Goal:** Establish the repository as the doctrine control-plane source of truth.

### Checklist

- [x] Repository verified
- [x] Root README created
- [x] Agent operating instructions created
- [x] Governance rules created
- [x] Doctrine lock created
- [x] Changelog created
- [x] CODEOWNERS created
- [x] Pull request template created
- [x] Phase 0 evidence recorded

### Exit criteria

- [x] Repository declares scope and non-scope
- [x] Agents know how to consume doctrine
- [x] Governance process is explicit
- [x] Phase tracker exists

### Evidence

- Repository verified: `S3curethecloud/securethecloud-doctrine-control-plane`
- Root baseline files created: `README.md`, `AGENTS.md`, `GOVERNANCE.md`, `doctrine.lock.md`, `CHANGELOG.md`, `CODEOWNERS`
- PR checklist created: `.github/pull_request_template.md`
- Phase tracker created and updated: `docs/phases/PHASE_TRACKER.md`
- Frontend decision: frontend platform is not required for doctrine baseline; any future frontend must be read-only documentation visualization only.

## Phase 1 — Portfolio Doctrine Baseline

**Goal:** Define customer-offerable suites, Shared Trust Fabric, Composition Layer doctrine, SENTINEL control-point doctrine, authority separation, and product packaging boundaries.

### Checklist

- [x] Create `docs/portfolio/SECURETHECLOUD_ENTERPRISE_PRODUCT_PORTFOLIO.md`
- [x] Create `docs/portfolio/SHARED_TRUST_FABRIC.md`
- [x] Create `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md`
- [x] Create `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`
- [x] Create `docs/portfolio/SUITE_CATALOG.md`
- [x] Create `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md`
- [x] Define four customer-offerable suites
- [x] Define Shared Trust Fabric
- [x] Freeze Composition Layer rules
- [x] Canonicalize SENTINEL control-point doctrine
- [x] Record Phase 1 evidence

### Evidence

- Four customer-offerable suites frozen:
  - SecureTheCloud Agent Blackbox Suite
  - SecureTheCloud Compliance Evidence Suite
  - SecureTheCloud Runtime Assurance Suite
  - SecureTheCloud Risk Intelligence Suite
- Shared Trust Fabric defined as a shared substrate, not a fifth customer-offerable suite.
- Composition Layer rule frozen: composition may package and present but may not create authority or bypass SENTINEL.
- SENTINEL control-point doctrine canonicalized for runtime-impacting allow, deny, admission, enforcement, and production-control outcomes.
- Product packaging boundaries defined: packaging is not authority and must not merge suite roles.
- Agent sharing rule clarified: share the repo and `AGENTS.md` immediately; share Markdown doctrine after Phase 1; share machine-readable JSON contracts only after Phase 3 creates and validates them.

## Phase 2 — Module Authority Matrix

**Goal:** Assign every module to category, status, authority type, callable interfaces, forbidden actions, and suite membership.

### Checklist

- [x] Create `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`
- [x] Create `docs/portfolio/STATUS_TAXONOMY.md`
- [x] Define module categories
- [x] Define module status values
- [x] Define module authority types
- [x] Define callable interfaces
- [x] Define forbidden actions per module
- [x] Assign all modules to suites, Shared Trust Fabric, or internal doctrine ownership
- [x] Record Phase 2 evidence

### Evidence

- Status taxonomy created for lifecycle status, suite/packaging status, authority status, module categories, evidence status, and interface status.
- Module authority matrix created with module IDs, categories, lifecycle status, authority type, callable interfaces, forbidden actions, and membership.
- Default unregistered-module rule frozen: unregistered modules are `unregistered_candidate` with `no_runtime_authority`.
- Universal forbidden actions recorded, including token issuance, authorization grants, runtime sessions, provider/Kubernetes mutation, live backend exposure, production traffic cutover, runtime enforcement, and SENTINEL bypass.
- Suite membership coverage recorded for all baseline modules across the four suites, Shared Trust Fabric, internal doctrine, and future candidates.
- Phase 3 contract paths remain reserved placeholders until schemas and JSON contracts are created and validated.

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
