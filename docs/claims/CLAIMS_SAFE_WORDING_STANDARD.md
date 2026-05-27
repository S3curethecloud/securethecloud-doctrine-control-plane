# Claims-Safe Wording Standard

Status: Phase 9B / Implementation In Progress

## Purpose

This standard defines claims-safe wording boundaries for SecureTheCloud customer-facing, portfolio, suite, readiness, evidence, SOC 2, runtime, enforcement, Vault, SageMaker, ML, and intelligence language.

This standard is doctrine-boundary documentation only.

It does not change runtime behavior, product packaging authority, module authority, suite membership, APIs, datasets, exports, authentication, token/session behavior, credential behavior, enforcement behavior, production routing, or production enforcement.

## Required canonical phrasing rules

### Production readiness language

Allowed:

- production-ready posture
- production readiness
- customer-offerable packaging posture
- deployment readiness evidence
- documented readiness

Required boundary:

Production-ready wording must not imply production enforcement, live runtime authority, live backend activation, production operating effectiveness, authorization behavior, token issuance, session creation, or credential handling.

### SOC 2 and audit language

Allowed:

- SOC 2-aligned evidence
- SOC 2 readiness evidence
- audit-ready evidence package
- audit evidence package
- control traceability
- change management evidence

Required boundary:

Do not claim SOC 2 certification, completed independent audit, or production operating effectiveness unless supported by separate external audit evidence and explicitly authorized by doctrine.

### Suite and packaging language

Allowed:

- customer-offerable suite
- standalone module
- portfolio packaging
- commercial packaging
- buy by suite
- integrated enterprise portfolio

Required boundary:

Packaging does not create authority. Suite packaging must not imply merged module authority, runtime authority, enforcement authority, authorization authority, or production authority.

### Trust, intelligence, evidence, and readiness language

Allowed:

- evidence context
- readiness context
- explanation context
- trust intelligence
- risk intelligence
- customer-safe narrative
- audit narrative
- decision-support context

Required boundary:

Evidence does not create enforcement authority. Explanation does not create authorization authority. Intelligence outputs must remain bounded to evidence, readiness, explanation, and customer-safe context unless a future doctrine phase grants additional scope.

### Runtime, enforcement, OPA, SENTINEL, and session language

Required boundary:

Aegis informs.

RiskDNA informs.

OPA decides where policy evaluation is required.

SENTINEL remains canonical for runtime-impacting control decisions.

Runtime owns token/session side effects.

No customer-facing wording may imply OPA replacement, SENTINEL bypass, token issuance, session creation, authorization behavior, runtime enforcement, or production enforcement unless explicitly authorized by doctrine.

### Secret Vault and credential language

Required boundary:

Secret Vault adoption does not grant Vault reference resolution, secret mutation, credential authority, production secret handling, or runtime secret authority.

Any future secret handling claim requires separate doctrine authority, implementation evidence, security review, and phase approval.

### SageMaker, ML, model, and inference language

Required boundary:

SageMaker Risk Intelligence adoption does not grant SageMaker runtime execution, ML authority, model deployment, model training, runtime inference, or production risk automation.

Any future ML, model, inference, or SageMaker runtime claim requires separate doctrine authority, implementation evidence, security review, and phase approval.

## Forbidden implication patterns

Customer-facing wording must not imply:

- SOC 2 certification without external audit evidence
- production operating effectiveness without external audit evidence
- production enforcement without explicit authority
- runtime authority from evidence
- authorization authority from explanation
- module authority from suite packaging
- token/session authority from readiness labels
- Vault or secret authority from Secret Vault adoption
- SageMaker runtime or ML authority from SageMaker Risk Intelligence adoption
- OPA replacement
- SENTINEL bypass

## Current Phase 9B conclusion

Claims-safe wording must qualify readiness, packaging, SOC 2, audit, evidence, intelligence, Vault, SageMaker, ML, runtime, and enforcement language with explicit doctrine boundaries.

This standard is the baseline for future customer-facing claims review.
