from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

people = (
    spark.read.option("header", "true")
    .option("inferSchema", "true")
    .csv("data/fakefriends-header.csv")
)

print("Here is our inferred schema:")
people.printSchema()

print("Show name and age:")
people.select(people.name, people.age).show()

print("Show average age:")
people.select(avg(people.age)).show()

spark.stop()
