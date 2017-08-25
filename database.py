import sqlite3

db = sqlite3.connect('database.db')
db.execute('Create table user (ID, desiredPassword, confirmedPassword)')
