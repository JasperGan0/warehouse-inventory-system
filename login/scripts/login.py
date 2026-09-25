import sqlite3
import getpass

from login.scripts.functions import verify_password

con = sqlite3.connect('users.db')
cursor = con.cursor()

def login():
    while True:
        username = input('enter username: ')
        cursor.execute(
            "SELECT password FROM USERS WHERE username = ?",
            (username,)
        )
        result = cursor.fetchone()

        if result is not None:
            break
        print('username not found')

    while True:
        password = getpass.getpass('enter password: ')

        if verify_password(result[0], password):
            print('login successful')
            break
        else:
            print('incorrect password')
