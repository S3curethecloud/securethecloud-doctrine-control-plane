# SOC 2 Evidence Register

**Status:** Phase 4 / SOC 2 Alignment Evidence
**Doctrine Version:** 0.4.0-soc2-alignment-baseline
**Last Updated:** 2026-05-23

## Purpose

This register identifies SOC 2-aligned evidence produced by the Doctrine Control Plane.

It is an evidence inventory for readiness and traceability. It is not a SOC 2 report, certification, or assertion of operating effectiveness.

## Evidence classification

| Evidence type | Meaning |
|---|---|
| Governance design evidence | Shows that governance rules and boundaries are defined. |
| Contract evidence | Shows that machine-readable doctrine exists. |
| Validation evidence | Shows that contracts are checked for consistency. |
| Change-management evidence | Shows that doctrine changes are phase-gated and reviewable. |
| Boundary evidence | Shows what is explicitly out of scope or forbidden. |

## Evidence inventory

| Evidence ID | Artifact | Evidence type | SOC 2 alignment | Owner | Status |
|---|---|---|---|---|---|
| SOC2-EV-001 | `README.md` | Governance design evidence | Control environment, information and communication | Doctrine Control Plane | Active |
| SOC2-EV-002 | `AGENTS.md` | Governance design evidence | Information and communication, control activities | Doctrine Control Plane | Active |
| SOC2-EV-003 | `GOVERNANCE.md` | Governance design evidence | Control environment, change management | Doctrine Control Plane | Active |
| SOC2-EV-004 | `doctrine.lock.md` | Boundary evidence | Control environment, change management, risk mitigation | Doctrine Control Plane | Active |
| SOC2-EV-005 | `CHANGELOG.md` | Change-management evidence | Change management | Doctrine Control Plane | Active |
| SOC2-EV-006 | `CODEOWNERS` | Control activity evidence | Control activities, change management | Doctrine Control Plane | Active |
| SOC2-EV-007 | `.github/pull_request_template.md` | Control activity evidence | Control activities, change management | Doctrine Control Plane | Active |
| SOC2-EV-008 | `docs/phases/PHASE_TRACKER.md` | Change-management evidence | Monitoring activities, change management | Doctrine Control Plane | Active |
| SOC2-EV-009 | `docs/portfolio/SECURETHECLOUD_ENTERPRISE_PRODUCT_PORTFOLIO.md` | Governance design evidence | Information and communication, risk assessment | Doctrine Control Plane | Active |
| SOC2-EV-010 | `docs/portfolio/SHARED_TRUST_FABRIC.md` | Governance design evidence | Information and communication, control environment | Doctrine Control Plane | Active |
| SOC2-EV-011 | `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md` | Boundary evidence | Risk assessment, control activities | Doctrine Control Plane | Active |
| SOC2-EV-012 | `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md` | Boundary evidence | Security, risk mitigation, system operations boundary | Doctrine Control Plane | Active |
| SOC2-EV-013 | `docs/portfolio/SUITE_CATALOG.md` | Governance design evidence | Information and communication | Doctrine Control Plane | Active |
| SOC2-EV-014 | `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md` | Boundary evidence | Risk assessment, information and communication | Doctrine Control Plane | Active |
| SOC2-EV-015 | `docs/portfolio/STATUS_TAXONOMY.md` | Contract evidence | Processing integrity, information and communication | Doctrine Control Plane | Active |
| SOC2-EV-016 | `docs/portfolio/MODULE_AUTHORITY_MATRIX.md` | Boundary evidence | Security, risk assessment, logical authority boundary | Doctrine Control Plane | Active |
| SOC2-EV-017 | `schemas/portfolio/*.schema.json` | Contract evidence | Processing integrity | Doctrine Control Plane | Active |
| SOC2-EV-018 | `contracts/portfolio/*.json` | Contract evidence | Processing integrity, information and communication | Doctrine Control Plane | Active |
| SOC2-EV-019 | `tools/validate_doctrine_contracts.py` | Validation evidence | Processing integrity, control activities | Doctrine Control Plane | Active |
| SOC2-EV-020 | `.github/workflows/doctrine-validate.yml` | Validation evidence | Processing integrity, monitoring activities | Doctrine Control Plane | Active |
| SOC2-EV-021 | `docs/phases/PHASE_3_SHARED_MACHINE_READABLE_CONTRACTS.md` | Validation evidence | Change management, processing integrity | Doctrine Control Plane | Active |
| SOC2-EV-022 | `docs/soc2/SOC2_ALIGNMENT_OVERVIEW.md` | Governance design evidence | SOC 2 readiness mapping | Doctrine Control Plane | Active |
| SOC2-EV-023 | `docs/soc2/SOC2_CONTROL_TRACEABILITY.md` | Traceability evidence | SOC 2 readiness mapping | Doctrine Control Plane | Active |
| SOC2-EV-024 | `docs/soc2/SOC2_EVIDENCE_REGISTER.md` | Evidence inventory | SOC 2 readiness mapping | Doctrine Control Plane | Active |
| SOC2-EV-025 | `docs/soc2/SOC2_CHANGE_MANAGEMENT.md` | Change-management evidence | Change management readiness | Doctrine Control Plane | Pending until created |

## Evidence rules

Evidence entries must remain accurate to repository contents.

Evidence must not claim production operating effectiveness unless operating evidence exists for a defined period.

Evidence must not claim certification unless an independent audit report exists.

Evidence derived from machine-readable contracts must remain consistent with Markdown doctrine and `doctrine.lock.md`.

## Evidence update triggers

Update this register when:

- a doctrine artifact is added, removed, or renamed;
- a schema or contract is added, removed, or renamed;
- a validation workflow changes;
- authority boundaries change;
- suite membership changes;
- SENTINEL control-point doctrine changes;
- product packaging boundaries change;
- SOC 2 traceability expands;
- evidence status changes.

## Current readiness conclusion

The Doctrine Control Plane has design-level SOC 2-aligned evidence for governance, authority separation, contract consistency, and change traceability.

It does not yet provide operating-effectiveness evidence for a SOC 2 Type 2 report.

## Phase 7 evidence extension

Evidence ID	Artifact	Evidence type	SOC 2 alignment	Owner	Status
SOC2-EV-026	docs/phases/PHASE_7_AEGIS_RUNTIME_RISKDNA_DOCTRINE_DELTA.md	Boundary evidence	Aegis Runtime / RiskDNA readiness boundary	Doctrine Control Plane	Active
SOC2-EV-027	contracts/portfolio/module_registry.json and contracts/portfolio/authority_matrix.json Phase 7 records	Contract evidence	Machine-readable Aegis/RiskDNA authority parity	Doctrine Control Plane	Active

## Phase 8 downstream adoption evidence extension

| Evidence ID | Artifact | Evidence type | SOC 2 alignment | Owner | Status |
|---|---|---|---|---|---|
| SOC2-EV-028 | `docs/adoption/DOWNSTREAM_DOCTRINE_ADOPTION_REGISTER.md` | Adoption evidence register | Information and communication, change management, boundary evidence | Doctrine Control Plane | Active |
| SOC2-EV-029 | `docs/phases/PHASE_8_DOWNSTREAM_DOCTRINE_ADOPTION_EVIDENCE_CLOSURE.md` | Phase evidence | Change management and downstream adoption traceability | Doctrine Control Plane | Active |

## Phase 8I pending adoption evidence extension

| Evidence ID | Artifact | Evidence type | SOC 2 alignment | Owner | Status |
|---|---|---|---|---|---|
| SOC2-EV-030 | `docs/adoption/DOWNSTREAM_DOCTRINE_ADOPTION_REGISTER.md` Phase 8I row | Adoption backlog evidence | Information and communication, change management, boundary evidence | Doctrine Control Plane | Pending downstream adoption |

## Final Phase 8 adoption closure

Phase 8 downstream adoption is complete across the known downstream repositories:

- Phase 8A - Aegis/RiskDNA runtime: df83c3e
- Phase 8B - SENTINEL: 3054784
- Phase 8C - ASZ: b0f6459
- Phase 8D - Blackbox: 0306170
- Phase 8E - Risk Exchange: ce40bf4
- Phase 8F - SAF-P: 64738e6
- Phase 8G - SageMaker Risk Intelligence: 9ea6cbe
- Phase 8H - Secret Vault: 3259def
- Phase 8I - Intelligence Core: ea922ea

This final closure is evidence/register-only. It does not grant runtime authority, token issuance, session creation, authorization behavior, OPA replacement, SENTINEL bypass, Vault reference resolution, secret mutation, SageMaker runtime execution, ML authority, Helm packaging, production routing, production enforcement, SOC 2 certification, or production operating effectiveness.
