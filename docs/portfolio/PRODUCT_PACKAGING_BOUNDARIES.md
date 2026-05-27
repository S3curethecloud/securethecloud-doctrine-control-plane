# Product Packaging Boundaries

**Status:** Phase 1 / Portfolio Doctrine Baseline
**Doctrine Version:** 0.1.0-portfolio-baseline
**Last Updated:** 2026-05-23

## Purpose

This document defines how SecureTheCloud products, suites, shared fabric dependencies, and customer packages may be presented without merging roles or authority.

## Canonical rule

Packaging is not authority.

A customer package may combine suite visibility, but it must not merge suite roles, expand module authority, hide forbidden actions, or bypass SENTINEL control-point doctrine.

## Customer-offerable packaging units

Only the following suites are customer-offerable baseline packaging units:

1. SecureTheCloud Agent Blackbox Suite
2. SecureTheCloud Compliance Evidence Suite
3. SecureTheCloud Runtime Assurance Suite
4. SecureTheCloud Risk Intelligence Suite

## Not standalone customer-offerable by default

The following are not standalone customer-offerable suites by default:

- Shared Trust Fabric
- Doctrine Control Plane
- SENTINEL control-point doctrine
- module authority matrix
- status taxonomy
- schema registry
- internal phase tracker
- local agent instructions

These may support customer-facing packages, but they must not be sold or described as standalone authority-bearing suites unless doctrine is updated.

## Allowed packaging behavior

A package may:

- include one or more customer-offerable suites
- expose read-only evidence surfaces
- expose customer-safe summaries
- reference Shared Trust Fabric dependencies
- state SENTINEL readiness or dependency status when accurate
- include SOC 2-aligned evidence documents when approved
- identify included modules and authority posture

## Forbidden packaging behavior

A package must not:

- imply live enforcement when enforcement is not approved
- imply authorization when authorization is not approved
- imply runtime mutation authority from evidence-only modules
- merge Agent Blackbox evidence authority with Runtime Assurance enforcement authority
- merge Compliance Evidence packaging with control-point execution
- turn Risk Intelligence summaries into policy decisions
- present Shared Trust Fabric as a standalone customer suite
- hide forbidden actions
- bypass SENTINEL
- invent suite names or module authority
- claim SOC 2 certification from SOC 2-aligned documentation alone

## Multi-suite packaging rule

A multi-suite package must include:

- included suite list
- included module list when module-level claims are made
- Shared Trust Fabric dependencies
- explicit authority posture
- forbidden actions
- control-point dependency statement
- SOC 2 evidence impact statement when applicable

## Naming rule

Customer package names may be market-facing, but they must map back to the canonical suite catalog.

A marketing name does not create a new suite.

## SOC 2 alignment

Packaging boundaries support SOC 2 readiness by preventing inaccurate claims about control ownership, enforcement state, evidence lineage, and separation of duties.

Any packaging change that changes authority claims, evidence claims, or enforcement claims must update SOC 2 traceability after Phase 4 exists.

## Frozen baseline

The frozen packaging baseline is:

1. four customer-offerable suites only;
2. Shared Trust Fabric is a dependency, not a fifth suite;
3. doctrine control plane is internal, not customer packaging;
4. SENTINEL doctrine is canonical, not optional marketing language;
5. packaging must not expand authority;
6. SOC 2-aligned documentation must not be represented as certification.

## Phase 7 Aegis Runtime / RiskDNA packaging reality

Aegis Runtime and RiskDNA have documented logical boundaries and planning-ready contracts.

They are not proven independent deployment units.

No Helm toggle, suite module, package decomposition, disable/enable behavior, or production routing claim is authorized by Phase 7.

Customer-facing packaging may reference Aegis Runtime and RiskDNA only as bounded readiness, evidence, risk, signal, or explanation context within approved suite boundaries.
