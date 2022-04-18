from pyspark.sql import SparkSession
import logging


class Extract:
    logger = logging.getLogger("Extract")

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def extract_data(self, bucket_path: str):
        """
        Extracts the date from a file
        :param bucket_path:
        :return:
        """
        Extract.logger.info(f"extract_data method started. Extracting the data from {bucket_path}")
        return self.spark.read.csv(bucket_path, header=True)
