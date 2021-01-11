# hotels_jp_solr

Search hotels in Japan with MLIT open data.

## Requirements

- nkf
- docker
- python3.7

## How to use

1. Download CSV from [MLIT website](https://www.hokoukukan.go.jp/metadata/detail/30)
    - **YOU MUST DOWNLOAD ONLY HOTELS**
    - 旅館(ryokan) data has different columns. why... 😞
2. Unzip downloaded file.
3. Convert encode Shift-JIS to utf-8
    - `sed -e 1d 30/**.csv | nkf -w > hotels.csv`
        - it may have only `30/80/hotel_ichiran201812.csv`
4. Start solr with Docker
    - `docker run --rm -p 8983:8983 -v "${PWD}/hotels_mlti:/var/solr/data/hotels_mlti" solr:8.7.0 solr-fg`
5. Use `convert.py`

```bash
# Example of indexing
$ cd converter
$ python3 -m venv .venv/
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ python3 convert.py ${PATH_OF_HOTELS}
```

## Example

- Search hotels nearby Shin-Yokohama station.
    - http://localhost:8983/solr/hotels_mlti/select?d=50.0&fl=*%2Cgeodist()&fq=%7B!geofilt%7D&pt=35.5087%2C139.6133&q=*%3A*&sfield=coordinate&sort=geodist()%20asc