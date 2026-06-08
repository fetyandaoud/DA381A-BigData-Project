df = spark.read.option("header", "true").option("multiLine", "true").option("escape", "\"").csv("hdfs://localhost:9000/data/steam_reviews.csv")

df.count()

df.groupBy("recommended").count().show()

df.groupBy("language").count().orderBy("count", ascending=False).show(10)

df.groupBy("app_name").count().orderBy("count", ascending=False).show(10, truncate=False)

from pyspark.sql.functions import col

df2 = df.withColumn("votes_helpful", col("votes_helpful").cast("int"))

df2 = df2.withColumn("playtime_forever_num", col("`author.playtime_forever`").cast("double"))

df2.groupBy("recommended").avg("votes_helpful").show()

df2.groupBy("recommended").avg("playtime_forever_num").show()