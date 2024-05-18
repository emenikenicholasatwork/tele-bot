
from dotenv import load_dotenv
load_dotenv()
import os
import requests
from web3 import Web3
from eth_account import Account
import ccxt
exchange = ccxt.bybit()

network_name = os.getenv('ETHEREUM_NETWORK')
network_api_key = os.getenv('ETHEREUM_NETWORK_API_KEY')
# bybit_api_key = os.getenv('BYBIT_API_KEY')
# bybit_api_secret = os.getenv('BYBIT_API_SECRET')
# session = HTTP(api_key=bybit_api_key, api_secret=bybit_api_secret)
w3 = Web3(Web3.HTTPProvider(f"https://{network_name}.infura.io/v3/{network_api_key}"))

class Eth_Wallet:
    @staticmethod
    async def new_wallet():
        try:
            # create ethereum account
            account = w3.eth.account.create()
            address = account.address
            private_key = account.key.hex()
            balance = w3.eth.get_balance(address)
            balance_in_eth = w3.from_wei(balance, 'ether')
            dollar_price = await Eth_Wallet.get_eth_current_price()
            balance_in_dollars = dollar_price * float(balance_in_eth)
            return private_key, balance_in_eth, balance_in_dollars
        except Exception as e:
            print(e)
            
    
    async def get_asset_price():
        try:
            ticker = exchange.fetch_ticker("BTC/USDT")
            print(ticker)
            # res = await session.get_option_delivery_price(category="option", symbol=token)
            # print(ticker)
            return ticker
        except Exception as err:
            print(err)