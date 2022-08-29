
import org.apache.spark.sql.SparkSession
val spark:SparkSession = SparkSession.builder().master("local").appName("TestSpark").getOrCreate()   

val url_hive= "jdbc:hive2://51.161.115.210:10000"
val user_hive="debian"
val pw_hive="KTQhkLYfP3nV33MH"
val boxes = "prl_migrate.box_boxes"
val schema_prl_migrate = "prl_migrate"
val jdbcDF = spark.read.format("jdbc").option("url", url_hive).option("dbtable",boxes).option("user", user_hive).option("password",pw_hive).load()


