# Read-Only Doctrine Portal Evaluation

**Status:** Evaluated / Optional Future Candidate
**Doctrine Version:** 0.6.0-read-only-portal-evaluation
**Last Updated:** 2026-05-23

## Purpose

This document records the doctrine position on whether SecureTheCloud needs a frontend portal for the Doctrine Control Plane.

## Decision

A frontend portal is not required for the doctrine baseline.

The current doctrine baseline is complete as a Git-governed repository containing:

- Markdown doctrine;
- machine-readable JSON contracts;
- JSON schemas;
- validation workflow;
- SOC 2-aligned readiness evidence;
- agent adoption instructions;
- phase tracker evidence.

## Optional future portal

A future portal may be considered as a read-only generated documentation surface.

It may help humans browse:

- suite catalog;
- module authority matrix;
- status taxonomy;
- SENTINEL control-point doctrine;
- Composition Layer doctrine;
- SOC 2 readiness evidence;
- machine-readable contract summaries;
- phase status.

## Hard boundary

A portal must never become the source of truth.

The source of truth remains this Git repository.

## Allowed future portal behavior

A future portal may:

- render Markdown doctrine;
- render JSON contract summaries;
- render schema summaries;
- show phase status;
- link to canonical Git files;
- provide read-only search;
- provide read-only navigation;
- expose customer-safe doctrine summaries when approved.

## Forbidden future portal behavior

A future portal must not:

- edit doctrine;
- write contracts;
- alter schemas;
- change phase status;
- create modules;
- create suite membership;
- grant authority;
- modify forbidden actions;
- bypass SENTINEL;
- issue tokens;
- grant authorization;
- create runtime sessions;
- connect to production backends;
- mutate provider or Kubernetes resources;
- enforce runtime decisions;
- claim SOC 2 certification.

## Adoption rule

Agents should not wait for a portal.

Agents must consume the doctrine repository directly.

## Conclusion

The doctrine-control-plane role does not need a frontend platform at this time.

A future read-only portal is permitted only as a visualization layer generated from canonical repository artifacts.
