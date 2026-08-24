# Foundation baseline to Mind Protocol 0.9

This document records the first concrete `0xda-market` Mind publication from the repository's historical abstract baseline lineage.

## Historical state

- historical baseline branch: `foundation/baseline-v0.1.0`
- observed baseline tip: `5efd81842389e5fa8d273c29e589eea6c36c2220`
- baseline manifest schema: `1`
- baseline context version: `0.1.0`
- baseline subject: not concrete
- existing `master` before this work: `256cb7a4b328f9d981ce33eeb80ec5c980a9c6ab`
- destination protocol: `0.9.0`
- destination manifest schema: `3`
- first concrete context version: `0.2.0`

The baseline is below Mind Protocol 0.9's supported `0.6.0` migration floor and does not contain a concrete subject. This is intentionally a fresh concrete publication, not a supported automated migration from `0.1.0`.

## Branch preservation

The historical baseline branch is preserved untouched as source history. The repository also already had a divergent `master` line containing assistant/project configuration. Rather than force-rewriting either branch, the concrete 0.9 work starts from the existing `master` engineering line and explicitly reconciles the durable organization facts authored in the baseline README.

Changing the repository's default branch from the historical baseline to `master` is repository metadata, not protocol semantics. It must be completed separately if the available GitHub integration cannot mutate that setting directly.

## Authored facts preserved

The historical README explicitly authored:

- organization `0xda-market`;
- parent organization `aiaiaiai` ecosystem membership;
- root owner `0x0sky`;
- digital-commerce role.

Those human-readable facts remain in the concrete README. No parent-child relationship predicate is invented in machine-readable form during this canary because no such relationship resource was previously authored.

## Protocol consumption

The concrete mind consumes the immutable `0x0sky/mind` release tag `v0.9.0` at commit `457844c8ced0318d91d628617ff6f8ec6f428ab7`.

`protocol.lock.yaml` records the exact protocol descriptor, conformance contract, compatibility policy, and complete frozen schema set with Git blob SHA-1 fingerprints. CI proves that the local frozen schema descriptors match the release compatibility freeze exactly.

Protocol tags are not created in this concrete repository. Protocol version and `0xda-market` context version remain independent.

## Concrete publication boundary

The first `0.2.0` line publishes only what is required for a valid organization canary:

- manifest v3;
- subject and publication owner `organization:0xda-market`;
- one universal Identity resource;
- exact protocol-release machine contracts;
- public visibility boundaries;
- validation and CI.

It deliberately does not invent relationships, provider bindings, products/projects, or canonical visual assets.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
