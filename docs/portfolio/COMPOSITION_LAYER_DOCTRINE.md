# Composition Layer Doctrine

**Status:** Phase 1 / Portfolio Doctrine Baseline
**Doctrine Version:** 0.1.0-portfolio-baseline
**Last Updated:** 2026-05-23

## Purpose

The Composition Layer defines how SecureTheCloud modules, suites, evidence surfaces, control points, and customer packages may be assembled without merging authority or bypassing doctrine.

## Canonical rule

Composition is packaging and orchestration. Composition is not authority creation.

A composed product surface may expose modules together, but it must not grant any module authority beyond the module authority matrix.

## Composition Layer may do

The Composition Layer may:

- assemble customer-facing packages from approved suites
- present Shared Trust Fabric metadata through approved suite surfaces
- route read-only evidence views
- combine evidence summaries from approved sources
- reference module registry entries
- reference suite catalog entries
- reference authority matrix entries
- present customer-safe summaries
- prepare product packaging views

## Composition Layer must not do

The Composition Layer must not:

- create runtime authority
- issue tokens
- grant authorization
- bypass SENTINEL
- perform provider mutation
- perform Kubernetes mutation
- execute OPA, Sentinel, or admission decisions directly unless explicitly assigned that authority
- convert evidence modules into enforcement modules
- convert explanation modules into authorization modules
- merge customer suite roles into a single undefined authority surface
- invent status values outside the status taxonomy
- invent suite membership outside the suite catalog
- invent module authority outside the authority matrix

## Authority preservation rule

When modules are composed, each module keeps its original authority type, callable interfaces, forbidden actions, status, and suite/fabric membership.

Composition never upgrades authority.

Composition never erases forbidden actions.

Composition never changes SENTINEL control-point doctrine.

## Product packaging rule

A product package may include multiple suites only if each suite remains separately identifiable.

The package must identify:

- included suites
- included modules
- Shared Trust Fabric dependencies
- authority-bearing modules
- evidence-only modules
- explanation-only modules
- runtime-impacting modules
- forbidden actions
- SENTINEL dependency status

## Suite boundary rule

Suite boundaries are packaging boundaries, not implicit authority boundaries.

Authority boundaries are defined by the module authority matrix and SENTINEL control-point doctrine.

## Shared fabric rule

Shared Trust Fabric components may support multiple suites but must not be duplicated or forked by a suite.

If a composition needs a new shared concept, the Shared Trust Fabric doctrine must be updated first.

## SENTINEL rule

Any composition that includes runtime enforcement, admission control, policy decisioning, deny/allow behavior, or production control-point behavior must preserve SENTINEL as the canonical control point.

No Composition Layer package may bypass, replace, or silently emulate SENTINEL.

## SOC 2 alignment

The Composition Layer supports SOC 2 alignment by preserving separation of duties, change traceability, and explicit control ownership.

Composition changes that alter customer-visible authority, evidence scope, or enforcement posture must update SOC 2 traceability once Phase 4 documents exist.

## Frozen baseline

The Composition Layer baseline is frozen as:

1. composition may package and present;
2. composition may not create authority;
3. composition may not bypass SENTINEL;
4. composition must preserve module-level authority and forbidden actions;
5. composition must reference shared contracts rather than invent local doctrine.

## Phase 7 Aegis Runtime / RiskDNA composition rule

Composition may reference Aegis Runtime and RiskDNA as planning-ready logical boundaries.

Composition must not convert Aegis Runtime or RiskDNA into independent packages, Helm toggles, production routing units, or enforcement modules until future doctrine and implementation evidence proves clean deploy boundaries.

Composition must preserve Runtime ownership of token/session side effects, OPA policy decision authority, and SENTINEL non-bypass.
