import sqlite3, sys, time, os
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from argon2.low_level import hash_secret_raw, Type

hasher = PasswordHasher()

current_input_buffer = ""

def hash_password(password):
    return hasher.hash(password)

def verify_password(stored_hash, password):
    try:
        return hasher.verify(stored_hash, password)
    except VerifyMismatchError:
        return False

def check_username(username):
    with sqlite3.connect('users.db') as con:
        cursor = con.cursor()
        cursor.execute(
            "SELECT password FROM USERS WHERE username = ?",
            (username,)
        )
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return True

def check_message():
    with sqlite3.connect('messages.db') as con:
        cursor = con.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS CHAT
                          (chat_id INTEGER PRIMARY KEY,
                           username1 TEXT NOT NULL,
                           username2 TEXT NOT NULL)
                       """)
        con.commit()

def generate_salt_for_key():
    salt = os.urandom(16)
    return salt

def derive_key(password, key_salt):
    return hash_secret_raw(
        secret=password.encode(),
        salt=key_salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=4,
        hash_len=32,   # 256-bit key
        type=Type.ID
    )
