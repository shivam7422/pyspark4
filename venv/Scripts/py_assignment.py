import findspark
findspark.init()

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import row_number
from pyspark.sql.window import *

spark=SparkSession.builder.appName("app").master("local").getOrCreate()
a= spark.read.option("inferschema","true").option("header","true").csv("C:\\Users\\Shiva\\IdeaProjects\\new_one\\src\\main\\resources\\sales1.csv")
a.printSchema()
a.show()
b=a.withColumn('sales1', F.regexp_replace(('sales'), "\\$","")).withColumn("Load_time",F.current_timestamp())\
    .withColumn("row_number",F.row_number().over(Window.partitionBy().orderBy("id")))
b.show()
c=b.createOrReplaceTempView("axis")
d= spark.sql("select sum(sales1) as Total_sales ,country from axis group by country")
d.show()