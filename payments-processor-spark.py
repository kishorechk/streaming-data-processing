from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StringType,
    TimestampType,
    StructType,
    StructField,
    DoubleType,
)
from pyspark.sql.functions import from_json, window, count, avg, when, col

BOOTSTRAP_SERVERS = "localhost:9092"

PAYMENTS_TOPIC = "payments"

spark = (
    SparkSession.builder.appName("Payments processing")
    .config("spark.streaming.stopGracefullyOnShutdown", True)
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0")
    .config("spark.sql.shuffle.partitions", 4)
    .master("local[*]")
    .getOrCreate()
)

windowDuration = "30 seconds"
slideDuration = "5 seconds"
json_schema = StructType(
    [
        StructField("cardNumber", StringType(), True),
        StructField("expiryDate", StringType(), True),
        StructField("timestamp", TimestampType(), True),
        StructField("amount", DoubleType(), True),
    ]
)


def process_transaction():
    try:
        df = (
            spark.readStream.format("kafka")
            .option("kafka.bootstrap.servers", BOOTSTRAP_SERVERS)
            .option("subscribe", PAYMENTS_TOPIC)
            .load()
        )

        json_df = df.selectExpr("cast(value as string) as value")

        json_expanded_df = json_df.withColumn(
            "value", from_json(json_df["value"], json_schema)
        ).select("value.*")

        print("Received message:")
        json_expanded_df.printSchema()

        json_expanded_df = json_expanded_df.withWatermark("timestamp", "1 minute")

        windowed_df = json_expanded_df.groupBy(
            window("timestamp", windowDuration, slideDuration), "cardNumber"
        )

        transaction_count = windowed_df.agg(
            count("*").alias("transactionCount"),
            avg("amount").alias("avgTransactionAmount"),
        )

        query = (
            transaction_count.writeStream.outputMode("append")
            .format("console")
            .trigger(processingTime="5 seconds")
            .start()
        )
        query.awaitTermination()
    except:
        print("Something went wrong")


process_transaction()
