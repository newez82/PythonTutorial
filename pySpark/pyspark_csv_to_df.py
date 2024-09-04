"""
    Create DataFrames from Various Data Sources
"""

############################################################
# Read CSV file into DataFrame
############################################################
from pyspark.sql import SparkSession

# define schema using StructType and StructField classes along with data types
from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)

spark = SparkSession.builder.appName("ReadFromCSV").getOrCreate()
csv_file_path = (
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\pySpark\\data\\products.csv"
)
df = spark.read.csv(csv_file_path, header=True)

# Display DataFrame Schema to find data type of each column
df.printSchema()

# Display DataFrame's content
df.show()

# Update data type since it should not be all Stirng
schema = StructType(
    [
        StructField(name="id", dataType=IntegerType(), nullable=True),
        StructField(name="name", dataType=StringType(), nullable=True),
        StructField(name="category", dataType=StringType(), nullable=True),
        StructField(name="quantity", dataType=IntegerType(), nullable=True),
        StructField(name="price", dataType=DoubleType(), nullable=True),
    ]
)

df = spark.read.csv(csv_file_path, header=True, schema=schema)
df.printSchema()
df.show()

# inferSchema allows Spark to automatically guess the data types of columns
# it saves us from manually defining schemas
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)
df.printSchema()
df.show()


############################################################
# Read JSON file into DataFrame
############################################################
# read single line json file
json_file_path = (
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\pySpark\\data\\products.json"
)
df = spark.read.json(json_file_path)
df.printSchema()
df.show()

# read mulit-lines json file
json_file_path = "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\pySpark\\data\\productsArrays.json"
df = spark.read.json(json_file_path, multiLine=True)
df.printSchema()
df.show()

############################################################
# Read Parquet file into DataFrame
# it is a columnar storage format that's highly optimized
# for analytics workloads.
############################################################
# write dataframe into parquet file
# parquet_file_path = (
#     "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\pySpark\\data\\products.parquet"
# )
# df.write.parquet(parquet_file_path, mode="overwrite")

# read parquet file from dataframe
# df.read.parquet(parquet_file_path)
# df.printSchema()
# df.show()

df.stop()
