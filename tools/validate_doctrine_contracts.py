#!/usr/bin/env python3
"""Validate SecureTheCloud doctrine control-plane contracts.

This script is repository governance tooling only. It does not implement runtime
adapter behavior, enforcement logic, Helm behavior, UI assets, or production
control behavior.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "schemas/portfolio/module_registry.schema.json",
    "schemas/portfolio/suite_catalog.schema.json",
    "schemas/portfolio/authority_matrix.schema.json",
    "contracts/portfolio/module_registry.json",
    "contracts/portfolio/suite_catalog.json",
    "contracts/portfolio/authority_matrix.json",
    "contracts/portfolio/composition_rules.json",
    "contracts/portfolio/status_taxonomy.json",
]

CUSTOMER_SUITES = {
    "agent_blackbox",
    "compliance_evidence",
    "runtime_assurance",
    "risk_intelligence",
}

FORBIDDEN_RUNTIME_AUTHORITY = {
    "issuing_tokens",
    "granting_authorization",
    "creating_runtime_sessions",
    "mutating_provider_resources",
    "mutating_kubernetes_resources",
    "executing_helm_deployments",
    "exposing_live_backend_apis",
    "performing_production_traffic_cutover",
    "enforcing_runtime_allow_deny_decisions",
    "bypassing_sentinel",
}


def load_json(path: str) -> object:
    full_path = ROOT / path
    if not full_path.exists():
        raise AssertionError(f"Missing required file: {path}")
    with full_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def assert_required_files() -> None:
    for path in REQUIRED_FILES:
        load_json(path)


def assert_suite_catalog() -> None:
    catalog = load_json("contracts/portfolio/suite_catalog.json")
    suites = catalog["suites"]
    suite_ids = {suite["suite_id"] for suite in suites}
    if suite_ids != CUSTOMER_SUITES:
        raise AssertionError(f"Unexpected customer suite IDs: {sorted(suite_ids)}")
    if not all(suite["customer_offerable"] for suite in suites):
        raise AssertionError("All baseline suites must be customer_offerable=true")
    substrates = {item["substrate_id"]: item for item in catalog["non_suite_substrates"]}
    if substrates["shared_trust_fabric"]["customer_offerable"]:
        raise AssertionError("Shared Trust Fabric must not be a customer-offerable suite")


def assert_module_and_authority_consistency() -> None:
    registry = load_json("contracts/portfolio/module_registry.json")
    authority = load_json("contracts/portfolio/authority_matrix.json")
    module_ids = {module["module_id"] for module in registry["modules"]}
    authority_ids = {row["module_id"] for row in authority["authority_rows"]}
    if module_ids != authority_ids:
        missing_from_authority = sorted(module_ids - authority_ids)
        missing_from_registry = sorted(authority_ids - module_ids)
        raise AssertionError(
            "Module/authority mismatch: "
            f"missing_from_authority={missing_from_authority}, "
            f"missing_from_registry={missing_from_registry}"
        )
    if len(module_ids) != len(registry["modules"]):
        raise AssertionError("Duplicate module IDs detected in module registry")
    if len(authority_ids) != len(authority["authority_rows"]):
        raise AssertionError("Duplicate module IDs detected in authority matrix")

    forbidden = set(authority["universal_forbidden_actions"])
    missing_forbidden = sorted(FORBIDDEN_RUNTIME_AUTHORITY - forbidden)
    if missing_forbidden:
        raise AssertionError(f"Missing universal forbidden runtime actions: {missing_forbidden}")

    runtime_rows = [row["module_id"] for row in authority["authority_rows"] if row["runtime_authority"]]
    if runtime_rows:
        raise AssertionError(f"Phase 3 baseline must not grant runtime authority: {runtime_rows}")


def assert_status_taxonomy() -> None:
    taxonomy = load_json("contracts/portfolio/status_taxonomy.json")
    required_authority_values = {
        "doctrine_only",
        "shared_contract",
        "composition_only",
        "evidence_read_only",
        "evidence_packaging",
        "explanation_read_only",
        "risk_scoring_read_only",
        "control_point_canonical",
        "runtime_enforcement_blocked",
    }
    present = set(taxonomy["authority_status"])
    missing = sorted(required_authority_values - present)
    if missing:
        raise AssertionError(f"Missing authority status values: {missing}")


def assert_composition_rules() -> None:
    composition = load_json("contracts/portfolio/composition_rules.json")
    if not composition["sentinel_non_bypass"]:
        raise AssertionError("Composition rules must preserve SENTINEL non-bypass")
    forbidden = set(composition["forbidden_actions"])
    for action in ["create_runtime_authority", "issue_tokens", "grant_authorization", "bypass_sentinel"]:
        if action not in forbidden:
            raise AssertionError(f"Composition rule missing forbidden action: {action}")


def main() -> int:
    assert_required_files()
    assert_suite_catalog()
    assert_module_and_authority_consistency()
    assert_status_taxonomy()
    assert_composition_rules()
    print("Doctrine contract validation passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - CI failure path
        print(f"Doctrine contract validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
