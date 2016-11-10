import time
import pickle
import feedparser

RSS_URL = 'http://cggekijo.blog.fc2.com/?xml'

try:
    offset_time = pickle.load(open('./.last-modified', 'rb'))
except FileNotFoundError:
    offset_time = time.gmtime(1)

data = feedparser.parse(RSS_URL)

for entry in data['entries']:
    if entry['updated_parsed'] > offset_time and 'まとめ' not in entry['tags'][0]['term']:
        print(entry['id'])

pickle.dump(time.gmtime(), open('./.last-modified', 'wb'))
