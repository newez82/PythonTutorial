"""
    DataFrame Operations - Select, Filter, Group, Aggregate, Join, Sort, Drop, etc.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc

spark = SparkSession.builder.appName("DataFrame-Operations").getOrCreate()

data_file_path = (
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\pySpark\\data\\stock.txt"
)
df = spark.read.csv(data_file_path, header=True, inferSchema=True)
df.printSchema()
print("Initial DataFrame:")
df.show(10)

# select specific columns
selected_columns = df.select("id", "name", "price")
print("Selected Columns:")
selected_columns.show(10)

# apply conditions to filter rows
filtered_data = df.filter(df.quantity > 20)
print("Filtered Data:", filtered_data.count())
filtered_data.show()

# GroupBy and aggregations data based on specific columns
grouped_data = df.groupBy("category").agg({"quantity": "sum", "price": "avg"})
print("Grouped and Aggregated Data:")
grouped_data.show()


# combine multiple DataFrames based on specified columns
df2 = df.select("id", "category").limit(10)
joined_data = df.join(df2, "id", "inner")
print("Joined Data")
joined_data.show()


# Arrange rows based on one or more columns
sorted_data = df.orderBy("price")
print("Sorted Data:")
sorted_data.show(10)

# Sorted by mulitple columns
sorted_data = df.orderBy(col("price").desc(), col("id").desc())
print("Sorted Data Descending:")
sorted_data.show(10)

# Get Unique rows
distinct_rows = df.select("category").distinct()
print("Distinct Product Categories:")
distinct_rows.show()


# Remove specified Columns
dropped_columns = df.drop("quantity", "category")
print("Dropped Columns")
dropped_columns.show(10)

# Add new calculated Columns
df_with_new_column = df.withColumn("revenue", df.quantity * df.price)
print("DataFrame with New Column:")
df_with_new_column.show(10)

# Rename columns for better readability
df_with_alias = df.withColumnRenamed("price", "product_price")
print("DataFrame with Alised Column:")
df_with_alias.show(10)

spark.stop()
