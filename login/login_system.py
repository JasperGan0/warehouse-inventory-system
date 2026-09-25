import sqlite3
from login.scripts.login import login
from login.scripts.create_account import register

con = sqlite3.connect('databases/users.db')
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS USERS
                  (user_id INTEGER PRIMARY KEY,
                   username TEXT NOT NULL,
                   password TEXT NOT NULL,
                   key_salt BLOB NOT NULL)
               """)
con.commit()

login()
