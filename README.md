# Real-time Stream Processing with Kafka and Spark

This project demonstrates the implementation of a streaming data pipeline using Apache Kafka and Apache Spark for real-time analytics of credit card payment transactions.

## Table of Contents

- [Introduction](#introduction)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Generating Payment Transactions](#generating-payment-transactions)
- [Stream Processing](#stream-processing)

## Introduction

The blog post associated with this repository walks through the process of setting up a streaming data pipeline, aggregating payment transactions in real-time, and highlights the importance of stream processing for fraud detection.

## Tech Stack

- **Python:** Used for application development and scripting.
- **Apache Kafka:** Used as the messaging backbone for real-time data streams.
- **Apache Spark:** Utilized for stream processing and analytics.
- **Docker:** Enables easy setup and management of Kafka and Zookeeper services.

## Prerequisites

Ensure you have the following prerequisites installed:

- Docker
  - **Mac users:** `brew install --cask docker`
  - **Windows users:** `choco install docker-desktop`

## Getting Started

1. **Setup Kafka Cluster:**
   - Use `docker-compose.yml` to set up a local Kafka cluster with Zookeeper.

2. **Generating Payment Transactions:**
   - Run `payments-generator.py` to generate synthetic transaction data using Faker library.

3. **Stream Processing:**
   - Execute `process_transaction.py` to process payment transactions in real-time using Spark.

## Generating Payment Transactions

The `payments-generator.py` script generates synthetic payment transactions, simulating real-world data for demonstration purposes. It utilizes the Faker library to create transactions with various fields.

## Stream Processing

The `process_transaction.py` script consumes payment transactions from Kafka, performs windowed aggregations, and calculates transaction counts and average amounts per window for fraud detection.

For detailed information and a step-by-step guide, refer to the associated [blog post](https://medium.com/@kishorchukka/stream-processing-with-kafka-and-spark-b6fd7e2144bb)https://medium.com/@kishorchukka/stream-processing-with-kafka-and-spark-b6fd7e2144bb.

Feel free to reach out for any queries or suggestions!

