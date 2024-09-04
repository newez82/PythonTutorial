"""
    Spark SQL and SQL Operations

    1. Spark SQL is module in Apache Spark that enables querying structured and semi-structured
    data using SQL commands.

    2. it extends Spark's capabilities to handle strutured data effectively, allows users to seamlessly
    switch between SQL queries and Spark's core APIs for data processing.

    Key Features of Spark SQL

    1. Unified Data Processing - Spark Sql provides a unified API for both batch adn real-time
    data processing, simplifying end to end data pipeline development.

    2. Schema Ingerence - Automatically infers structured data sources' schema, reducing the need for
    explicit schema definitions.

    3. Data Source Abstraction - Supports a wide range of data sources (Hive, Parquet, Avro, ORC, 
    JSON, JDBC), enhancing versatility for working with various data formats.

    4. Integration with Hive: Seamlessly integrates with Apache Hive, enabling Hive query execution
    and access to Hive UDFs within Spark SQL.    
"""

import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

spark = SparkSession.builder.appName("DataFrameSQL").getOrCreate()
data_file_path = (
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\pySpark\\data\\persons.csv"
)
df = spark.read.csv(data_file_path, header=True, inferSchema=True)
df.printSchema()
print("Inital DataFrame:")
df.show()

# To run SQL Queries on DataFrame, we need to register it as a temporary view.
df.createOrReplaceTempView("my_table")

# perform SQL-like Queries
result = spark.sql("SELECT * FROM my_table WHERE age > 25")
result.show()


# compute the average salary by gender
avg_salary_by_gender = spark.sql(
    "SELECT gender, AVG(salary) as avg_salary FROM my_table GROUP BY gender"
)
avg_salary_by_gender.show()

##########################################################
# creating and managing temporary views
##########################################################
# create a temporary view
df.createOrReplaceTempView("people")

# query teh temporary view
result = spark.sql("SELECT * from people WHERE age > 25")
result.show()

# check if a temporary view exists
view_exists = spark.catalog.tableExists("people")
print("is temporary people view exists:", view_exists)

# drop a temporary view
spark.catalog.dropTempView("people")

# check if a temporary view eixts
view_exists = spark.catalog.tableExists("people")
print("is temporary people view exists:", view_exists)

##########################################################
# subqueries
##########################################################
# Create DataFarmes
employee_data = [
    (1, "John"),
    (2, "Alice"),
    (3, "Bob"),
    (4, "Emily"),
    (5, "David"),
    (6, "Sarah"),
    (7, "Michael"),
    (8, "Lisa"),
    (9, "William"),
]

employees = spark.createDataFrame(employee_data, ["id", "name"])
employees.show()

salary_data = [
    ("HR", 1, 60000),
    ("HR", 2, 55000),
    ("HR", 3, 58000),
    ("IT", 4, 70000),
    ("IT", 5, 72000),
    ("IT", 6, 68000),
    ("Sales", 7, 75000),
    ("Sales", 8, 78000),
    ("Sales", 9, 77000),
]

salaries = spark.createDataFrame(salary_data, ["department", "id", "salary"])
salaries.show()

# Register as temporary views
employees.createOrReplaceTempView("employees")
salaries.createOrReplaceTempView("salaries")

# subquery to find employees with salaries above average
result = spark.sql(
    """
    SELECT name
    FROM employees
    WHERE id IN (SELECT id 
                FROM salaries
                WHERE salary > (SELECT AVG(salary) FROM salaries))

"""
)
result.show()

##########################################################
# window function
# allow us to perform calculations across a window of rows
# defined by an ordered parition of the data
# ROW_NUMBER(), RANK(), DENSE_RANK(), SUM(), AVG(), etc.
##########################################################
employee_salary = spark.sql(
    """
    SELECT salaries.*, employees.name
    FROM salaries
    left join employees on salaries.id=employees.id
"""
)
employee_salary.show()

# create a window specification
window_spec = Window.partitionBy("department").orderBy(F.desc("salary"))

# calculate the rank of employees within each department based on salary
employee_salary.withColumn("rank", F.rank().over(window_spec)).show()
spark.stop()
