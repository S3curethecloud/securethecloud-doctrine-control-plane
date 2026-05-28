# Phase 9E Downstream Claims Risk Classification / Target Selection

Status: Phase 9E / Target Selection In Progress

Purpose: Classify downstream claim-surface risk from the Phase 9D inventory and select the first downstream repository for a later claims-safe wording review.

## Source evidence

- docs/claims/evidence/PHASE_9D_DOWNSTREAM_CUSTOMER_FACING_CLAIMS_SURFACE_INVENTORY.md

## Risk model

The Phase 9E score is a target-selection heuristic, not a runtime authority decision.

Weighted risk formula:

- production readiness claims x 2
- runtime and enforcement authority claims x 4
- SOC 2 and audit claims x 3
- product portfolio and suite packaging claims x 1
- trust intelligence, evidence, and readiness claims x 1
- Vault, secret, SageMaker, ML, and model authority claims x 4

High-impact claims are runtime/enforcement, SOC 2/audit, and Vault/secret/SageMaker/ML/model authority claims.

## Repository risk ranking

| Rank | Repository | Branch | HEAD | Total matches | High-impact matches | Weighted risk |
| --- | --- | --- | --- | ---: | ---: | ---: |
| 1 | securethecloud-kubernetes-sentinel | phase-0-admission-review-contract | 3054784 | 34213 | 5310 | 51366 |
| 2 | securethecloud-agent-blackbox | main | 2b35365 | 21296 | 5410 | 38025 |
| 3 | securethecloud-agent-sovereignty-zones | main | 21d3485 | 18907 | 5245 | 34420 |
| 4 | securethecloud-agent-risk-exchange | main | 95fb78c | 11614 | 6189 | 29742 |
| 5 | securethecloud-secret-vault | main | 73d54c9 | 2944 | 2301 | 9690 |
| 6 | stc-intelligence-core | evidence/intelligence-core-phase8i-doctrine-adoption-release-baseline | 55f5d61 | 1504 | 400 | 2685 |
| 7 | securethecloud-sagemaker-risk-intelligence | main | 4e43a83 | 892 | 434 | 2122 |
| 8 | securethecloud-safp | main | 64738e6 | 868 | 137 | 1277 |
| 9 | aegis-riskdna-runtime/ztr-runtime | unknown | unknown | 0 | 0 | 0 |

## Category breakdown

### securethecloud-kubernetes-sentinel

- Branch: phase-0-admission-review-contract
- HEAD: 3054784
- Production readiness claims: 1970
- Runtime and enforcement authority claims: 145
- SOC 2 and audit claims: 747
- Product portfolio and suite packaging claims: 11922
- Trust intelligence, evidence, and readiness claims: 15011
- Vault, secret, SageMaker, ML, and model authority claims: 4418
- Total matches: 34213
- High-impact matches: 5310
- Weighted risk: 51366

### securethecloud-agent-blackbox

- Branch: main
- HEAD: 2b35365
- Production readiness claims: 1416
- Runtime and enforcement authority claims: 1202
- SOC 2 and audit claims: 917
- Product portfolio and suite packaging claims: 6613
- Trust intelligence, evidence, and readiness claims: 7857
- Vault, secret, SageMaker, ML, and model authority claims: 3291
- Total matches: 21296
- High-impact matches: 5410
- Weighted risk: 38025

### securethecloud-agent-sovereignty-zones

- Branch: main
- HEAD: 21d3485
- Production readiness claims: 235
- Runtime and enforcement authority claims: 1961
- SOC 2 and audit claims: 457
- Product portfolio and suite packaging claims: 2913
- Trust intelligence, evidence, and readiness claims: 10514
- Vault, secret, SageMaker, ML, and model authority claims: 2827
- Total matches: 18907
- High-impact matches: 5245
- Weighted risk: 34420

### securethecloud-agent-risk-exchange

- Branch: main
- HEAD: 95fb78c
- Production readiness claims: 167
- Runtime and enforcement authority claims: 134
- SOC 2 and audit claims: 606
- Product portfolio and suite packaging claims: 1706
- Trust intelligence, evidence, and readiness claims: 3552
- Vault, secret, SageMaker, ML, and model authority claims: 5449
- Total matches: 11614
- High-impact matches: 6189
- Weighted risk: 29742

### securethecloud-secret-vault

- Branch: main
- HEAD: 73d54c9
- Production readiness claims: 25
- Runtime and enforcement authority claims: 89
- SOC 2 and audit claims: 182
- Product portfolio and suite packaging claims: 373
- Trust intelligence, evidence, and readiness claims: 245
- Vault, secret, SageMaker, ML, and model authority claims: 2030
- Total matches: 2944
- High-impact matches: 2301
- Weighted risk: 9690

### stc-intelligence-core

- Branch: evidence/intelligence-core-phase8i-doctrine-adoption-release-baseline
- HEAD: 55f5d61
- Production readiness claims: 17
- Runtime and enforcement authority claims: 84
- SOC 2 and audit claims: 36
- Product portfolio and suite packaging claims: 96
- Trust intelligence, evidence, and readiness claims: 991
- Vault, secret, SageMaker, ML, and model authority claims: 280
- Total matches: 1504
- High-impact matches: 400
- Weighted risk: 2685

### securethecloud-sagemaker-risk-intelligence

- Branch: main
- HEAD: 4e43a83
- Production readiness claims: 16
- Runtime and enforcement authority claims: 73
- SOC 2 and audit claims: 88
- Product portfolio and suite packaging claims: 171
- Trust intelligence, evidence, and readiness claims: 271
- Vault, secret, SageMaker, ML, and model authority claims: 273
- Total matches: 892
- High-impact matches: 434
- Weighted risk: 2122

### securethecloud-safp

- Branch: main
- HEAD: 64738e6
- Production readiness claims: 7
- Runtime and enforcement authority claims: 26
- SOC 2 and audit claims: 9
- Product portfolio and suite packaging claims: 216
- Trust intelligence, evidence, and readiness claims: 508
- Vault, secret, SageMaker, ML, and model authority claims: 102
- Total matches: 868
- High-impact matches: 137
- Weighted risk: 1277

### aegis-riskdna-runtime/ztr-runtime

- Branch: unknown
- HEAD: unknown
- Production readiness claims: 0
- Runtime and enforcement authority claims: 0
- SOC 2 and audit claims: 0
- Product portfolio and suite packaging claims: 0
- Trust intelligence, evidence, and readiness claims: 0
- Vault, secret, SageMaker, ML, and model authority claims: 0
- Total matches: 0
- High-impact matches: 0
- Weighted risk: 0

## Selected first downstream target

Selected repository: securethecloud-kubernetes-sentinel

Selected branch observed: phase-0-admission-review-contract

Selected HEAD observed: 3054784

Selection basis:

- Total matches: 34213
- High-impact matches: 5310
- Weighted risk: 51366

Decision:

The selected repository should be reviewed first in a later downstream-specific claims-safe wording phase.

## Explicit non-scope

Phase 9E does not change downstream repositories.

Phase 9E does not patch customer-facing wording.

Phase 9E does not grant runtime authority, enforcement authority, token/session authority, Vault authority, SageMaker runtime authority, ML authority, production authority, SOC 2 certification, or production operating effectiveness.

## Recommended next phase

Phase 9F - First Downstream Claims-Safe Wording Planning Gate

The next phase should plan a downstream-specific review for the selected first target before any patch is applied.
