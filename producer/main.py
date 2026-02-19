from confluent_kafka import Producer
import os

kafka_uri = os.getenv("KAFKA_URI")
topic_name = os.getenv("TOPIC_NAME","alert")
config = {"bootstrap.servers":kafka_uri}

producer = Producer(config)

producer.produce(topic=topic_name,value=)

producer.flush()