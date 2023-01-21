
Question 1:

docker build --help



Question 2:

(base) jwagg-lt1:DE-Zoomcamp-Homework j.wagg$ docker run -it python:3.9
Python 3.9.16 (main, Jan 11 2023, 15:55:30) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os 
>>> os.system("pip list")
Package    Version
---------- -------
pip        22.0.4
setuptools 58.1.0
wheel      0.38.4



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
