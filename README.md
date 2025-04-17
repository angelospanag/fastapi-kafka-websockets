# fastapi-kafka-websockets

Experimenting with a full flow of sending messages from an Apache Kafka consumer, to a FastAPI websockets endpoint, to a UI using a JavaScript websockets connection.

- [fastapi-kafka-websockets](#fastapi-kafka-websockets)
  - [Prerequisites](#prerequisites)
    - [Quick install for MacOS](#quick-install-for-macos)
  - [Running](#running)
    - [Start Apache Kafka (using MacOS and `brew`)](#start-apache-kafka-using-macos-and-brew)
    - [Start Kafka producer](#start-kafka-producer)
    - [Start Kafka consumer](#start-kafka-consumer)
    - [Run server](#run-server)

## Prerequisites

### Quick install for MacOS

```bash
brew install python@3.13 uv kafka
```

## Running

### Start Apache Kafka (using MacOS and `brew`)

```bash
brew services start zookeeper
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

### Run server

```bash
uvicorn main:app --reload
```
