from pyspark.sql import SparkSession
import extract
import transform
import pipeline
import logging
import logging.config


def main():
    spark = SparkSession. \
        builder. \
        appName("AppName"). \
        getOrCreate()

    pipeline_process = pipeline.Pipeline(spark)
    pipeline_process.run_pipeline()


if __name__ == "__main__":
    main()
