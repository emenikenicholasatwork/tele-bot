
from dotenv import load_dotenv
load_dotenv()
import os
import requests
from web3 import Web3
from helper_functions import save_private_key_to_db, get_wallet_address_from_DB
from eth_account import Account
import ccxt
exchange = ccxt.bybit()

network_name = os.getenv('ETHEREUM_NETWORK')
network_api_key = os.getenv('ETHEREUM_NETWORK_API_KEY')
# bybit_api_key = os.getenv('BYBIT_API_KEY')
# bybit_api_secret = os.getenv('BYBIT_API_SECRET')
# session = HTTP(api_key=bybit_api_key, api_secret=bybit_api_secret)
w3 = Web3(Web3.HTTPProvider(f"https://{network_name}.infura.io/v3/{network_api_key}"))

def create_new_account(telegram_user_id):
    try:
        address = get_wallet_address_from_DB(telegram_user_id)
        if address == None:
            account = w3.eth.account.create()
            address = account.address
            privatekey = account.key.hex()
            save_private_key_to_db(telegram_user_id, privatekey, address)
            return address
        return address
            
    except Exception as e:
        print(e)
            
    
def get_token_price(token):
    try:
        ticker = exchange.fetch_ticker(token)
        print(ticker)
        return ticker
    except Exception as err:
        return None
        