# fastapi-kafka-websockets

## Download and extract Kafka
```bash
wget https://archive.apache.org/dist/kafka/3.3.1/kafka_2.13-3.3.1.tgz
tar -xzf kafka_2.13-3.3.1.tgz 
cd kafka_2.13-3.3.1
```

## Start Kafka server
```bash
bin/kafka-server-start.sh config/kraft/server.properties
```

## Start Kafka producer
```bash
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
```


## Start Kafka consumer
```bash
bin/kafka-console-consumer.sh --topic quickstart-events --from-beginningv --bootstrap-server localhost:9092 
```
