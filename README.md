# fastapi-kafka-websockets

Experimenting with a full flow of sending messages from an Apache Kafka consumer, to a FastAPI websockets endpoint, to a
UI using a JavaScript websockets connection.

<!-- TOC -->
* [fastapi-kafka-websockets](#fastapi-kafka-websockets)
  * [Prerequisites](#prerequisites)
    * [Quick install for MacOS](#quick-install-for-macos)
    * [Create a `.env` file at the root of the project](#create-a-env-file-at-the-root-of-the-project)
  * [Running](#running)
    * [Start Apache Kafka (using MacOS and `brew`)](#start-apache-kafka-using-macos-and-brew)
    * [Start Kafka producer](#start-kafka-producer)
    * [Start Kafka consumer](#start-kafka-consumer)
    * [Start server](#start-server)
      * [Development server](#development-server)
      * [Production server](#production-server)
  * [Linting](#linting)
  * [Formatting](#formatting)
<!-- TOC -->

## Prerequisites

### Quick install for MacOS

```bash
brew install python@3.13 uv kafka
```

### Create a `.env` file at the root of the project

```dotenv
TOPICS=quickstart-events
BOOTSTRAP_SERVERS=localhost:9092
GROUP_ID=my-group
AUTO_OFFSET_RESET=latest
```

## Running

### Start Apache Kafka (using MacOS and `brew`)

```bash
brew services start kafka
```

### Start Kafka producer

```bash
kafka-console-producer --topic quickstart-events --bootstrap-server localhost:9092
```

### Start Kafka consumer

```bash
kafka-console-consumer --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
```

### Start server

#### Development server

```bash
uv run fastapi dev app/main.py
```

#### Production server

```bash
uv run fastapi run app/main.py
```

Visit http://localhost:8000 and send some text from the Kafka console producer. The text will appear on your screen,
after being picked up by the Kafka consumer of the backend, and sent through a websockets connection to the UI.

## Linting

```bash
ruff check app/*
```

## Formatting

```bash
ruff format app/*
```
