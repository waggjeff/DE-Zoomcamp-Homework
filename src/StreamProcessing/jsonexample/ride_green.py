from typing import List, Dict
from decimal import Decimal
from datetime import datetime

class Ride_green:
    def __init__(self, arr: List[str]):
        self.vendor_id = arr[0]
        self.tpep_pickup_datetime = datetime.strptime(arr[1], "%Y-%m-%d %H:%M:%S"),
        self.tpep_dropoff_datetime = datetime.strptime(arr[2], "%Y-%m-%d %H:%M:%S"),
        self.store_and_fwd_flag = arr[3]
        self.rate_code_id = arr[4]
        self.pu_location_id = arr[5]
        self.do_location_id = arr[6]
        self.passenger_count = arr[7]
        self.trip_distance = arr[8]
        self.fare_amount = arr[9]
        self.extra = arr[10]
        self.mta_tax = arr[11]
        self.tip_amount = arr[12]
        self.tolls_amount = arr[13]
        self.ehail_fee = arr[14]
        self.improvement_surcharge = arr[15]
        self.total_amount = arr[16]
        self.payment_type = arr[17]
        self.trip_type = arr[18]
        self.congestion_surcharge = arr[19]

    @classmethod
    def from_dict(cls, d: Dict):
        return cls(arr=[
            d['vendor_id'],
            d['tpep_pickup_datetime'][0],
            d['tpep_dropoff_datetime'][0],
            d['store_and_fwd_flag'],
            d['passenger_count'],
            d['trip_distance'],
            d['rate_code_id'],
            d['store_and_fwd_flag'],
            d['pu_location_id'],
            d['do_location_id'],
            d['payment_type'],
            d['fare_amount'],
            d['extra'],
            d['mta_tax'],
            d['tip_amount'],
            d['tolls_amount'],
            d['improvement_surcharge'],
            d['total_amount'],
            d['congestion_surcharge'],
            d['ehail_fee'],
            d['trip_type']
            ]
        )

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'


    
