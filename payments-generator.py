from confluent_kafka import Producer
import json
import random
import time
from faker import Faker

fake = Faker()

BOOTSTRAP_SERVERS = "localhost:9092"

producer_conf = {"bootstrap.servers": BOOTSTRAP_SERVERS}
producer = Producer(producer_conf)
payments_topic = "payments"


def generate_transaction():
    # create dummy payment object
    card_types = ["mastercard", "visa16", "visa19"]
    card_type = random.choice(card_types)
    transaction = {
        "cardNumber": fake.credit_card_number(card_type),
        "expiryDate": fake.credit_card_expire(),
        "cvv": fake.credit_card_security_code(),
        "cardHolderName": fake.name(),
        "cardType": card_type,
        "amount": round(random.uniform(10.0, 500.0), 2),
        "currency": "USD",
        "timestamp": int(time.time()),
        "merchantId": fake.uuid4(),
        "merchantName": fake.company(),
        "transactionType": random.choice(["online_purchase", "in_store"]),
        "location": fake.address(),
        "transactionStatus": random.choice(["approved", "declined", "pending"]),
        "authorizationCode": fake.ean8(),
    }
    # publish payment to kafka
    print("Publishing message: {}".format(transaction))
    producer.produce(payments_topic, json.dumps(transaction).encode("utf-8"))
    producer.flush()


while True:
    generate_transaction()
    time.sleep(1)
