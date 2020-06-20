import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

# to make sure table is empty delete any previous rows
cur.execute('DELETE FROM Ages;')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Renars", 16)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Cailean", 13)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Nial", 33)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Mhyren", 17)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Sergei", 17)')

conn.commit()

conn.close()
