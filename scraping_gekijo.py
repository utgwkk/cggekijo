import sys
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

# http://cggekijo.blog.fc2.com/

datas = []

for url in sys.stdin:
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    splitted = soup.find('h2').a.text.split(' ', 2)
    try:
        number = int(splitted[1].replace('第', '').replace('話', ''))
    except ValueError:
        continue
    title = splitted[2]
    print(number, title, file=sys.stderr)

    people = []
    for tag in soup.select('.tag_list')[0].find_all('a'):
        people.append(tag.text)
    print(people, file=sys.stderr)
    datas.append({'title': title, 'people': people, 'number': number})

print(json.dumps(datas))
