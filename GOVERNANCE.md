# Governance

## Purpose

This repository governs SecureTheCloud portfolio doctrine, module authority, composition rules, product packaging boundaries, shared contracts, and SOC 2-aligned evidence traceability.

## Authority model

The repository is the source of truth for doctrine only. It does not implement runtime behavior.

The doctrine control plane may define:

- what suites exist
- which modules belong to which suites
- which modules are shared fabric
- which modules are internal control-plane dependencies
- which modules may observe, explain, route, package, decide, or enforce
- which actions are forbidden
- which interfaces are callable
- which status values are valid
- which product packaging combinations are allowed or forbidden

The doctrine control plane may not implement:

- runtime adapters
- admission controllers
- policy engines
- Helm charts
- UI/website assets
- provider mutations
- Kubernetes mutations
- module-specific enforcement logic

## Change management

All material changes must be traceable through Git history and phase evidence.

Material changes include:

- adding or removing a suite
- changing suite membership
- adding or removing a module
- changing authority type
- changing callable interfaces
- changing forbidden actions
- changing SENTINEL control-point doctrine
- changing Composition Layer rules
- changing product packaging boundaries
- changing status taxonomy values
- changing SOC 2 control traceability

## Review expectations

Material doctrine changes should include:

1. human-readable doctrine update
2. machine-readable contract update
3. schema update when the contract shape changes
4. phase tracker update
5. SOC 2 traceability update when applicable

## SOC 2 alignment

This repository supports SOC 2 readiness through documented control environment, authority boundaries, change management, risk traceability, and evidence registers.

It does not itself certify SOC 2 compliance.

## Doctrine freeze

A doctrine rule is considered frozen when it appears in `doctrine.lock.md` and the relevant portfolio doctrine file.

Frozen doctrine may only be changed through an explicit phase update.
