### This directory contains code and homework solutions for week 6 of the Data Engineering zoomcamp. 

One needs to follow these steps to start the streaming process required for the homework. 

### 1. Build Required Images for running Spark

Change to the spark directory. 

The details of how to spark-images are build in different layers can be created can be read through 
the blog post written by André Perez on [Medium blog -Towards Data Science](https://towardsdatascience.com/apache-spark-cluster-on-docker-ft-a-juyterlab-interface-418383c95445)

```bash
# Build Spark Images
./build.sh 
```

### 2. Create Docker Network & Volume

```bash
# Create Network
docker network  create kafka-spark-network

# Create Volume
docker volume create --name=hadoop-distributed-file-system
```

### 3. Run Services on Docker
```bash
# Start Docker-Compose (within both the kafka and spark folders)
docker compose up -d
```
In depth explanation of [Kafka Listeners](https://www.confluent.io/blog/kafka-listeners-explained/)

Explanation of [Kafka Listeners](https://www.confluent.io/blog/kafka-listeners-explained/)

### 4. Start the kafka Producer and consumer

In the 'kafka' director, run:

```bash
python3 producer_multiple.py
```

This file has been modified to process both the [fhv_tripdata_2019-01.csv.gz](https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv) 
and [green_tripdata_2019-01.csv.gz](https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green) datasets. 

Also in the kafka directory, start the consumer which has been modified to read the 'rides_green' and 'rides_fhv' topics sent by the producer. 

```bash
python3 consumer_multiple.py
```


### 5. Stop Services on Docker
```bash
# Stop Docker-Compose (within for kafka and spark folders)
docker compose down
```

### 6. Helpful Comands
```bash
# Delete all Containers
docker rm -f $(docker ps -a -q)

# Delete all volumes
docker volume rm $(docker volume ls -q)
```
