# Assistant Configuration

This directory contains machine-facing configuration for AI assistants working with this repository and the wider `0xda-market` project.

## Files

### `0x0da.yaml`

Defines the vendor-independent assistant identity, engineering principles, communication rules, language policy, boundaries, decision model, and code standards.

### `chatgpt.yaml`

Defines the ChatGPT-specific project contract for:

- GitHub access and capabilities;
- repository conventions;
- engineering workflow and autonomy;
- approval boundaries;
- CI and pull request policy;
- concise execution reporting.

## Rules

- Keep vendor-independent behavior in `0x0da.yaml`.
- Keep ChatGPT-specific operational instructions in `chatgpt.yaml`.
- Store project knowledge under `projects/`.
- Store current priorities under `state/`.
- Store historical material under `archive/`.
- Do not duplicate implementation details.
- Prefer references to canonical repository files over copied context.
- Never commit credentials, tokens, secrets, or private production data.
