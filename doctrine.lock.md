# Doctrine Lock

**Status:** Phase 0 / Repository Baseline
**Doctrine Version:** 0.0.1-baseline
**Last Updated:** 2026-05-23

## Canonical statement

This repository is the SecureTheCloud doctrine control plane.

It is the source of truth for portfolio-level authority, suite composition, module boundaries, status taxonomy, product packaging, and SOC 2-aligned doctrine evidence.

## Current frozen rules

### Repository scope

- This repository owns doctrine, schemas, contracts, and evidence traceability.
- This repository does not own runtime adapter code.
- This repository does not own Helm templates.
- This repository does not own UI or website assets.
- This repository does not own module-specific enforcement logic.

### Agent rule

Other agents must not invent suite membership, module authority, callable interfaces, enforcement ownership, forbidden actions, or product packaging rules outside this doctrine.

### Frontend rule

A frontend is not required for the initial doctrine control-plane role.

If a frontend is ever added, it must be read-only documentation visualization generated from canonical Markdown and JSON contracts. It must not become the source of truth and must not implement runtime enforcement.

### SOC 2 rule

This repository may provide SOC 2-aligned evidence and traceability, but it does not claim SOC 2 certification.

## Unfrozen pending doctrine

The following areas are not yet frozen and must be completed in later phases:

- four customer-offerable suites
- Shared Trust Fabric doctrine
- Composition Layer rules
- SENTINEL control-point doctrine
- module authority matrix
- status taxonomy
- product packaging boundaries
- schema definitions
- machine-readable portfolio contracts
- SOC 2 traceability documents
