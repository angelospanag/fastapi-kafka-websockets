# fastapi-kafka-websockets

## Prerequisites

### Quick install for MacOS

```bash
brew install python@3.13 uv kafka
```

### Start Apache Kafka (using MacOS and `brew`)

```bash
brew services start zookeeper
brew services start kafka
```

## Start Kafka producer

```bash
kafka-console-producer --topic quickstart-events --bootstrap-server localhost:9092
```

## Start Kafka consumer

```bash
kafka-console-consumer --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
```

## Run server

```bash
uvicorn main:app --reload
```
