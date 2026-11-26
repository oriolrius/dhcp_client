## v0.2.0 (2026-11-26)

First public release on GitHub.

### Features

- `dhcp_client_v2.py`: starts the sniffer in a thread before it sends the Discover, so fast DHCP servers are not missed.
- `dhcp_client_dry.py`: the original send-then-sniff probe.
- Both scripts broadcast a `DHCPDISCOVER` and print every `DHCPOFFER` they get in 30 seconds.

### Docs

- New README: what the tool does, quick start with `uv`, the two scripts compared, example output, and a safety note.

### Build

- Commitizen manages versions (`pyproject.toml`, `v$version` tags, changelog on bump).
- Project description in `pyproject.toml`.
