# Provider avatar projection

The canonical `0xda-market` identity mark lives in this repository as SVG. Provider surfaces consume a generated projection; they do not define the identity.

For GitHub, generate the square 1024×1024 white-canvas PNG with:

```sh
python scripts/export_visual_assets.py
```

The approved provider projection has SHA-256 `7761193cf5360dac36738aa68a8ddbc902838a8369d9acc766babdf2680aca7f` when produced with the pinned CI renderer dependency. Uploading that projection to GitHub is a manual provider action and is intentionally separate from merging the canonical Mind publication.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
