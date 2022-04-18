import extract
import transform
import logging
import logging.config

from pyspark.sql import SparkSession


class Pipeline:
    logging.config.fileConfig("resources/configs/logging.conf")

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def run_pipeline(self):
        """
        Runs the pipeline
        :return:
        """

        logging.info("run_pipeline method started. Running a pipeline")

        extractor = extract.Extract(self.spark)
        transformer = transform.Transform(self.spark)

        df = extractor.extract_data("../../test/data/sample_data_1.csv")
        df.show()
        df = transformer.drop_nulls(df)
        df.show()
