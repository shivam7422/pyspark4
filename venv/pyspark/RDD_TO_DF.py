import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark import SparkContext,SQLContext
from pyspark.sql import Row,Column,DataFrame
from pyspark.sql.types import *

sc = SparkContext('local[*]', 'pyspark tutorial')
spark=SparkSession(sc)
rdd= sc.textFile("C:\\Users\\Shiva\\IdeaProjects\\new_one\\src\\main\\resources\\sales.csv")
rdd1= rdd.first()
rdd2= rdd.filter(lambda x: x!=rdd1)
rdd3= rdd2.map(lambda x:x.split(","))
rdd4= rdd3.map(lambda x: Row(t_id=int(x[0]),c_id=int(x[1]),i_id=int(x[2]),amt_paid=float(x[3])))
#rdd4.foreach(print)

schema= StructType([
    StructField("t_id",IntegerType(),True),
    StructField("c_id",IntegerType(),True),
    StructField("i_id",IntegerType(),True),
    StructField("amt_paid",FloatType(),True)])
df1=spark.createDataFrame(rdd4,schema)
df1.printSchema
df1.show(22)