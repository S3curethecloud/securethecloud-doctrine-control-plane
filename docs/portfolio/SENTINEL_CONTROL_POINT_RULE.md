# SENTINEL Control-Point Rule

**Status:** Phase 1 / Portfolio Doctrine Baseline
**Doctrine Version:** 0.1.0-portfolio-baseline
**Last Updated:** 2026-05-23

## Purpose

This document defines SENTINEL as the canonical control point for SecureTheCloud runtime-impacting enforcement decisions.

## Canonical rule

SENTINEL is the canonical control point for runtime-impacting allow, deny, admission, policy-decision, enforcement, and production-control outcomes.

No suite, module, agent, Composition Layer package, evidence surface, explanation surface, or customer packaging surface may bypass SENTINEL when a runtime-impacting control decision is in scope.

## What counts as a control-point decision

A control-point decision includes any action that may:

- allow a runtime operation
- deny a runtime operation
- admit a workload or agent action
- block a workload or agent action
- enforce policy
- mutate provider state
- mutate Kubernetes state
- issue or validate production authorization outcomes
- change production enforcement state
- create runtime control evidence that claims enforcement occurred

## SENTINEL owns

SENTINEL owns canonical doctrine for:

- control-point decision routing
- enforcement decision authority
- non-bypass expectations
- enforcement evidence source expectations
- runtime-impacting decision boundary language
- future production control-point alignment

## SENTINEL does not automatically own

SENTINEL doctrine does not automatically grant active production enforcement.

Production enforcement requires explicit phase approval, authority matrix approval, deployment approval, and SOC 2 traceability.

## Non-bypass rule

The following are forbidden unless explicitly approved by future doctrine:

- a suite enforcing directly outside SENTINEL
- a module bypassing SENTINEL for allow/deny behavior
- a Composition Layer package silently replacing SENTINEL
- an evidence surface claiming enforcement authority
- an explanation module producing runtime control outcomes
- a customer package implying SENTINEL-backed enforcement when SENTINEL is not active
- a local agent inventing a parallel control point

## Evidence rule

Evidence may describe SENTINEL state only when the evidence source is declared and approved.

Read-only evidence may indicate readiness, posture, simulation, or doctrine status, but it must not claim live enforcement unless live enforcement is explicitly approved and recorded.

## Suite relationship

SENTINEL may be surfaced through the Runtime Assurance Suite and referenced by other suites.

SENTINEL is not owned by customer packaging language.

SENTINEL authority is governed by the doctrine control plane, the module authority matrix, and phase evidence.

## SOC 2 alignment

SENTINEL control-point doctrine supports SOC 2-aligned evidence by making enforcement authority explicit, reviewable, and non-ambiguous.

Any change to SENTINEL authority, bypass posture, evidence claims, or production enforcement status is a material doctrine change.

## Frozen baseline

The frozen SENTINEL baseline is:

1. SENTINEL is canonical for runtime-impacting control decisions.
2. SENTINEL may not be bypassed by suite packaging or Composition Layer assembly.
3. Evidence-only and explanation-only modules must not claim SENTINEL authority.
4. Live enforcement may not be claimed without explicit doctrine and phase approval.
5. Other agents must not create local substitute control-point doctrine.
