#from pyspark import SparkConf,SparkContext
import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql import *

spark=SparkSession.builder.appName("app").master("local").getOrCreate()
ss= spark.read.option("inferschema","true").option("header","true").csv("C:\\Users\\Shiva\\IdeaProjects\\new_one\\src\\main\\resources\\sales1.csv")
ss.printSchema()
ss.show()
se= ss.select()