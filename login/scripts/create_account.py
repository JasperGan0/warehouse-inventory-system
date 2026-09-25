import sqlite3
import getpass

from login.scripts.functions import hash_password, check_username, generate_salt_for_key

con = sqlite3.connect('users.db')
cursor = con.cursor()

def register():
    while True:
        username = input('enter username: ')
        if not check_username(username):
            break
        print('username in use already.')

    password = getpass.getpass('enter password: ')
    hashed_password = hash_password(password)
    key_salt = generate_salt_for_key()

    cursor.execute(
        "INSERT INTO USERS (username, password, key_salt) VALUES (?, ?, ?)",
        (username, hashed_password, key_salt)
    )
    con.commit()
