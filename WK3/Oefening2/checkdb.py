import sqlite3
import pytz

db = sqlite3.connect("contacts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
cursor = db.cursor()
newname = input("Please enter your name!")

for row in cursor.execute("SELECT * FROM Contacts WHERE name = {name}".format(name = "'" + newname + "'")):
    print(row)

db.close()

