import pydantic
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

# --- PHASE A ---
spark = SparkSession.builder.appName("ComplexLogic").getOrCreate()
lookup_table = {"A": 1.1, "B": 1.2, "C": 1.3}

# --- PHASE B ---
raw_df = spark.read.parquet("s3://data/events/")
meta_df = spark.createDataFrame([("A", "Premium"), ("B", "Standard")], ["code", "type"])


# --- PHASE C ---
@F.udf("double")
def calculate_markup(price, code):
    multiplier = lookup_table.get(code, 1.0)
    return price * multiplier


# --- PHASE D ---
joined_df = raw_df.join(meta_df, raw_df.event_code == meta_df.code)

# --- PHASE E ---
final_df = joined_df.withColumn(
    "final_price", calculate_markup("price", "code")
).filter(F.col("type") == "Premium")

# --- PHASE F ---
report = final_df.groupBy("type").agg(F.avg("final_price")).collect()

# --- PHASE G ---
for row in report:
    print(f"Type: {row['type']}, Avg: {row['avg(final_price)']}")
