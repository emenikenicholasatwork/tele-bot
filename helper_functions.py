from dotenv import load_dotenv
load_dotenv()
from cryptography.fernet import Fernet
import sqlite3
import os
encryption_key = os.getenv('ENCRYPTION_KEY').encode()


def encrypt_data(string):
    try:
        string_bytes = string.encode()
        cipher = Fernet(encryption_key)
        encrypted_string = cipher.encrypt(string_bytes)
        print(f"Encrypted: {encrypted_string}")
        return encrypted_string
    except Exception as e:
        print(f"Encryption error: {e}")

def decrypt_data(encrypted_string):
    try:
        cipher = Fernet(encryption_key)
        decrypted_string = cipher.decrypt(encrypted_string)
        print(f"Decrypted: {decrypted_string.decode()}")
        return decrypted_string.decode()
    except Exception as e:
        print(f"Decryption error: {e}")
        
def create_db_table():
    conn =sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users(
                       user_id INTEGER PRIMARY KEY,
                       private_key TEXT NOT NULL
                   )
                   ''')
    conn.commit()
    conn.close()