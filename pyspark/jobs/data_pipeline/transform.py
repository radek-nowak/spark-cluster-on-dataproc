import logging

from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


class Transform:
    logger = logging.getLogger("Transform")

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def drop_nulls(self, data: DataFrame):
        """
        Drops nulls across the table.
        :param data: dataframe
        :return:
        """
        Transform.logger.info("Dropping NULLS from the table")
        return data.na.drop()
