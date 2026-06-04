# fastapi-kafka-websockets

Experimenting with a full flow of sending messages from an Apache Kafka consumer, to a FastAPI websockets endpoint, to a UI using a JavaScript websockets connection.

<!-- TOC -->
* [fastapi-kafka-websockets](#fastapi-kafka-websockets)
  * [Getting Started](#getting-started)
  * [Running](#running)
  * [Development](#development)
<!-- TOC -->

## Getting Started

[`mise`](https://mise.jdx.dev/) manages the pinned toolchain (Python 3.14, uv).

**macOS / Linux**

```bash
curl https://mise.run | sh
```

**Windows**

```bash
winget install jdx.mise
```

Activate mise in your shell so the pinned versions take precedence over any system installs (Homebrew, etc.). In `~/.zshrc`:

```bash
eval "$(mise activate zsh)"
```

Then, in the repo:

```bash
mise trust        # one-time, confirms you trust this repo's mise.toml
mise install      # downloads and pins Python and uv
mise run install  # installs dependencies into .venv
```

Create a `.env` file at the root of the project:

```dotenv
TOPICS=quickstart-events
BOOTSTRAP_SERVERS=localhost:9092
GROUP_ID=my-group
AUTO_OFFSET_RESET=latest
```

## Running

Install Kafka (macOS):

```bash
brew install kafka
brew services start kafka
```

Start a Kafka producer to send messages:

```bash
kafka-console-producer --topic quickstart-events --bootstrap-server localhost:9092
```

Start the server:

```bash
mise run dev
```

Visit http://localhost:8000 and send some text from the Kafka console producer. The text will appear on your screen after being picked up by the Kafka consumer in the backend and forwarded through the WebSocket connection.

## Development

| Command              | Description                          |
|----------------------|--------------------------------------|
| `mise run install`   | Install dependencies into `.venv`    |
| `mise run dev`       | FastAPI dev server on 127.0.0.1:8000 |
| `mise run serve`     | Production server on 0.0.0.0:8000    |
| `mise run fmt`       | Format code via `ruff format`        |
| `mise run lint`      | Lint code via `ruff check`           |
| `mise run typecheck` | Type check via `ty check`            |
| `mise run vuln`      | Audit deps for known vulnerabilities |
| `mise run deps`      | Update and sync dependencies         |
