from typing import List, Dict
from decimal import Decimal
from datetime import datetime

class Ride_fhv:
    def __init__(self, arr: List[str]):
        self.dispatching_base_num = arr[0]
        self.pickup_datetime = datetime.strptime(arr[1], "%Y-%m-%d %H:%M:%S"),
        self.dropoff_datetime = datetime.strptime(arr[2], "%Y-%m-%d %H:%M:%S"),
        self.pu_location_id = arr[3]
        self.do_location_id = arr[4]
        self.SR_Flag = arr[5]
        self.Affiliated_base_number = arr[6]
        
    

    @classmethod
    def from_dict(cls, d: Dict):
        return cls(arr=[
            d['dispatching_base_num'],
            d['pickup_datetime'][0],
            d['dropoff_datetime'][0],
            d['pu_location_id'],
            d['do_location_id'],
            d['SR_Flag'],
            d['Affiliated_base_number']
        ]
        )

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'
