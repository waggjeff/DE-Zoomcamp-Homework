## Week 3 Homework
<b><u>Important Note:</b></u> <p>You can load the data however you would like, but keep the files in .GZ Format. 
If you are using orchestration such as Airflow or Prefect do not load the data into Big Query using the orchestrator.</br> 
Stop with loading the files into a bucket. </br></br>
<u>NOTE:</u> You can use the CSV option for the GZ files when creating an External Table</br>

<b>SETUP:</b></br>
Create an external table using the fhv 2019 data. </br>
Create a table in BQ using the fhv 2019 data (do not partition or cluster this table). </br>
Data can be found here: https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv </p>

JW - Uploaded the *csv.gz files to GCP Bucket called 'jwagg-fhv'

In BigQuery:
-- CREATE OR REPLACE EXTERNAL TABLE `taxi-rides-ny.nytaxi.external_yellow_tripdata`
CREATE OR REPLACE EXTERNAL TABLE `mythic-byway-375404.nytaxi.fhv2019`
OPTIONS (
  format = 'CSV',
  uris = ['gs://jwagg-fhv/fhv_tripdata_*.csv.gz']
);

-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE nytaxi.fhv2019_non_partitoned AS
SELECT * FROM nytaxi.fhv2019;

## Question 1:
What is the count for fhv vehicle records for year 2019?

- 43,244,696

SELECT COUNT(0) FROM nytaxi.fhv2019;


## Question 2:
Write a query to count the distinct number of affiliated_base_number for the entire dataset on both the tables.</br> 
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

- 0 MB for the External Table and 0MB for the BQ Table

SELECT COUNT(DISTINCT Affiliated_base_number) AS ALIAS1 FROM `mythic-byway-375404.nytaxi.fhv2019`;
-- returns 3165  (~0 bytes billed)

SELECT COUNT(DISTINCT Affiliated_base_number) AS ALIAS1 FROM `mythic-byway-375404.nytaxi.fhv2019_non_partitoned`;
-- returns 3165 (0 bytes billed)


## Question 3:
How many records have both a blank (null) PUlocationID and DOlocationID in the entire dataset?
- 717,748

SELECT COUNT(0) AS ALIAS1 FROM `mythic-byway-375404.nytaxi.fhv2019_non_partitoned`
	WHERE (PUlocationID IS NULL AND DOlocationID IS NULL);


## Question 4:
What is the best strategy to optimize the table if query always filter by pickup_datetime and order by affiliated_base_number?

- Partition by pickup_datetime Cluster on affiliated_base_number


## Question 5:
Implement the optimized solution you chose for question 4. Write a query to retrieve the distinct affiliated_base_number between pickup_datetime 03/01/2019 and 03/31/2019 (inclusive).</br> 
Use the BQ table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values? Choose the answer which most closely matches.

- 582.63 MB for non-partitioned table and 0 MB for the partitioned table

-- Creating a partition and cluster table  (Quetion 5)
CREATE OR REPLACE TABLE nytaxi.fhv2019_partitoned_clustered
PARTITION BY DATE(pickup_datetime)
CLUSTER BY affiliated_base_number AS 
SELECT * FROM nytaxi.fhv2019;


## Question 6: 
Where is the data stored in the External Table you created?

- GCP Bucket

## Question 7:
It is best practice in Big Query to always cluster your data:

- False


## (Not required) Question 8:
A better format to store these files may be parquet. Create a data pipeline to download the gzip files and convert them into parquet. Upload the files to your GCP Bucket and create an External and BQ Table. 


Note: Column types for all files used in an External Table must have the same datatype. While an External Table may be created and shown in the side panel in Big Query, this will need to be validated by running a count query on the External Table to check if any errors occur. 
 
## Submitting the solutions

* Form for submitting: https://forms.gle/rLdvQW2igsAT73HTA
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 13 February (Monday), 22:00 CET


## Solution

We will publish the solution here
