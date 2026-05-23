# Shared Trust Fabric

**Status:** Phase 1 / Portfolio Doctrine Baseline
**Doctrine Version:** 0.1.0-portfolio-baseline
**Last Updated:** 2026-05-23

## Purpose

The Shared Trust Fabric is the common doctrine, contract, metadata, and evidence substrate used by all SecureTheCloud suites.

It prevents every suite and agent from creating its own local definitions for trust, authority, status, evidence, composition, and packaging.

## Canonical rule

The Shared Trust Fabric is not a fifth customer-offerable suite.

It is a shared substrate that may be consumed by customer-offerable suites, internal agents, evidence surfaces, and future read-only documentation views.

## Shared Trust Fabric owns

The Shared Trust Fabric owns shared definitions for:

- suite catalog
- module registry
- authority registry
- status taxonomy
- composition rules
- evidence metadata rules
- SOC 2-aligned traceability mapping
- product packaging boundaries
- agent consumption expectations
- canonical forbidden-action language

## Shared Trust Fabric does not own

The Shared Trust Fabric does not own:

- product-specific customer promises
- runtime adapter code
- Helm templates
- UI or website assets
- production deployment scripts
- module-specific enforcement logic
- customer-specific secrets
- live backend integrations
- direct production mutation authority

## Fabric participation rule

A module may depend on Shared Trust Fabric definitions without becoming part of the fabric.

A module belongs to the fabric only if its primary purpose is to provide shared doctrine, registry, taxonomy, metadata, contract, or traceability used across suites.

## Authority rule

Shared Trust Fabric participation does not grant runtime authority.

Fabric modules may define authority boundaries, but they do not automatically possess the runtime authority they describe.

Authority must be granted through the module authority matrix and frozen doctrine contracts.

## Suite relationship

Each customer-offerable suite may consume Shared Trust Fabric definitions.

Suites must not fork fabric definitions.

If a suite needs a new status value, authority type, composition rule, or packaging boundary, the Shared Trust Fabric doctrine must be updated first.

## SOC 2 alignment

The Shared Trust Fabric supports SOC 2 alignment by making governance, authority, risk, and evidence definitions consistent across the portfolio.

It supports control objectives related to:

- control environment
- risk assessment
- information and communication
- change management
- logical authority separation
- system operation boundaries
- control evidence consistency

## Agent rule

Agents must import or reference Shared Trust Fabric definitions from this repository.

Agents must not create local substitutes for suite catalogs, module registries, authority matrices, composition rules, or status taxonomies.

## Customer visibility rule

Shared Trust Fabric content may be exposed to customers only through approved suite surfaces or auditor-facing evidence surfaces.

Customer visibility does not convert Shared Trust Fabric into a standalone product suite.
