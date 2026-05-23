# Status Taxonomy

**Status:** Phase 2 / Module Authority Matrix
**Doctrine Version:** 0.2.0-authority-baseline
**Last Updated:** 2026-05-23

## Purpose

This document defines the canonical status values used by SecureTheCloud doctrine, suites, modules, shared fabric dependencies, authority boundaries, evidence posture, and product packaging.

Agents must use these values when describing module state, suite state, authority state, or evidence state.

## Canonical rule

Agents must not invent local status values.

If a status value is missing, this taxonomy must be updated before downstream repositories or agents use the new value.

## Module lifecycle status

| Status | Meaning | Runtime implication |
|---|---|---|
| `doctrine_defined` | The module is defined in doctrine but may not have implementation artifacts in this repository. | No runtime authority by itself. |
| `planned` | The module is planned but not yet implemented or packaged. | No runtime authority. |
| `implemented_static` | The module exists as static documentation, UI, metadata, schema, or read-only artifact. | No runtime mutation authority. |
| `implementation_complete` | The module implementation is complete for its approved scope. | Authority remains limited to the authority matrix. |
| `evidence_recorded` | Evidence for the approved scope has been recorded. | Evidence does not imply runtime authority. |
| `active_read_only` | The module may be used for read-only evidence, explanation, or presentation. | Read-only only. |
| `active_runtime_approved` | Runtime-impacting behavior has been explicitly approved by doctrine and phase evidence. | Runtime authority only as scoped. |
| `blocked` | The module or action is intentionally blocked by doctrine. | Must not execute. |
| `deprecated` | The module is retained for history but should not be used for new work. | No new authority. |
| `unregistered_candidate` | The module has not been accepted into the module registry. | No authority; cannot be packaged as canonical. |

## Suite and packaging status

| Status | Meaning |
|---|---|
| `customer_offerable` | May be offered as a customer-facing suite. |
| `shared_fabric_dependency` | Supports customer-offerable suites but is not a standalone customer suite. |
| `internal_doctrine_only` | Internal doctrine/control-plane artifact; not customer-offerable. |
| `future_candidate` | May be evaluated later but is not currently accepted as customer-offerable. |
| `not_customer_offerable` | Must not be packaged as a customer suite. |

## Authority status

| Status | Meaning |
|---|---|
| `no_runtime_authority` | No runtime-impacting authority exists. |
| `doctrine_only` | May define rules, boundaries, and contracts but cannot execute runtime behavior. |
| `shared_contract` | May define shared machine-readable contract expectations. |
| `composition_only` | May assemble, route, or present approved modules without creating authority. |
| `evidence_read_only` | May read, summarize, and present evidence from approved sources. |
| `evidence_packaging` | May package approved evidence for customer or auditor consumption. |
| `explanation_read_only` | May explain state, posture, decisions, or traceability without control effect. |
| `risk_scoring_read_only` | May score or summarize risk without creating policy outcomes. |
| `control_point_canonical` | Canonical control-point doctrine applies; runtime activation still requires explicit approval. |
| `runtime_enforcement_approved` | Runtime enforcement is approved only for the exact scope documented. |
| `runtime_enforcement_blocked` | Runtime enforcement is explicitly blocked. |

## Module category taxonomy

| Category | Meaning |
|---|---|
| `doctrine_control` | Owns doctrine, boundaries, contracts, phase state, and governance rules. |
| `shared_trust_fabric` | Shared doctrine, registry, schema, metadata, contract, or taxonomy substrate. |
| `composition_layer` | Packaging, presentation, and assembly layer that preserves authority boundaries. |
| `control_point` | Canonical control-point doctrine or future enforcement decision boundary. |
| `suite_shell` | Customer-offerable suite boundary and product shell. |
| `agent_evidence` | Agent behavior, decision, handoff, or explanation evidence. |
| `compliance_evidence` | Audit, SOC 2-aligned, compliance, or control evidence module. |
| `runtime_assurance` | Runtime assurance, enforcement-readiness, or production-boundary module. |
| `risk_intelligence` | Risk posture, trust score, control-gap, or executive risk narrative module. |
| `evidence_surface` | Read-only evidence display or evidence navigation surface. |
| `evidence_export` | Evidence packaging, manifest, report, bundle, or export module. |
| `integration_candidate` | Future or external integration candidate with no authority until accepted. |

## Evidence status

| Status | Meaning |
|---|---|
| `not_applicable` | No evidence status applies. |
| `evidence_required` | Evidence must be recorded before completion. |
| `evidence_recorded` | Evidence has been recorded for the approved scope. |
| `soc2_trace_pending` | SOC 2 traceability is required but not yet recorded. |
| `soc2_trace_recorded` | SOC 2 traceability has been recorded. |

## Interface status

| Status | Meaning |
|---|---|
| `read_only_reference` | Interface may be referenced or read, but not mutated. |
| `read_only_query` | Interface may query approved data sources without mutation. |
| `customer_presentation` | Interface may present customer-safe information. |
| `auditor_presentation` | Interface may present auditor-safe evidence. |
| `contract_export` | Interface may export approved doctrine or evidence contracts. |
| `runtime_control_candidate` | Candidate runtime control interface; blocked until explicit approval. |
| `runtime_control_active` | Runtime control interface approved for exact documented scope. |
| `forbidden` | Interface must not be called or implemented. |

## Default rule for unregistered modules

Any module not listed in `docs/portfolio/MODULE_AUTHORITY_MATRIX.md` is `unregistered_candidate` with `no_runtime_authority`.

Unregistered modules must not be customer-packaged, granted authority, used as canonical doctrine, or described as part of a suite until accepted into the authority matrix.

## Phase 3 relationship

This taxonomy is the human-readable source for Phase 2.

Phase 3 will create the machine-readable contract at:

`contracts/portfolio/status_taxonomy.json`
