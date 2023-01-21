
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
