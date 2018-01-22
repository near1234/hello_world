import sqlite3

database = sqlite3.connect("weine.db")
db = database.cursor()
db.execute("select * from Erzeuger natural join Weine")
print(db.fetchall())
print("Hello World")
