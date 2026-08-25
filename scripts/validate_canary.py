#!/usr/bin/env python3
# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Validate the 0xda-market concrete Mind Protocol 0.9 consumer boundary."""

from __future__ import annotations

import sys
from pathlib import Path

from validate_manifest import load_yaml_mapping

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ENTITY = {"type": "organization", "id": "0xda-market"}
EXPECTED_PROTOCOL_CONSUMPTION = {
    "id": "mind",
    "version": "0.9.0",
    "authority_repository": "aiaiaiai-org/mind-protocol",
    "release_repository": "0x0sky/mind",
    "release_tag": "v0.9.0",
    "release_commit": "457844c8ced0318d91d628617ff6f8ec6f428ab7",
    "floating_master": "forbidden",
}


def validate() -> list[str]:
    errors: list[str] = []
    manifest = load_yaml_mapping(ROOT / "manifest.yaml")
    repository = load_yaml_mapping(ROOT / "mind-repository.yaml")
    mind = manifest.get("mind", {})

    if manifest.get("schema_version") != 3:
        errors.append("manifest schema_version must be 3")
    if manifest.get("protocol") != {"id": "mind", "version": "0.9.0"}:
        errors.append("manifest must consume Mind Protocol 0.9.0")
    if mind.get("name") != "mind@0xda-market":
        errors.append("canonical mind name must be mind@0xda-market")
    if mind.get("context_version") != "0.2.0":
        errors.append("concrete context line must remain 0.2.0")
    if mind.get("subject") != EXPECTED_ENTITY or mind.get("owner") != EXPECTED_ENTITY:
        errors.append("subject and publication owner must remain organization:0xda-market")

    roles = repository.get("repository", {}).get("roles", {})
    if roles.get("protocol_authority") != {"enabled": False}:
        errors.append("0xda-market/mind must not declare protocol authority")
    concrete = roles.get("concrete_mind", {})
    if concrete.get("enabled") is not True or concrete.get("canonical_for_subject") != EXPECTED_ENTITY:
        errors.append("repository must be a concrete Mind canonical only for organization:0xda-market")
    if concrete.get("reference_implementation") is not False or concrete.get("template_authority") is not False:
        errors.append("concrete organization Mind must not be reference or template authority")
    if repository.get("protocol_consumption") != EXPECTED_PROTOCOL_CONSUMPTION:
        errors.append("repository metadata must separate current authority from historical v0.9.0 release provenance")
    if repository.get("fork_policy", {}).get("relationship_to_protocol_repository") != "independent_consumer":
        errors.append("protocol relationship must be independent_consumer")

    modules = manifest.get("modules", {})
    if modules.get("required") != ["identity"] or modules.get("registered") != ["identity"]:
        errors.append("0.9 canary must contain only the authored identity module")

    descriptor = load_yaml_mapping(ROOT / "modules/identity/module.yaml")
    if descriptor.get("module", {}).get("owner") != EXPECTED_ENTITY:
        errors.append("identity module owner must be organization:0xda-market")

    identity = load_yaml_mapping(ROOT / "modules/identity/identity.yaml").get("identity")
    if identity != {"type": "organization", "id": "0xda-market", "display_name": "0xda-market"}:
        errors.append("canonical Identity must remain organization:0xda-market")
    if isinstance(identity, dict) and "visual_identity" in identity:
        errors.append("0.9 canary must not invent canonical visual identity")
    if (ROOT / "modules/relationships/module.yaml").exists():
        errors.append("0.9 canary must not invent a relationship module")

    return errors


def main() -> int:
    try:
        errors = validate()
    except (OSError, ValueError, TypeError) as error:
        print(f"0xda-market canary validation failed:\n- {error}", file=sys.stderr)
        return 1
    if errors:
        print("0xda-market canary validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("0xda-market is a standalone concrete 0.9 consumer with truthful protocol provenance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
