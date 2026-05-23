# Suite Catalog

**Status:** Phase 1 / Portfolio Doctrine Baseline
**Doctrine Version:** 0.1.0-portfolio-baseline
**Last Updated:** 2026-05-23

## Purpose

This document defines the canonical human-readable SecureTheCloud suite catalog.

The machine-readable suite catalog will be created in Phase 3 at `contracts/portfolio/suite_catalog.json`.

## Sharing status

This Markdown suite catalog may be shared with agents after Phase 1 is complete.

The machine-readable JSON catalog should not be treated as consumable until Phase 3 creates and validates it.

## Suite status values

Suite status values are provisional until Phase 2 freezes the full status taxonomy.

Current allowed suite status values for Phase 1:

- `portfolio_baseline`
- `customer_offerable`
- `shared_fabric_dependency`
- `internal_doctrine_only`
- `future_candidate`
- `not_customer_offerable`

## Customer-offerable suites

### 1. SecureTheCloud Agent Blackbox Suite

**Status:** `customer_offerable`

**Primary role:** Agent behavior evidence, decision traceability, governed explanations, handoff context, trust intelligence summaries, and client demo/readiness packaging.

**Customer offerable:** Yes.

**Authority posture:** Evidence, explanation, readiness, and packaging. No runtime mutation or enforcement authority by default.

**Shared Trust Fabric dependencies:** suite catalog, module registry, authority matrix, evidence metadata, status taxonomy, product packaging boundaries.

### 2. SecureTheCloud Compliance Evidence Suite

**Status:** `customer_offerable`

**Primary role:** SOC 2-aligned evidence packages, audit workspace, control traceability, evidence registers, export manifests, and auditor-facing summaries.

**Customer offerable:** Yes.

**Authority posture:** Evidence recording, mapping, traceability, packaging, and presentation. No runtime enforcement authority by default.

**Shared Trust Fabric dependencies:** evidence taxonomy, SOC 2 traceability, module authority matrix, doctrine lock, status taxonomy.

### 3. SecureTheCloud Runtime Assurance Suite

**Status:** `customer_offerable`

**Primary role:** Runtime assurance doctrine, enforcement-readiness pathways, control-point routing, SENTINEL-backed decision posture, and production-boundary clarity.

**Customer offerable:** Yes.

**Authority posture:** Runtime-impacting authority only when explicitly granted by doctrine, module authority matrix, deployment phase, and SENTINEL control-point rule.

**Shared Trust Fabric dependencies:** authority matrix, SENTINEL rule, composition rules, status taxonomy, product packaging boundaries.

### 4. SecureTheCloud Risk Intelligence Suite

**Status:** `customer_offerable`

**Primary role:** Risk posture narratives, authority overlap analysis, control gap summaries, trust scoring context, and customer-safe risk intelligence.

**Customer offerable:** Yes.

**Authority posture:** Analyze, score, explain, and summarize. No runtime mutation, authorization, or enforcement authority by default.

**Shared Trust Fabric dependencies:** authority registry, status taxonomy, evidence metadata, risk/control traceability, product packaging boundaries.

## Non-suite shared substrate

### Shared Trust Fabric

**Status:** `shared_fabric_dependency`

**Customer offerable:** No, not as a standalone suite.

**Role:** Shared doctrine, registries, schemas, contracts, taxonomy, evidence metadata, and traceability substrate used by all suites.

### Doctrine Control Plane

**Status:** `internal_doctrine_only`

**Customer offerable:** No.

**Role:** This repository. It defines the portfolio doctrine and contract source of truth.

## Suite catalog freeze

The four customer-offerable suites are frozen for Phase 1.

New suites, suite renames, suite removals, or suite role changes require a doctrine update and phase evidence.
