## 2026-05-26 — Phase 7 Aegis Runtime / RiskDNA Doctrine Delta

Added canonical doctrine delta for Aegis Runtime signal context and RiskDNA runtime risk context.
Added module registry and authority matrix records with no runtime authority.
Preserved SENTINEL non-bypass, packaging non-authority, runtime non-scope, and SOC 2 non-certification boundaries.

# Changelog

All notable doctrine control-plane changes will be recorded here.

This project follows a phase-gated change model. Material changes to suite membership, authority, composition rules, product packaging, or SOC 2 traceability must reference the relevant phase evidence.

## 0.0.1-baseline — 2026-05-23

### Added

- Repository baseline initialized.
- Root README added.
- Agent operating instructions added.
- Governance rules added.
- Initial doctrine lock added.
- Phase tracker added.

### Scope confirmation

- Documentation, schemas, contracts, and evidence traceability are in scope.
- Runtime adapter code is out of scope.
- Helm templates are out of scope.
- UI/website assets are out of scope.
- Module-specific enforcement logic is out of scope.
