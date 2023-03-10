import csv
import json
from typing import List, Dict
from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError

from ride_green import Ride_green
from ride_fhv import Ride_fhv
from settings_multiple import BOOTSTRAP_SERVERS, INPUT_DATA_PATH, KAFKA_TOPIC


class JsonProducer(KafkaProducer):
    def __init__(self, props: Dict):
        self.producer = KafkaProducer(**props)

    @staticmethod
    def read_records(resource_path: str, taxitype='green'):
        records = []
        if taxitype == 'green':
            with open(resource_path, 'r') as f:
                reader = csv.reader(f)
                header = next(reader)  # skip the header row
                for row in reader:
                    records.append(Ride_green(arr=row))
            return records
        if taxitype == 'fhv':
            with open(resource_path, 'r') as f:
                reader = csv.reader(f)
                header = next(reader)  # skip the header row
                for row in reader:
                    records.append(Ride_fhv(arr=row))
            return records

    def publish_rides_green(self, topic: str, messages: List[Ride_green]):
        for ride in messages:
            try:
                record = self.producer.send(topic=topic, key=ride.pu_location_id, value=ride)
                print('Record {} successfully produced at offset {}'.format(ride.pu_location_id, record.get().offset))
            except KafkaTimeoutError as e:
                print(e.__str__())

    def publish_rides_fhv(self, topic: str, messages: List[Ride_fhv]):
        for ride in messages:
            try:
                record = self.producer.send(topic=topic, key=ride.pu_location_id, value=ride)
                print('Record {} successfully produced at offset {}'.format(ride.pu_location_id, record.get().offset))
            except KafkaTimeoutError as e:
                print(e.__str__())


if __name__ == '__main__':
    # Config Should match with the KafkaProducer expectation
    config = {
        'bootstrap_servers': BOOTSTRAP_SERVERS,
        'key_serializer': lambda key: str(key).encode(),
        'value_serializer': lambda x: json.dumps(x.__dict__, default=str).encode('utf-8')
    }

    # stream green data 
    producer = JsonProducer(props=config)
    rides = producer.read_records(resource_path=INPUT_DATA_PATH[0])
    producer.publish_rides_green(topic=KAFKA_TOPIC[0], messages=rides)

    # stream fhv data
    producer = JsonProducer(props=config)
    rides = producer.read_records(resource_path=INPUT_DATA_PATH[1])
    producer.publish_rides_fhv(topic=KAFKA_TOPIC[1], messages=rides)
