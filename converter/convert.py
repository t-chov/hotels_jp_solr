import csv
import sys
from dataclasses import asdict, dataclass, field
from typing import Dict

import pysolr


@dataclass()
class Hotel:
    id: str
    name_ja: str
    address_ja: str
    tel: str
    url: str
    latitude: float
    longitude: float
    coordinate: str = field(init=False)

    def __post_init__(self):
        self.coordinate = f'{self.latitude},{self.longitude}'

def convert(item: Dict) -> Hotel:
    return Hotel(
        id=item['登録番号'],
        name_ja=item['施設名称'],
        address_ja=item['住所'],
        tel=item['電話番号'],
        url=item['URL'],
        latitude=float(item['緯度']),
        longitude=float(item['経度'])
    )

if __name__ == '__main__':
    input_filepath = sys.argv[1]
    with open(input_filepath) as input_file:
        reader = csv.DictReader(input_file)
        hotels = [asdict(convert(item)) for item in reader]
    solr = pysolr.Solr('http://localhost:8983/solr/hotels_mlti', always_commit=True)
    solr.delete(q="*:*")
    solr.add(hotels)
