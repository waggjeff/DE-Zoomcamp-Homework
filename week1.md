
Question 3:
SELECT count(1) FROM green_taxi_trips WHERE lpep_pickup_datetime >= '2019-01-15 00:00:00'
       AND lpep_pickup_datetime <  '2019-01-16 00:00:00';



Question 4:
SELECT MAX(trip_distance) FROM green_taxi_trips WHERE lpep_pickup_datetime >= '2019-01-18 00:00:00'
       AND lpep_pickup_datetime <  '2019-01-19 00:00:00';

2019-01-18: 80.96
2019-01-28: 64.27
2019-01-15: 117.99
2019-01-10: 64.2

Question 5:
SELECT count(1) FROM green_taxi_trips WHERE lpep_pickup_datetime >= '2019-01-01 00:00:00'
       AND lpep_pickup_datetime <  '2019-01-02 00:00:00' and passenger_count=2;

2: 1282  3: 254

Question 6:
