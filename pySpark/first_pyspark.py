"""
    pySpark
"""

# import SparkSession class from pyspark.sql model.
# SparkSession class is the entry point for working
# with structured data using Spark SQL.
# from pyspark.sql import SparkSession
import os
import sys

from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
# Create spark object using builder pattern
# appName sets the name of the spark application
# getOrCreate() either retrieves an existing spark
# session or creat a new one if it doesn't exist
spark = SparkSession.builder.appName("PySpark get Started").getOrCreate()

# Create Spark DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Show the DataFrame
df.show()


