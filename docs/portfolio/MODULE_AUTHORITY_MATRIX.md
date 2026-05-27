# Module Authority Matrix

**Status:** Phase 2 / Module Authority Matrix
**Doctrine Version:** 0.2.0-authority-baseline
**Last Updated:** 2026-05-23

## Purpose

This document defines baseline authority for SecureTheCloud modules.

Every registered module must declare:

- module ID
- category
- lifecycle status
- authority status
- callable interfaces
- forbidden actions
- suite membership or Shared Trust Fabric ownership

## Canonical rule

No module may claim authority outside this matrix.

Suite membership does not create authority.

Packaging does not create authority.

Composition does not create authority.

Evidence does not create enforcement authority.

Explanation does not create authorization authority.

Runtime-impacting allow, deny, admission, policy-decision, enforcement, and production-control outcomes remain under SENTINEL control-point doctrine.

## Default rule

Any module not listed here is an `unregistered_candidate` with `no_runtime_authority`.

Unregistered modules must not be customer-packaged, granted runtime authority, used as canonical doctrine, or described as part of an approved suite.

## Authority type definitions

| Authority type | Meaning |
|---|---|
| `doctrine_only` | May define doctrine, boundaries, and governance rules; cannot execute runtime behavior. |
| `shared_contract` | May define shared machine-readable contracts and schemas; no runtime behavior by itself. |
| `composition_only` | May package, assemble, and present approved modules; cannot create authority. |
| `evidence_read_only` | May read and present approved evidence; cannot mutate runtime systems. |
| `evidence_packaging` | May package approved evidence into reports, manifests, or bundles; cannot create new evidence truth. |
| `explanation_read_only` | May explain decisions, posture, or traceability; cannot authorize or enforce. |
| `risk_scoring_read_only` | May summarize or score risk; cannot create policy outcomes. |
| `control_point_canonical` | Canonical control-point doctrine applies; live runtime activation still requires explicit approval. |
| `runtime_enforcement_blocked` | Runtime enforcement is explicitly blocked. |

## Callable interface taxonomy

| Interface | Meaning |
|---|---|
| `read_doctrine` | Read doctrine files and locked rules. |
| `read_registry` | Read module, suite, authority, or status registry data. |
| `read_evidence` | Read approved evidence sources. |
| `present_customer_safe` | Present customer-safe views or summaries. |
| `present_auditor_safe` | Present auditor-facing evidence views. |
| `package_evidence` | Package approved evidence into manifests, reports, or bundles. |
| `compose_package` | Assemble approved suites/modules for presentation without changing authority. |
| `explain_posture` | Explain posture, readiness, boundaries, or decisions. |
| `score_risk` | Produce read-only risk scoring or risk narrative. |
| `control_point_reference` | Reference SENTINEL control-point doctrine without executing enforcement. |
| `none` | No callable interface is approved. |

## Universal forbidden actions

Unless a module row explicitly grants otherwise, all modules are forbidden from:

- issuing tokens
- granting authorization
- creating runtime sessions
- mutating provider resources
- mutating Kubernetes resources
- executing Helm deployments
- exposing live backend APIs
- performing production traffic cutover
- enforcing runtime allow/deny decisions
- bypassing SENTINEL
- inventing suite membership
- inventing authority
- inventing status taxonomy values
- claiming SOC 2 certification from SOC 2-aligned documentation

## Authority matrix

| Module ID | Module name | Category | Lifecycle status | Authority type | Callable interfaces | Forbidden actions | Membership |
|---|---|---|---|---|---|---|---|
| `doctrine_control_plane` | Doctrine Control Plane | `doctrine_control` | `evidence_recorded` | `doctrine_only` | `read_doctrine`, `read_registry` | runtime adapter code; Helm templates; UI/website assets; module-specific enforcement logic; live backend integration | Internal doctrine only |
| `portfolio_doctrine` | Enterprise Product Portfolio Doctrine | `doctrine_control` | `evidence_recorded` | `doctrine_only` | `read_doctrine` | runtime authority; suite execution; customer enforcement claims | Internal doctrine only |
| `shared_trust_fabric` | Shared Trust Fabric | `shared_trust_fabric` | `evidence_recorded` | `shared_contract` | `read_registry`, `read_doctrine` | standalone customer suite packaging; runtime mutation; enforcement | Shared Trust Fabric |
| `composition_layer` | Composition Layer | `composition_layer` | `evidence_recorded` | `composition_only` | `compose_package`, `present_customer_safe`, `read_registry` | creating authority; bypassing SENTINEL; runtime enforcement; token issuance | Shared Trust Fabric / all suites dependency |
| `sentinel_control_point` | SENTINEL Control Point Doctrine | `control_point` | `evidence_recorded` | `control_point_canonical` | `control_point_reference`, `read_doctrine` | live enforcement claims without phase approval; local substitute control points; silent bypass | Runtime Assurance Suite / Shared Trust Fabric dependency |
| `suite_catalog` | Suite Catalog | `shared_trust_fabric` | `evidence_recorded` | `shared_contract` | `read_registry`, `read_doctrine` | inventing customer suites; runtime authority; enforcement claims | Shared Trust Fabric |
| `module_authority_matrix` | Module Authority Matrix | `shared_trust_fabric` | `evidence_recorded` | `shared_contract` | `read_registry`, `read_doctrine` | granting runtime authority without doctrine update; local overrides | Shared Trust Fabric |
| `status_taxonomy` | Status Taxonomy | `shared_trust_fabric` | `evidence_recorded` | `shared_contract` | `read_registry`, `read_doctrine` | inventing local statuses; runtime authority | Shared Trust Fabric |
| `product_packaging_boundaries` | Product Packaging Boundaries | `doctrine_control` | `evidence_recorded` | `doctrine_only` | `read_doctrine`, `compose_package` | merging suite roles; expanding authority through packaging; SOC 2 certification claims | Internal doctrine / all suites dependency |
| `agent_blackbox_suite_shell` | Agent Blackbox Suite Shell | `suite_shell` | `doctrine_defined` | `composition_only` | `present_customer_safe`, `compose_package`, `explain_posture` | runtime mutation; authorization; enforcement; SENTINEL bypass | SecureTheCloud Agent Blackbox Suite |
| `agent_decision_evidence` | Agent Decision Evidence | `agent_evidence` | `doctrine_defined` | `evidence_read_only` | `read_evidence`, `present_customer_safe`, `explain_posture` | changing decisions; authorizing agents; enforcing controls; mutating evidence source truth | SecureTheCloud Agent Blackbox Suite |
| `agent_handoff_context` | Agent Handoff Context | `agent_evidence` | `doctrine_defined` | `evidence_read_only` | `read_evidence`, `present_customer_safe`, `explain_posture` | marking handoffs used; runtime handoff mutation; authorization; enforcement | SecureTheCloud Agent Blackbox Suite |
| `agent_trust_intelligence_summary` | Agent Trust Intelligence Summary | `agent_evidence` | `doctrine_defined` | `explanation_read_only` | `read_evidence`, `present_customer_safe`, `explain_posture` | inventing evidence; producing enforcement outcomes; issuing trust credentials | SecureTheCloud Agent Blackbox Suite / Risk Intelligence Suite |
| `compliance_evidence_suite_shell` | Compliance Evidence Suite Shell | `suite_shell` | `doctrine_defined` | `composition_only` | `present_customer_safe`, `present_auditor_safe`, `compose_package` | runtime enforcement; authorization; SOC 2 certification claims | SecureTheCloud Compliance Evidence Suite |
| `soc2_alignment_evidence` | SOC 2 Alignment Evidence | `compliance_evidence` | `doctrine_defined` | `evidence_read_only` | `read_evidence`, `present_auditor_safe`, `explain_posture` | claiming SOC 2 certification; mutating controls; runtime enforcement | SecureTheCloud Compliance Evidence Suite |
| `soc2_control_traceability` | SOC 2 Control Traceability | `compliance_evidence` | `doctrine_defined` | `evidence_read_only` | `read_evidence`, `present_auditor_safe`, `explain_posture` | certifying audit results; creating runtime controls; overriding authority matrix | SecureTheCloud Compliance Evidence Suite |
| `audit_workspace` | Auditor Evidence Workspace | `evidence_surface` | `doctrine_defined` | `evidence_read_only` | `read_evidence`, `present_auditor_safe` | new export generation unless approved; runtime enforcement; token/session issuance | SecureTheCloud Compliance Evidence Suite |
| `soc2_export_manifest` | SOC 2 Export Manifest | `evidence_export` | `doctrine_defined` | `evidence_packaging` | `package_evidence`, `present_auditor_safe` | creating evidence truth; signing bundles unless approved; claiming certification | SecureTheCloud Compliance Evidence Suite |
| `pdf_report_package` | PDF Report Package | `evidence_export` | `doctrine_defined` | `evidence_packaging` | `package_evidence`, `present_customer_safe`, `present_auditor_safe` | regenerating production reports without approval; signing; enforcement claims | SecureTheCloud Compliance Evidence Suite / Agent Blackbox Suite |
| `signed_bundle_manifest` | Signed Bundle Manifest | `evidence_export` | `doctrine_defined` | `evidence_packaging` | `package_evidence`, `present_auditor_safe` | cryptographic signing unless explicitly approved; changing evidence source truth; enforcement claims | SecureTheCloud Compliance Evidence Suite |
| `runtime_assurance_suite_shell` | Runtime Assurance Suite Shell | `suite_shell` | `doctrine_defined` | `composition_only` | `present_customer_safe`, `compose_package`, `control_point_reference` | live enforcement without approval; SENTINEL bypass; authorization claims | SecureTheCloud Runtime Assurance Suite |
| `runtime_boundary_readiness` | Runtime Boundary Readiness | `runtime_assurance` | `doctrine_defined` | `explanation_read_only` | `read_evidence`, `explain_posture`, `control_point_reference` | activating enforcement; traffic cutover; backend API exposure; runtime mutation | SecureTheCloud Runtime Assurance Suite |
| `sentinel_readiness_reference` | SENTINEL Readiness Reference | `runtime_assurance` | `doctrine_defined` | `control_point_canonical` | `control_point_reference`, `explain_posture` | live allow/deny execution without approval; bypassing doctrine; production enforcement claims | SecureTheCloud Runtime Assurance Suite |
| `risk_intelligence_suite_shell` | Risk Intelligence Suite Shell | `suite_shell` | `doctrine_defined` | `composition_only` | `present_customer_safe`, `compose_package`, `score_risk` | policy enforcement; authorization; runtime mutation | SecureTheCloud Risk Intelligence Suite |
| `risk_posture_narrative` | Risk Posture Narrative | `risk_intelligence` | `doctrine_defined` | `risk_scoring_read_only` | `read_evidence`, `score_risk`, `present_customer_safe`, `explain_posture` | creating policy outcomes; enforcing controls; mutating risk evidence | SecureTheCloud Risk Intelligence Suite |
| `authority_overlap_detector` | Authority Overlap Detector | `risk_intelligence` | `doctrine_defined` | `risk_scoring_read_only` | `read_registry`, `score_risk`, `explain_posture` | changing authority assignments; blocking modules; enforcing controls | SecureTheCloud Risk Intelligence Suite / Shared Trust Fabric dependency |
| `agent_risk_exchange_candidate` | Agent Risk Exchange Candidate | `integration_candidate` | `future_candidate` | `runtime_enforcement_blocked` | `none` | implementation; runtime exchange; provider mutation; enforcement; customer packaging as active module | Future candidate only |
| `frontend_doctrine_portal_candidate` | Read-Only Doctrine Portal Candidate | `integration_candidate` | `future_candidate` | `composition_only` | `present_customer_safe`, `read_doctrine`, `read_registry` | becoming source of truth; runtime behavior; enforcement; editing doctrine outside Git | Future candidate only |

## Suite membership coverage

### SecureTheCloud Agent Blackbox Suite

- `agent_blackbox_suite_shell`
- `agent_decision_evidence`
- `agent_handoff_context`
- `agent_trust_intelligence_summary`
- `pdf_report_package`

### SecureTheCloud Compliance Evidence Suite

- `compliance_evidence_suite_shell`
- `soc2_alignment_evidence`
- `soc2_control_traceability`
- `audit_workspace`
- `soc2_export_manifest`
- `pdf_report_package`
- `signed_bundle_manifest`

### SecureTheCloud Runtime Assurance Suite

- `runtime_assurance_suite_shell`
- `runtime_boundary_readiness`
- `sentinel_readiness_reference`
- `sentinel_control_point`

### SecureTheCloud Risk Intelligence Suite

- `risk_intelligence_suite_shell`
- `risk_posture_narrative`
- `authority_overlap_detector`
- `agent_trust_intelligence_summary`

### Shared Trust Fabric

- `shared_trust_fabric`
- `composition_layer`
- `suite_catalog`
- `module_authority_matrix`
- `status_taxonomy`
- `authority_overlap_detector`

### Internal doctrine only

- `doctrine_control_plane`
- `portfolio_doctrine`
- `product_packaging_boundaries`

### Future candidates only

- `agent_risk_exchange_candidate`
- `frontend_doctrine_portal_candidate`

## Phase 3 relationship

This matrix is the human-readable source for Phase 2.

Phase 3 will create machine-readable contracts for:

- `contracts/portfolio/module_registry.json`
- `contracts/portfolio/authority_matrix.json`
- `contracts/portfolio/suite_catalog.json`

Until Phase 3 is complete, these JSON contract paths are reserved placeholders, not active integration dependencies.

## Phase 7 Aegis Runtime / RiskDNA authority additions

Module ID	Module name	Category	Lifecycle status	Authority type	Callable interfaces	Forbidden actions	Membership
aegis_runtime_signal_context	Aegis Runtime Signal Context	runtime_assurance	evidence_recorded	explanation_read_only	read_evidence, present_customer_safe, explain_posture, control_point_reference	token issuance; authorization; runtime session creation; provider mutation; Kubernetes mutation; Helm execution; OPA replacement; SENTINEL bypass; production enforcement; independent package claim	SecureTheCloud Runtime Assurance Suite / SecureTheCloud Compliance Evidence Suite / SecureTheCloud Agent Blackbox Suite / SecureTheCloud Risk Intelligence Suite
riskdna_runtime_risk_context	RiskDNA Runtime Risk Context	risk_intelligence	evidence_recorded	risk_scoring_read_only	read_evidence, score_risk, present_customer_safe, explain_posture	authorization; policy outcome creation; runtime mutation; token issuance; runtime session creation; OPA replacement; SENTINEL bypass; production enforcement; independent package claim	SecureTheCloud Risk Intelligence Suite / SecureTheCloud Runtime Assurance Suite

Phase 7 preserves the canonical rule that suite membership does not create authority, packaging does not create authority, composition does not create authority, evidence does not create enforcement authority, and explanation does not create authorization authority.
