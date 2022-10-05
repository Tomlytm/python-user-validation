import sqlite3

con = sqlite3.connect("clients.db")
print("Database opened successfully")

con.execute("create table Clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, address TEXT NOT NULL, phone TEXT NOT NULL, email TEXT UNIQUE NOT NULL, date TEXT NOT NULL, time TEXT NOT NULL)")

print("Table created successfully")

con.close()