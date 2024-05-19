from dotenv import load_dotenv
load_dotenv()
from cryptography.fernet import Fernet
import sqlite3
import os
encryption_key = os.getenv('ENCRYPTION_KEY').encode()


def encrypt_data(massage):
    try:
        encoded_massage = massage.encode('utf-8')
        cipher = Fernet(encryption_key)
        encrypted_string = cipher.encrypt(encoded_massage)
        return encrypted_string
    except Exception as e:
        print(f"Encryption error: {e}")

def decrypt_data(encrypted_massage):
    try:
        cipher = Fernet(encryption_key)
        decrypted_massage = cipher.decrypt(encrypted_massage)
        return decrypted_massage.decode('utf-8')
    except Exception as e:
        print(f"Decryption error: {e}")
        
def set_up_DB():
    conn =sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users(
                       user_id INTEGER PRIMARY KEY,
                       telegram_id INTEGER NOT NULL,
                       private_key TEXT NOT NULL,
                       address TEXT NOT NULL
                   )
                   ''')
    conn.commit()
    conn.close()
    

def get_wallet_address_from_DB(telegram_user_id):
    try:
        conn =sqlite3.connect('users.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE telegram_id = {telegram_user_id} LIMIT 1;"
        cursor.execute(query)
        row = cursor.fetchone()
        if row:    
            conn.close()
            return row[3]
        cursor.close()
        return None
    except Exception as e:
        print(f'error getting user address: {e}')

def save_private_key_to_db(telegram_user_id, privatekey, address):
    try:
        encoded_privatekey = decrypt_data(privatekey)
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (telegram_id, private_key, address) VALUES (?, ?, ?)', (telegram_user_id, encoded_privatekey, address))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"error saving private key: {e}")
        