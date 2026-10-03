# Agent guidance

This Home Assistant integration restores historical light attributes in the recorder database. Check the README's recorder-storage guidance when changing which attributes or states are recorded. Prefer focused changes to `custom_components/light_reilluminator/`.

The configured local checks are `ruff check .`, `ruff format . --check`, Home Assistant hassfest, and HACS validation; the latter two run in GitHub Actions. `scripts/lint` fixes and rewrites files, so use the read-only Ruff commands when validating an edit. There is no test suite in this checkout. `scripts/develop` starts a local Home Assistant instance and `scripts/setup` installs dependencies; use them only when that local development environment is part of the requested work.

Recorder changes can increase stored history. Keep behavior and storage implications clear in the README. Validate source locally without connecting to Ron's Home Assistant or changing its configuration; a live installation or runtime check needs explicit authorization.
