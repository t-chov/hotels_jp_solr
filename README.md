# hotels_jp_solr

Search hotels in Japan with MLIT open data.

## Requirements

- nkf
- docker

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