# SOC 2 Alignment Overview

**Status:** Phase 4 / SOC 2 Alignment Evidence
**Doctrine Version:** 0.4.0-soc2-alignment-baseline
**Last Updated:** 2026-05-23

## Purpose

This document defines how the SecureTheCloud Doctrine Control Plane supports SOC 2-aligned readiness evidence.

It maps the doctrine repository to control objectives for authority separation, change management, risk traceability, evidence consistency, and agent adherence.

## Non-certification statement

This repository does not certify SecureTheCloud as SOC 2 compliant.

This repository does not replace an independent SOC 2 examination by a qualified auditor.

This repository provides SOC 2-aligned readiness evidence that can support a future audit, readiness review, or customer assurance process.

## Reference basis

The AICPA Trust Services Criteria are used for attestation or consulting engagements to evaluate and report on controls over the security, availability, processing integrity, confidentiality, or privacy of information and systems used to provide products or services.

SSAE No. 18 provides attestation standards context for examination engagements.

## SOC 2 alignment model

The doctrine control plane contributes to SOC 2 readiness through:

- explicit authority boundaries;
- suite and module ownership;
- canonical product packaging rules;
- forbidden-action definitions;
- change-control gates;
- machine-readable contracts;
- validation workflow;
- evidence registers;
- agent consumption requirements;
- non-certification disclaimers.

## Trust Services Criteria alignment

| Trust Services Category | Doctrine alignment |
|---|---|
| Security | Authority boundaries, forbidden actions, SENTINEL non-bypass, no unapproved runtime authority. |
| Availability | Composition rules, module ownership, suite dependencies, change traceability for control-plane continuity. |
| Processing Integrity | Machine-readable contracts, schema validation, module/authority parity checks, status taxonomy consistency. |
| Confidentiality | Explicit non-scope for secrets, credentials, live backend integration, and unauthorized evidence mutation. |
| Privacy | Privacy-sensitive claims must be governed by approved evidence sources and future privacy-specific controls. |

## Common control themes supported

| SOC 2 control theme | Doctrine evidence support |
|---|---|
| Control environment | `GOVERNANCE.md`, `doctrine.lock.md`, `AGENTS.md`, phase tracker. |
| Information and communication | Shared Markdown doctrine plus active JSON contracts. |
| Risk assessment | Authority matrix, forbidden actions, product packaging boundaries, risk intelligence suite doctrine. |
| Monitoring activities | Git history, phase evidence, validation workflow, future evidence register. |
| Control activities | PR checklist, CODEOWNERS, schema validation, phase-gated doctrine updates. |
| Logical access boundary | No default authorization authority; token/session issuance forbidden unless future doctrine approves. |
| System operations boundary | Runtime behavior remains out of scope for this doctrine repository. |
| Change management | Pull request checklist, phase tracker, changelog, doctrine lock, validation workflow. |
| Risk mitigation | SENTINEL non-bypass, unregistered-module no-authority rule, product packaging boundaries. |

## Evidence posture

The repository produces evidence of governance design and doctrine control, not evidence that production controls operated over an audit period.

Type 2 operating effectiveness evidence would require time-bound operational evidence outside this repository.

## Approved Phase 4 evidence files

- `docs/soc2/SOC2_ALIGNMENT_OVERVIEW.md`
- `docs/soc2/SOC2_CONTROL_TRACEABILITY.md`
- `docs/soc2/SOC2_EVIDENCE_REGISTER.md`
- `docs/soc2/SOC2_CHANGE_MANAGEMENT.md`

## Non-scope confirmation

Phase 4 does not add runtime adapter code, Helm templates, UI or website assets, module-specific enforcement logic, live backend integration, token issuance, runtime session creation, or production enforcement.
