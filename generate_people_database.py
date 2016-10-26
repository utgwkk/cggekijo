import sys
import sqlite3

with sqlite3.connect('./cggekijo.db') as conn:
    c = conn.cursor()
    for line in sys.stdin:
        line = line.rstrip()
        name, kana = line.split(' ')
        print(name, kana)
        c.execute('INSERT INTO people (name, kana) VALUES (?, ?)',
                  (name, kana,))
    conn.commit()
