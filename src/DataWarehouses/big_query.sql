-- Query public available table (07/02/2023 - JW: updated for my project codes and homework)
SELECT station_id, name FROM
    bigquery-public-data.new_york_citibike.citibike_stations
LIMIT 100;


-- Creating external table referring to gcs path
-- CREATE OR REPLACE EXTERNAL TABLE `taxi-rides-ny.nytaxi.external_yellow_tripdata`
CREATE OR REPLACE EXTERNAL TABLE `mythic-byway-375404.nytaxi.fhv2019`
OPTIONS (
  format = 'CSV',
  uris = ['gs://jwagg-fhv/fhv_tripdata_*.csv.gz']
);


-- Check trip data to make sure it looks ok 
SELECT * FROM nytaxi2019.fhv limit 10;

-- Find the number of trips in 2019 
SELECT COUNT(0) FROM nytaxi.fhv2019 WHERE DATE(pickup_datetime) BETWEEN '2019-01-01' and '2019-12-31';

-- returned 43244696

-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE nytaxi.fhv2019_non_partitoned AS
SELECT * FROM nytaxi.fhv2019;


-- Creating a partition and cluster table  (Quetion 5)
CREATE OR REPLACE TABLE nytaxi.fhv2019_partitoned_clustered
PARTITION BY DATE(pickup_datetime)
CLUSTER BY affiliated_base_number AS 
SELECT * FROM nytaxi.fhv2019;








-- Create a partitioned table from external table
CREATE OR REPLACE TABLE nytaxi.fhv2019_partitoned
PARTITION BY
  DATE(pickup_datetime) AS
SELECT * FROM nytaxi.fhv;

-- Impact of partition
-- Scanning 1.6GB of data
SELECT DISTINCT(VendorID)
FROM taxi-rides-ny.nytaxi.yellow_tripdata_non_partitoned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2019-06-30';

-- Scanning ~106 MB of DATA
SELECT DISTINCT(VendorID)
FROM taxi-rides-ny.nytaxi.yellow_tripdata_partitoned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2019-06-30';

-- Let's look into the partitons
SELECT table_name, partition_id, total_rows
FROM `nytaxi.INFORMATION_SCHEMA.PARTITIONS`
WHERE table_name = 'yellow_tripdata_partitoned'
ORDER BY total_rows DESC;

-- Creating a partition and cluster table
CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_partitoned_clustered
PARTITION BY DATE(tpep_pickup_datetime)
CLUSTER BY VendorID AS
SELECT * FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;

-- Query scans 1.1 GB
SELECT count(*) as trips
FROM taxi-rides-ny.nytaxi.yellow_tripdata_partitoned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
  AND VendorID=1;

-- Query scans 864.5 MB
SELECT count(*) as trips
FROM taxi-rides-ny.nytaxi.yellow_tripdata_partitoned_clustered
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
  AND VendorID=1;
