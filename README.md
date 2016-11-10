# cggekijo

## Requiements
* Python 3.4 or later
* Libraries in `requirements.txt`

## Automatically fetch information

```sh
pip insatll -r requirements.txt

python fetch_urls.py > /tmp/urls.txt
python scraping_and_insert.py < /tmp/urls.txt
python generate_json.py | jq . > cggekijo.json
```
