#from pyspark import SparkConf,SparkContext
import findspark
findspark.init()

from pyspark.sql import SparkSession,functions as F
from pyspark.sql import *
from pyspark.sql.types import IntegerType
from pyspark.sql.column import Column # This is used for using any opertion which is going to happen on column

spark=SparkSession.builder.appName("app").master("local").getOrCreate()
ss= spark.read.option("inferschema","true").option("header","true").csv("C:\\Users\\Shiva\\IdeaProjects\\new_one\\src\\main\\resources\\sales1.csv")
ss.printSchema()
ss.show(2)
ss.cache()
#se= ss.select("id","first_name","last_name","sales").where("id=1").show()
#sa= ss.filter("sales>'$0.87'").show(1)
#sb=ss.selectExpr("*","current_date as date").show(2)
sc= ss.groupBy("country").max("id").select(F.col("max(id)").alias("max_id"),"country").show(2)
# with group by we can use the below parameters- agg
# avg,count,max, mean, min,pivot, sum