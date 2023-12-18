from confluent_kafka import Consumer
import json

BOOTSTRAP_SERVERS = "localhost:9092"

payments_topic = "payments"

consumer_conf = {
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "group.id": "data-processing",
    "auto.offset.reset": "earliest",
}
consumer = Consumer(consumer_conf)
consumer.subscribe([payments_topic])


def process_transaction():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        payment = msg.value().decode("utf-8")
        print("Received message: {}".format(payment))


process_transaction()
