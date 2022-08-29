import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
appName= "Hive Pyspark"
url_hive= "jdbc:hive2://51.161.115.210:10000"
user_hive="debian"
pw_hive="KTQhkLYfP3nV33MH"
boxes = "prl_migrate.box_boxes"
schema_prl_migrate = "prl_migrate"

spark = SparkSession.builder.appName(appName).enableHiveSupport().getOrCreate()

jdbcDF = spark.read \
    .format("jdbc") \
    .option("url", url_hive) \
    .option("dbtable", boxes) \
    .option("user", user_hive) \
    .option("password", pw_hive) \
    .load()
jdbcDF.createOrReplaceTempView("boxes")
SparkSession.sql("select * from std")
# boxesDf = jdbcDF.select("*")

# boxesDf.show()


