import sys
import sqlite3
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

print(datas)

with sqlite3.connect('./cggekijo.db') as conn:
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    for x in datas:
        c.execute('INSERT INTO stories (title, number) VALUES (?, ?)',
                  (x['title'], x['number'],))
        story_id = c.lastrowid
        c.executemany('INSERT INTO person_map (story_id, person_id) SELECT ?, id FROM people WHERE name = ?',
                      [(story_id, y) for y in x['people']])
    conn.commit()
