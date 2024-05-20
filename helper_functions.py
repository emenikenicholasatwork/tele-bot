from dotenv import load_dotenv
load_dotenv()
from cryptography.fernet import Fernet
import sqlite3
import os
encryption_key = os.getenv('ENCRYPTION_KEY').encode()


def encrypt_data(massage):
    try:
        cipher = Fernet(encryption_key)
        encrypted_string = cipher.encrypt(massage.encode('utf-8'))
        return encrypted_string
    except Exception as e:
        print(f"Encryption error: {e}")

def decrypt_data(encrypted_massage):
    try:
        cipher = Fernet(encryption_key)
        decrypted_massage = cipher.decrypt(encrypted_massage).decode('utf-8')
        print(decrypted_massage)
        return decrypted_massage
    except Exception as e:
        print(f"Decryption error: {e}")
        
def set_up_DB():
    conn =sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users(
                       user_id INTEGER PRIMARY KEY,
                       telegram_id INTEGER NOT NULL,
                       private_key BLOB NOT NULL,
                       address TEXT NOT NULL
                   )
                   ''')
    conn.commit()
    conn.close()
    
def get_private_key_from_DB(telegram_user_id):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE telegram_id = {telegram_user_id} LIMIT 1;"
        cursor.execute(query)
        row = cursor.fetchone()
        conn.close()
        if row:
            return decrypt_data(row[2])
        return None
    except Exception as e:
        print(f'Error while getting private key :{e}')
    

def get_wallet_address_from_DB(telegram_user_id):
    try:
        conn =sqlite3.connect('users.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE telegram_id = {telegram_user_id} LIMIT 1;"
        cursor.execute(query)
        row = cursor.fetchone()
        conn.close()
        if row:    
            return row[3]
        return None
    except Exception as e:
        print(f'error getting user address: {e}')

def save_private_key_to_db(telegram_user_id, privatekey, address):
    try:
        encrypted_privatekey = encrypt_data(privatekey)
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (telegram_id, private_key, address) VALUES (?, ?, ?)', (telegram_user_id, encrypted_privatekey, address))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"error saving private key: {e}")
        
        
