
Question 1:

docker build --help



Question 2:

docker run -it python:3.9

python>import os

python>os.system("pip list")



Question 3:

SELECT count(1) FROM green_taxi_trips WHERE lpep_pickup_datetime >= '2019-01-15 00:00:00'
       AND lpep_pickup_datetime <  '2019-01-16 00:00:00';



Question 4:

SELECT MAX(trip_distance) FROM green_taxi_trips WHERE lpep_pickup_datetime >= '2019-01-18 00:00:00'
       AND lpep_pickup_datetime <  '2019-01-19 00:00:00';

2019-01-18: 80.96

SELECT MAX(trip_distance) FROM green_taxi_trips WHERE lpep_pickup_datetime >= '2019-01-28 00:00:00'
       AND lpep_pickup_datetime <  '2019-01-29 00:00:00';

2019-01-28: 64.27

SELECT MAX(trip_distance) FROM green_taxi_trips WHERE lpep_pickup_datetime >= '2019-01-15 00:00:00'
       AND lpep_pickup_datetime <  '2019-01-16 00:00:00';

2019-01-15: 117.99

SELECT MAX(trip_distance) FROM green_taxi_trips WHERE lpep_pickup_datetime >= '2019-01-10 00:00:00'
       AND lpep_pickup_datetime <  '2019-01-11 00:00:00';

2019-01-10: 64.2

Question 5:

SELECT count(1) FROM green_taxi_trips WHERE lpep_pickup_datetime >= '2019-01-01 00:00:00'
       AND lpep_pickup_datetime <  '2019-01-02 00:00:00' and passenger_count=2;

SELECT count(1) FROM green_taxi_trips WHERE lpep_pickup_datetime >= '2019-01-01 00:00:00'
       AND lpep_pickup_datetime <  '2019-01-02 00:00:00' and passenger_count=3;


2: 1282  3: 254


Question 6:

SELECT "LocationID", "Zone" FROM Zones;

This shows that 'Astoria' is LocationID 7

SELECT MAX(tip_amount) FROM green_taxi_trips WHERE "PULocationID"= 7;

This shows that the largest tip was 88 USD

SELECT "DOLocationID", tip_amount FROM green_taxi_trips WHERE "PULocationID"= 7 and tip_amount=88.0;

The dropoff location ID was 146.

SELECT "Zone" from zones where "LocationID"=146;

Long Island City/Queens Plaza


Part 1-b

(base) jwagg-lt1:Terraform j.wagg$ terraform apply
var.project
  mythic-byway-375404

  Enter a value: mythic-byway-375404

google_storage_bucket.data-lake-bucket: Refreshing state... [id=dtc_data_lake_mythic-byway-375404]
google_bigquery_dataset.dataset: Refreshing state... [id=projects/mythic-byway-375404/datasets/trips_data_all]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be updated in-place
  ~ resource "google_bigquery_dataset" "dataset" {
      - default_partition_expiration_ms = 5184000000 -> null
      - default_table_expiration_ms     = 5184000000 -> null
        id                              = "projects/mythic-byway-375404/datasets/trips_data_all"
        # (9 unchanged attributes hidden)

        # (4 unchanged blocks hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.dataset: Modifying... [id=projects/mythic-byway-375404/datasets/trips_data_all]
google_bigquery_dataset.dataset: Modifications complete after 3s [id=projects/mythic-byway-375404/datasets/trips_data_all]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
