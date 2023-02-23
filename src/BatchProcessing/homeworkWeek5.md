## Week 5 Homework 

In this homework we'll put what we learned about Spark in practice.

For this homework we will be using the FHVHV 2021-06 data found here. [FHVHV Data](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhvhv/fhvhv_tripdata_2021-06.csv.gz )


### Question 1: 

**Install Spark and PySpark** 

- Install Spark
- Run PySpark
- Create a local spark session
- Execute spark.version.

What's the output?
- 3.3.2


commandline:

pyspark

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

spark.version
'3.3.2'

### Question 2: 

**HVFHW June 2021**

Read it with Spark using the same schema as we did in the lessons.</br> 
We will use this dataset for all the remaining questions.</br>
Repartition it to 12 partitions and save it to parquet.</br>
What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)? Select the answer which most closely matches.</br>


- 24MB
</br></br>

jfw - see code in 'week5_homework_jfw.ipynb'


### Question 3: 

**Count records**  

How many taxi trips were there on June 15?</br></br>
Consider only trips that started on June 15.</br>

- 452,470

jfw- from 'week5_homework_jfw.ipynb':

df.select(df.pickup_datetime) \
  .withColumn('pickup_datetime', F.to_date(df.pickup_datetime)) \
  .filter((df.pickup_datetime >= '2021-06-15') & (df.pickup_datetime < '2021-06-16')) \
  .count()

452470

### Question 4: 

**Longest trip for each day**  

Now calculate the duration for each trip.</br>
How long was the longest trip in Hours?</br>

- 66.87 Hours

jfw - from 'week5_homework_jfw.ipynb':

timeDiff = (unix_timestamp('dropoff_datetime', "yyyy-MM-dd HH:mm:ss") - unix_timestamp('pickup_datetime', "yyyy-MM-dd HH:mm:ss"))
df = df.withColumn("Duration", timeDiff)

df.select(max(df.Duration)).show()

+-------------+
|max(Duration)|
+-------------+
|       240764|
+-------------+

print(240764 / 3600.)

66.87


### Question 5: 

**User Interface**

 Spark’s User Interface which shows application's dashboard runs on which local port?</br>

- 4040



### Question 6: 

**Most frequent pickup location zone**

Load the zone lookup data into a temp view in Spark</br>
[Zone Data](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv)</br>

Using the zone lookup data and the fhvhv June 2021 data, what is the name of the most frequent pickup location zone?</br>

- Crown Heights North
</br></br>

jfw - from 'week5_homework_jfw.ipynb':

dfz = spark.read \
    .option("header", "true") \
    .csv("taxi_zone_lookup.csv")

df.groupBy('PULocationID').count().orderBy('count', ascending=False).show()

+------------+------+
|PULocationID| count|
+------------+------+
|          61            | 231279|
|          79            | 221244|
|         132           | 188867|

dfz.select(dfz.Zone).where(dfz.LocationID == '61').show()

+-------------------+
|               Zone|
+-------------------+
|Crown Heights North|
+-------------------+


## Submitting the solutions

* Form for submitting: https://forms.gle/EcSvDs6vp64gcGuD8
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 06 March (Monday), 22:00 CET


## Solution

We will publish the solution here
