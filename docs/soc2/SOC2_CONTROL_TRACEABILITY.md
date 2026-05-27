# SOC 2 Control Traceability

**Status:** Phase 4 / SOC 2 Alignment Evidence
**Doctrine Version:** 0.4.0-soc2-alignment-baseline
**Last Updated:** 2026-05-23

## Purpose

This document maps SecureTheCloud doctrine artifacts to SOC 2-aligned control themes and readiness evidence.

It is a traceability index, not an audit opinion, certification, or assertion of operating effectiveness.

## Traceability principles

- Every authority claim must map to doctrine.
- Every suite claim must map to the suite catalog.
- Every module claim must map to the module registry and authority matrix.
- Every composition claim must preserve Composition Layer doctrine.
- Every runtime-impacting control claim must preserve SENTINEL control-point doctrine.
- Every SOC 2 claim must remain readiness-oriented unless an independent audit supports certification or attestation.

## Control traceability matrix

| Control theme | Doctrine artifact | Evidence produced | Boundary |
|---|---|---|---|
| Control environment | `GOVERNANCE.md`, `doctrine.lock.md`, `AGENTS.md` | Governance rules, canonical source-of-truth statement, agent rules | Does not prove operating effectiveness. |
| Information and communication | `README.md`, `AGENTS.md`, `docs/portfolio/*`, `contracts/portfolio/*.json` | Human-readable and machine-readable doctrine | Agents must not fork local doctrine. |
| Risk assessment | `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`, `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md` | Authority boundaries, forbidden actions, unregistered-module no-authority rule | Does not execute runtime controls. |
| Control activities | `.github/pull_request_template.md`, `CODEOWNERS`, `tools/validate_doctrine_contracts.py`, `.github/workflows/doctrine-validate.yml` | PR checklist, ownership, contract validation | Validation is repository-scope only. |
| Change management | `CHANGELOG.md`, `docs/phases/PHASE_TRACKER.md`, `doctrine.lock.md` | Phase history, doctrine versioning, change evidence | Does not replace enterprise change board approval. |
| Logical authority boundary | `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`, `contracts/portfolio/authority_matrix.json` | Authority types and forbidden actions | No default authorization, token, or session authority. |
| System operations boundary | `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`, `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md` | Runtime non-bypass doctrine and composition restrictions | No production enforcement in this repository. |
| Monitoring readiness | `docs/phases/*`, Git history, validation workflow | Evidence history and validation results | Monitoring is repo-governance level only. |
| Risk mitigation | `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`, `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md` | Non-bypass and non-mispackaging rules | Does not activate SENTINEL enforcement. |
| Evidence consistency | `contracts/portfolio/*.json`, `schemas/portfolio/*.schema.json` | Machine-readable shared contracts | Contracts must stay aligned with Markdown doctrine. |

## Trust Services Category mapping

### Security

Relevant doctrine evidence:

- `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`
- `contracts/portfolio/authority_matrix.json`
- `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`
- `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md`
- `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md`

Security alignment:

- Authority is explicit.
- Forbidden actions are explicit.
- Unregistered modules receive no authority.
- Runtime-impacting control decisions remain under SENTINEL doctrine.
- Packaging cannot expand authority.

### Availability

Relevant doctrine evidence:

- `docs/portfolio/SUITE_CATALOG.md`
- `contracts/portfolio/suite_catalog.json`
- `contracts/portfolio/module_registry.json`
- `docs/phases/PHASE_TRACKER.md`

Availability alignment:

- Suites and dependencies are documented.
- Shared Trust Fabric dependencies are explicit.
- Change state is traceable through phases.
- The doctrine control plane avoids runtime dependencies.

### Processing Integrity

Relevant doctrine evidence:

- `schemas/portfolio/*.schema.json`
- `contracts/portfolio/*.json`
- `tools/validate_doctrine_contracts.py`
- `.github/workflows/doctrine-validate.yml`

Processing integrity alignment:

- Contract files are structured.
- Contract changes are validated.
- Module registry and authority matrix parity are checked.
- Status taxonomy values are canonical.

### Confidentiality

Relevant doctrine evidence:

- `AGENTS.md`
- `GOVERNANCE.md`
- `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`

Confidentiality alignment:

- Secrets and credentials are out of scope.
- Live backend integrations are out of scope.
- Evidence mutation is forbidden unless future doctrine approves.
- Customer-visible claims must be package-bound and evidence-bound.

### Privacy

Relevant doctrine evidence:

- `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`
- `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md`
- future privacy-specific evidence artifacts

Privacy alignment:

- Privacy-sensitive claims require approved evidence sources.
- No module may invent evidence or customer data handling authority.
- Privacy-specific operating controls remain future scope unless separately documented.

## Gap statement

This repository currently provides governance design evidence.

It does not yet provide:

- production operating effectiveness evidence;
- customer environment control evidence;
- independent auditor testing;
- privacy-specific processing activity records;
- production access review evidence;
- incident response execution evidence;
- vendor management evidence;
- data retention enforcement evidence.

These gaps are intentional unless future phases approve additional evidence scope.

## Phase 7 Aegis Runtime / RiskDNA traceability extension

Control theme	Doctrine artifact	Evidence produced	Boundary
Aegis Runtime boundary	docs/phases/PHASE_7_AEGIS_RUNTIME_RISKDNA_DOCTRINE_DELTA.md, docs/portfolio/MODULE_AUTHORITY_MATRIX.md, contracts/portfolio/authority_matrix.json	Aegis Runtime signal/evidence/readiness authority boundary	Readiness evidence only; no runtime authority or SOC 2 certification.
RiskDNA boundary	docs/phases/PHASE_7_AEGIS_RUNTIME_RISKDNA_DOCTRINE_DELTA.md, docs/portfolio/MODULE_AUTHORITY_MATRIX.md, contracts/portfolio/authority_matrix.json	RiskDNA risk-scoring/readiness authority boundary	Risk scoring only; no authorization, OPA replacement, or enforcement.
Packaging reality	docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md	No independent Helm/package/production routing claim	Packaging remains non-authority.
SENTINEL preservation	docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md	Aegis/RiskDNA context cannot bypass SENTINEL	SENTINEL remains canonical for runtime-impacting decisions.

## Phase 8 downstream adoption traceability

| Control theme | Doctrine artifact | Evidence produced | Boundary |
|---|---|---|---|
| Downstream doctrine adoption | `docs/adoption/DOWNSTREAM_DOCTRINE_ADOPTION_REGISTER.md` | Completed adoption evidence and pending adoption backlog | Adoption evidence only; no runtime authority granted. |
| Change management | `docs/phases/PHASE_8_DOWNSTREAM_DOCTRINE_ADOPTION_EVIDENCE_CLOSURE.md` | Phase-gated downstream adoption closure | Does not prove production operating effectiveness. |
| Information and communication | Downstream `AGENTS.md` adoption pointers | Canonical doctrine consumption path | Downstream repos must not create local substitute doctrine. |

## Phase 8I Intelligence Core pending adoption traceability

| Control theme | Doctrine artifact | Evidence produced | Boundary |
|---|---|---|---|
| Intelligence Core downstream adoption backlog | `docs/adoption/DOWNSTREAM_DOCTRINE_ADOPTION_REGISTER.md` | Pending Intelligence Core adoption target | Pending only; no Aegis/RiskDNA awareness, runtime authority, or intelligence claim is granted until downstream adoption is committed. |

## Phase 9B claims-safe wording traceability

Phase 9B adds a claims-safe wording standard and boundary language to high-impact portfolio and SOC 2 documents.

Control alignment:

- Information and communication: customer-facing wording is bounded by canonical doctrine.
- Change management: claims-safe wording is tracked as a governed documentation change.
- Risk assessment: high-risk claim categories are classified before correction.
- Monitoring: future customer-facing claims should use the Phase 9B standard.

This traceability does not claim SOC 2 certification or production operating effectiveness.
