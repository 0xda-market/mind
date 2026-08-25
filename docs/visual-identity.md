# Canonical visual identity

`0xda-market/mind` is the canonical publication source for the `0xda-market` compact emblem.

The universal Mind Protocol defines only the semantics of `identity.visual_identity.primary_mark` and visual-asset resolution. This concrete Mind owns the named mark, its exact bytes, its SHA-256 integrity, and the independent organization context version that introduces it.

## Source of truth

- canonical identity: `modules/identity/identity.yaml`;
- asset catalog: `modules/identity/visual-assets.yaml`;
- canonical SVG: `assets/visual/0xda-market/compact-emblem.svg`;
- deterministic provider projection: `python scripts/export_visual_assets.py`.

The SVG uses the established `#93C482` identity green on transparent geometry. Provider projection uses a white 1024×1024 canvas. GitHub avatars and other provider copies are downstream projections and never become identity authority.

## Integrity

`python scripts/validate_visual_assets.py` validates the catalog, canonical binding, controlled SVG path and SHA-256 digest. `python scripts/export_visual_assets.py --check` verifies that the controlled SVG geometry still produces the approved provider-ready PNG bytes.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
