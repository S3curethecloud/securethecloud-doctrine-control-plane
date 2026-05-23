# Doctrine Change Checklist

## Summary

Describe the doctrine, schema, contract, or evidence change.

## Scope confirmation

- [ ] This change does not add runtime adapter code.
- [ ] This change does not add Helm templates.
- [ ] This change does not add UI/website assets.
- [ ] This change does not add module-specific enforcement logic.
- [ ] This change does not add secrets, credentials, or live backend integration.

## Doctrine impact

- [ ] Suite membership unchanged, or updated in doctrine and contracts.
- [ ] Module authority unchanged, or updated in doctrine and contracts.
- [ ] Callable interfaces unchanged, or updated in doctrine and contracts.
- [ ] Forbidden actions unchanged, or updated in doctrine and contracts.
- [ ] Composition Layer rules unchanged, or updated through phase evidence.
- [ ] SENTINEL control-point doctrine unchanged, or updated through phase evidence.
- [ ] Product packaging boundaries unchanged, or updated through phase evidence.
- [ ] Status taxonomy unchanged, or updated in doctrine and contracts.

## SOC 2 alignment

- [ ] SOC 2 traceability does not apply.
- [ ] SOC 2 traceability applies and has been updated.

## Agent adoption

- [ ] Downstream agents can determine whether this change affects their work.
- [ ] No local substitute doctrine was introduced outside this repository.
