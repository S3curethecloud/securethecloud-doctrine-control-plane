# SecureTheCloud Enterprise Product Portfolio

**Status:** Phase 1 / Portfolio Doctrine Baseline
**Doctrine Version:** 0.1.0-portfolio-baseline
**Last Updated:** 2026-05-23

## Purpose

This document defines the customer-offerable SecureTheCloud enterprise portfolio baseline.

It establishes the four suites that may be packaged for customers while preserving authority separation, Shared Trust Fabric boundaries, Composition Layer rules, and SENTINEL control-point doctrine.

## Portfolio doctrine

SecureTheCloud is a modular trust, evidence, governance, and runtime assurance platform.

The portfolio is organized into four customer-offerable suites supported by one Shared Trust Fabric and governed by one doctrine control plane.

The suites are product packaging boundaries. They are not permission boundaries by themselves. Authority is granted only by the module authority matrix and doctrine contracts.

## Four customer-offerable suites

### 1. SecureTheCloud Agent Blackbox Suite

**Customer purpose:** Explain, audit, and package evidence for AI agent behavior, decisions, handoffs, and governed readiness.

**Primary customer value:** Agent evidence visibility, trust intelligence summaries, decision traceability, demo/readiness packaging, and auditor-consumable agent context.

**Allowed authority posture:** Observe, explain, summarize, package, and present evidence. It must not grant authorization, issue tokens, mutate runtime systems, or enforce production controls unless a separate enforcement module grants that authority through doctrine.

### 2. SecureTheCloud Compliance Evidence Suite

**Customer purpose:** Produce governance, audit, SOC 2-aligned, and enterprise evidence packages from canonical doctrine and approved evidence sources.

**Primary customer value:** Audit workspace, evidence registers, control traceability, SOC 2 alignment, export manifests, auditor packages, and customer-safe compliance summaries.

**Allowed authority posture:** Record, map, summarize, package, and present evidence. It must not become the system of runtime enforcement, identity authorization, or policy execution.

### 3. SecureTheCloud Runtime Assurance Suite

**Customer purpose:** Govern runtime assurance pathways, control points, admission/evaluation context, and runtime safety boundaries.

**Primary customer value:** Runtime boundary clarity, control-point routing, enforcement-readiness doctrine, non-bypass rules, and future production assurance integration.

**Allowed authority posture:** Runtime-impacting authority is allowed only when explicitly granted by the authority matrix, deployment phase, and control-point doctrine. SENTINEL is the canonical control point for enforcement decisions and may not be bypassed by suite packaging or Composition Layer wiring.

### 4. SecureTheCloud Risk Intelligence Suite

**Customer purpose:** Translate technical evidence, risk signals, authority boundaries, and module state into governed risk intelligence.

**Primary customer value:** Risk posture narratives, trust scoring context, control gaps, authority-overlap warnings, readiness summaries, and board/customer-facing risk explanations.

**Allowed authority posture:** Analyze, score, explain, and summarize risk. It must not invent runtime truth, mutate systems, override SENTINEL, or create enforcement outcomes without explicit authority.

## Shared Trust Fabric

The Shared Trust Fabric supports all suites. It is not a fifth customer-offerable suite.

It contains shared doctrine, registry, identity assumptions, evidence metadata, authority taxonomy, composition contracts, status taxonomy, schema definitions, and cross-suite traceability.

Shared fabric components may be visible to customers through a suite, but they must not be packaged as standalone authority unless doctrine explicitly grants that packaging.

## Doctrine control plane

The doctrine control plane is this repository.

It defines:

- suite catalog
- module registry requirements
- authority registry requirements
- composition rules
- status taxonomy
- product packaging boundaries
- SOC 2-aligned traceability expectations
- agent consumption rules

The doctrine control plane does not implement runtime behavior.

## Authority separation baseline

No suite may absorb the authority of another suite through packaging language.

No module may gain additional authority because it appears in a customer package.

No evidence module may become an enforcement module without explicit authority matrix approval.

No explanation module may become an authorization module.

No Composition Layer artifact may bypass SENTINEL when runtime enforcement or control-point decisions are in scope.

## Customer packaging rule

Customer packaging may combine suite visibility, but it may not merge suite roles.

A customer package may include multiple suites only if:

1. each suite remains separately described;
2. shared modules are identified as Shared Trust Fabric dependencies;
3. module authority remains unchanged;
4. forbidden actions remain explicit;
5. SENTINEL control-point doctrine remains authoritative;
6. SOC 2 traceability is updated when authority or evidence scope changes.

## Baseline freeze

The four customer-offerable suites frozen by this phase are:

1. SecureTheCloud Agent Blackbox Suite
2. SecureTheCloud Compliance Evidence Suite
3. SecureTheCloud Runtime Assurance Suite
4. SecureTheCloud Risk Intelligence Suite

Any addition, removal, rename, or role change requires a doctrine update.

## Phase 7 Aegis Runtime / RiskDNA doctrine delta

Aegis Runtime is recognized as a bounded runtime signal, evidence, and rendering participant.

RiskDNA is recognized as a logical runtime risk-context and scoring participant.

These records support Runtime Assurance, Risk Intelligence, Compliance Evidence, and Agent Blackbox evidence views only within their approved authority boundaries.

They do not create a fifth customer-offerable suite.

They do not grant token issuance, authorization, session lifecycle, runtime mutation, OPA replacement, SENTINEL bypass, Helm packaging, production routing, or production enforcement authority.
