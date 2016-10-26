import json
import sqlite3

datas = []

with sqlite3.connect('./cggekijo.db') as conn:
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    for story in c.execute('SELECT * FROM stories').fetchall():
        data = {'title': story['title'], 'number': story['number'], 'people': []}
        for person in c.execute('SELECT * FROM people WHERE id IN (SELECT person_id FROM person_map WHERE story_id = ?)', (story['id'],)).fetchall():
            data['people'].append(person['name'])
        datas.append(data)

datas.reverse()

print(json.dumps(datas, sort_keys=True, indent=2))
