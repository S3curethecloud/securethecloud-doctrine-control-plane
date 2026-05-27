# SOC 2 Change Management

**Status:** Phase 4 / SOC 2 Alignment Evidence
**Doctrine Version:** 0.4.0-soc2-alignment-baseline
**Last Updated:** 2026-05-23

## Purpose

This document defines the SOC 2-aligned change-management posture for the SecureTheCloud Doctrine Control Plane.

It applies to doctrine, schemas, machine-readable contracts, authority boundaries, product packaging boundaries, agent instructions, validation tooling, and SOC 2 evidence files.

## Non-certification statement

This document supports SOC 2 readiness. It is not a SOC 2 audit report, certification, or assertion of operating effectiveness.

## Change-management objectives

The doctrine control plane uses change management to ensure:

- portfolio doctrine remains deliberate and traceable;
- suite definitions are not changed silently;
- module authority is not expanded without review;
- forbidden actions are not removed without review;
- SENTINEL control-point doctrine is not bypassed;
- product packaging does not merge roles or misstate authority;
- machine-readable contracts remain consistent with Markdown doctrine;
- downstream agents can detect canonical doctrine changes.

## Change classes

| Change class | Examples | Required evidence |
|---|---|---|
| Administrative | README wording, formatting, typo fixes | Git history, changelog if material |
| Doctrine baseline | Suite, authority, composition, SENTINEL, packaging updates | Phase tracker, doctrine lock, relevant Markdown docs |
| Contract change | JSON contract or schema changes | Schema/contract update, validation pass, phase evidence |
| Authority change | Module authority, callable interface, forbidden action, suite membership | Doctrine lock, matrix update, contract update, SOC 2 traceability update |
| SOC 2 evidence change | Traceability, evidence register, readiness mapping | SOC 2 evidence register update and phase evidence |
| Runtime-scope request | Any request to add runtime behavior or enforcement logic | Must be rejected or moved to a separately approved runtime repository and phase |

## Required change artifacts

Material changes should update all applicable files:

- `doctrine.lock.md`
- `docs/phases/PHASE_TRACKER.md`
- relevant `docs/portfolio/*` doctrine files
- relevant `contracts/portfolio/*.json` files
- relevant `schemas/portfolio/*.schema.json` files
- `docs/soc2/SOC2_CONTROL_TRACEABILITY.md`
- `docs/soc2/SOC2_EVIDENCE_REGISTER.md`
- `CHANGELOG.md` when the change is externally meaningful

## Pull request requirements

Pull requests that modify doctrine or contracts should answer the checklist in `.github/pull_request_template.md`.

A pull request must identify whether it changes:

- suite membership;
- module authority;
- callable interfaces;
- forbidden actions;
- Composition Layer rules;
- SENTINEL control-point doctrine;
- product packaging boundaries;
- status taxonomy values;
- SOC 2 traceability;
- machine-readable contracts.

## Review requirements

Material doctrine changes should be reviewed by a repository owner or designated doctrine owner.

The `CODEOWNERS` file establishes repository-owner review expectations.

## Validation requirements

Changes to contracts, schemas, the validator, or the workflow must pass doctrine validation.

The validation workflow checks:

- required contract and schema files exist;
- JSON schema validation for active schema-backed contracts;
- suite catalog baseline consistency;
- module registry and authority matrix parity;
- duplicate module ID prevention;
- baseline runtime authority remains ungranted;
- universal forbidden actions remain present;
- SENTINEL non-bypass remains preserved;
- required authority status values remain present.

## Emergency change rule

If an urgent correction is required, it may be committed only if:

1. the correction preserves repository non-scope;
2. the phase tracker is updated after the correction;
3. doctrine lock is updated if frozen doctrine changed;
4. SOC 2 evidence register is updated if evidence posture changed;
5. a follow-up review is recorded.

## Prohibited change pattern

The following changes are prohibited in this repository:

- runtime adapter implementation;
- Helm chart or deployment template implementation;
- customer-facing product frontend source;
- module-specific enforcement implementation;
- live backend integration;
- credential or secret material;
- production deployment script;
- unapproved authorization or session behavior;
- unapproved runtime enforcement behavior.

## Evidence retention posture

Git history, phase documents, doctrine lock updates, changelog entries, validation workflow runs, and PR review records are the expected evidence trail.

This repository does not define organization-wide evidence retention periods. Retention policy should be set by the broader SecureTheCloud governance program.

## Current readiness conclusion

The Doctrine Control Plane has SOC 2-aligned change-management design evidence for doctrine governance.

It does not yet demonstrate time-bound operating effectiveness for a SOC 2 Type 2 report.

## Phase 7 change-management record

Phase 7 is a doctrine baseline and contract change.

It updates human-readable doctrine, machine-readable contracts, SOC 2 traceability, and phase evidence while preserving repository non-scope.

No runtime adapter code, Helm templates, UI assets, live backend integrations, token issuance, runtime session creation, authorization behavior, or production enforcement are added.

## Phase 8 downstream adoption change-management record

Phase 8 records downstream adoption evidence and pending adoption backlog for canonical Phase 7 doctrine.

This is an evidence/register update only.

It does not modify runtime behavior, Helm templates, deployment routing, token/session authority, authorization behavior, Vault reference authority, SageMaker runtime authority, provider mutation, Kubernetes mutation, or production enforcement.

## Phase 8I backlog correction record

Phase 8I records `S3curethecloud/stc-intelligence-core` as a pending downstream adoption target.

This correction is evidence/backlog-only. It does not grant Aegis/RiskDNA awareness, intelligence authority, runtime authority, Helm packaging, deployment routing, production enforcement, or SOC 2 certification claims.
