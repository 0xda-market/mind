# 0xda-market mind

> Canonical durable organization context for `0xda-market`.

This repository is a standalone concrete organization implementation of the implementation-independent [Mind Protocol](https://github.com/aiaiaiai-org/mind-protocol).

## Organization identity

- **Organization:** `0xda-market`
- **Canonical subject id:** `0xda-market`
- **Parent organization:** [`aiaiaiai` / `4xAI`](https://github.com/aiaiaiai-org)
- **Owner / root identity:** [0x0sky](https://github.com/0x0sky)
- **Role:** digital commerce organization

The parent-child relationship above is durable authored human context inherited from this repository's historical baseline documentation. This initial protocol canary deliberately does not invent a machine relationship predicate for it; relationship semantics belong in an explicit authored relationship resource when that contract is intentionally published.

## Protocol contract

`manifest.yaml` is the machine-readable entry point. This concrete `0xda-market` Mind currently publishes:

- Mind Protocol: `0.9.0`;
- manifest schema: v3;
- organization context: `0.2.0`.

`mind-repository.yaml` declares this repository as a concrete Mind only. It is neither protocol authority nor template/reference authority. Its intended relationship to `aiaiaiai-org/mind-protocol` is an independent consumer, not GitHub fork inheritance.

`protocol.lock.yaml` keeps two facts separate:

- **current protocol authority:** `aiaiaiai-org/mind-protocol`;
- **immutable `0.9.0` release provenance:** `0x0sky/mind@v0.9.0`, commit `457844c8ced0318d91d628617ff6f8ec6f428ab7`.

The authority moved after `0.9.0`; that historical release is not recreated or rewritten in the new authority repository. Starting with `1.0.0-rc.1`, formal protocol releases are published from `aiaiaiai-org/mind-protocol`.

The lock pins the exact protocol descriptor, conformance contract, compatibility policy, and complete frozen schema set. Protocol version and organization context version remain independent.

## Historical baseline

The branch `foundation/baseline-v0.1.0` remains historical source material and is not rewritten. It represented an abstract baseline without a concrete subject. This `0.2.0` line is therefore a fresh concrete publication, not a claim that the old baseline is inside the supported protocol migration floor.

The repository already had a separate `master` history containing assistant/project configuration. This concrete line starts from that engineering history while explicitly preserving the authored organization facts from the historical baseline. Details are recorded in [`docs/migrations/foundation-to-mind-0.9.md`](docs/migrations/foundation-to-mind-0.9.md).

## Composition

```text
OrganizationMind
├── manifest.yaml
├── mind-repository.yaml
├── protocol.yaml
├── protocol.lock.yaml
├── conformance.yaml
├── compatibility.yaml
├── schema/
│   ├── protocol.schema.json
│   ├── mind.schema.json
│   ├── module.schema.json
│   ├── identity.schema.json
│   ├── identity-resource.schema.json
│   ├── relationships.schema.json
│   ├── visual-assets.schema.json
│   ├── conformance.schema.json
│   └── compatibility.schema.json
└── modules/
    └── identity/
```

## Canary boundary

The 0.9 synchronization is intentionally narrow:

- publish one universal organization Identity resource;
- pin the exact protocol release contract set;
- validate subject/owner binding and repository visibility;
- do not infer relationships from GitHub metadata;
- do not require a final logo or provider binding;
- do not copy generic parent-organization content into this repository.

Protocol compatibility is expressed by the exact release lock, not by GitHub fork ancestry. Full named visual-family, provider, project/product, and broader ecosystem enrichment remains a separate post-1.0 rollout.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
