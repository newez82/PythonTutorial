import os
import sys

from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


import findspark

findspark.init()

spark = SparkSession.builder.appName("parquetFile").getOrCreate()
csv_file_path = (
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\pySpark\\data\\products.csv"
)
# df = spark.read.csv(csv_file_path, header=True)
data = [
    ("James ", "", "Smith", "36636", "M", 3000),
]
columns=["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data, columns)
df.show()
df.write.parquet(
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\pySpark\\data\\products.parquet",
    mode="overwrite",
)
# df.stop()
