# 0xda-market mind

> Canonical durable organization context for `0xda-market`.

This repository is a standalone concrete organization implementation of the implementation-independent [Mind Protocol](https://github.com/aiaiaiai-org/mind-protocol).

## Organization identity

- **Organization:** `0xda-market`
- **Canonical subject id:** `0xda-market`
- **Parent organization:** [`aiaiaiai` / `4xAI`](https://github.com/aiaiaiai-org)
- **Owner / root identity:** [0x0sky](https://github.com/0x0sky)
- **Role:** digital commerce organization

The parent-child relationship above is durable authored human context inherited from this repository's historical baseline documentation. This RC synchronization still does not invent a machine relationship predicate for it.

## Protocol contract

`manifest.yaml` is the machine-readable entry point. This concrete `0xda-market` Mind currently publishes:

- Mind Protocol: `1.0.0-rc.1`;
- manifest schema: v3;
- organization context: `0.2.0`.

`mind-repository.yaml` declares this repository as a concrete Mind only. It is neither protocol authority nor template/reference authority. Its relationship to `aiaiaiai-org/mind-protocol` is `independent_consumer`.

Exact release provenance:

- authority/release repository: `aiaiaiai-org/mind-protocol`;
- tag: `v1.0.0-rc.1`;
- commit: `6bf8467f0e3990808464e118cc60cc83d8ab2ced`.

`protocol.lock.yaml` pins the exact protocol descriptor, conformance contract, compatibility policy, and complete frozen schema set. The schema bytes remain the frozen pre-1.0 shapes; only the consumed release binding advances to the RC.

Protocol version and organization context version remain independent. Canonical Identity stays `organization:0xda-market`, and `mind.context_version` stays `0.2.0`.

## Historical baseline

The branch `foundation/baseline-v0.1.0` remains historical source material and is not rewritten. It represented an abstract baseline without a concrete subject. This `0.2.0` line remains the concrete organization context line.

Details of the original bridge are recorded in [`docs/migrations/foundation-to-mind-0.9.md`](docs/migrations/foundation-to-mind-0.9.md).

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
└── modules/
    └── identity/
```

## Consumer boundary

This synchronization intentionally remains narrow:

- preserve one authored organization Identity resource;
- pin the exact immutable RC contract set;
- validate subject/owner binding and repository visibility;
- do not infer relationships from GitHub metadata;
- do not require or invent a final visual identity;
- do not copy generic parent-organization context into this repository.

Protocol compatibility is expressed by the exact release lock, not GitHub fork ancestry. Full named visual-family, provider, project/product, and broader ecosystem enrichment remains post-`1.0.0` work.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
