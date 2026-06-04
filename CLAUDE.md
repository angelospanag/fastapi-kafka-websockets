# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

All tasks run via `mise run <task>`. The toolchain (Python 3.14, uv) is pinned in `mise.toml`.

| Task | Command |
|---|---|
| Install deps | `mise run install` |
| Dev server | `mise run dev` |
| Production server | `mise run serve` |
| Format | `mise run fmt` |
| Lint | `mise run lint` |
| Type check | `mise run typecheck` |
| Vulnerability audit | `mise run vuln` |
| Upgrade deps | `mise run deps` |

## Architecture

`app/main.py` owns the FastAPI application. It exposes two endpoints:

- `GET /` — serves the UI via a Jinja2 template (`templates/index.html`)
- `WS /ws` — WebSocket endpoint that creates an `AIOKafkaConsumer`, reads messages from the configured topic, and forwards them to the connected client

`app/config.py` uses `pydantic-settings` to load Kafka connection parameters from a `.env` file at the repo root. Settings are cached via `@lru_cache`.

The app requires a running Kafka broker. See the README for how to start Kafka and produce messages.
