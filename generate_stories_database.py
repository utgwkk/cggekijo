import sys
import json
import sqlite3

data = json.load(open('cggekijo.json'))
data.sort(key=lambda x: x['number'])

with sqlite3.connect('./cggekijo.db') as conn:
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    for i, story in enumerate(data):
        print(story['number'], story['title'])
        c.execute('INSERT INTO stories (number, title) VALUES (?, ?)', (story['number'], story['title'], ))
        for person in story['people']:
            person_data =  c.execute('SELECT id, name FROM people WHERE name = ?', (person,)).fetchone()
            c.execute('INSERT INTO person_map (person_id, story_id) VALUES (?, ?)',
                      (person_data['id'], i + 1))
    conn.commit()
