# 0xda-market mind

> Canonical durable organization context for `0xda-market`.

This repository is a concrete organization implementation of the implementation-independent [Mind Protocol](https://github.com/0x0sky/mind).

## Organization identity

- **Organization:** `0xda-market`
- **Canonical subject id:** `0xda-market`
- **Parent organization:** [`aiaiaiai` / `4xAI`](https://github.com/aiaiaiai-org)
- **Owner / root identity:** [0x0sky](https://github.com/0x0sky)
- **Role:** digital commerce organization

The parent-child relationship above is durable authored human context inherited from this repository's historical baseline documentation. This initial protocol canary deliberately does not invent a machine relationship predicate for it; relationship semantics belong in an explicit authored relationship resource when that contract is intentionally published.

## Protocol contract

`manifest.yaml` is the machine-readable entry point. This is the first concrete `0xda-market` mind line:

- Mind Protocol: `0.9.0`;
- manifest schema: v3;
- organization context: `0.2.0`.

`protocol.lock.yaml` pins the exact immutable upstream `v0.9.0` tag and commit, protocol descriptor, conformance contract, compatibility policy, and complete frozen schema set. Protocol version and organization context version are independent.

## Historical baseline

The branch `foundation/baseline-v0.1.0` remains historical source material and is not rewritten. It represented an abstract baseline without a concrete subject. This `0.2.0` line is therefore a fresh concrete publication, not a claim that the old baseline is inside the supported protocol migration floor.

The repository already had a separate `master` history containing assistant/project configuration. This concrete line starts from that engineering history while explicitly preserving the authored organization facts from the historical baseline. Details are recorded in [`docs/migrations/foundation-to-mind-0.9.md`](docs/migrations/foundation-to-mind-0.9.md).

## Composition

```text
OrganizationMind
├── manifest.yaml
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

Full named visual-family, provider, project/product, and broader ecosystem enrichment remains a separate post-1.0 rollout.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
