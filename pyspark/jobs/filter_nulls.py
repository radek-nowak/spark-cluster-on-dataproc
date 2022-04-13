import pyspark.sql
from pyspark.sql import SparkSession


def null_filter(data: pyspark.sql.DataFrame) -> pyspark.sql.DataFrame:
    """
    Filters null values from the dataframe.

    :param data: dataframe to clean
    :return: pyspark.sql.DataFrame
    """
    return data.na.drop()


def main():
    spark = SparkSession. \
        builder. \
        appName("NullFilter"). \
        getOrCreate()
    data = spark.read.csv("../test/data/sample_data_1.csv", header="true")
    data = null_filter(data)
    data.show()


if __name__ == '__main__':
    main()
