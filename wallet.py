
from dotenv import load_dotenv
load_dotenv()
import os
import requests
from web3 import Web3
from eth_account import Account

network_name = os.getenv('ETHEREUM_NETWORK')
network_api_key = os.getenv('ETHEREUM_NETWORK_API_KEY')

w3 = Web3(Web3.HTTPProvider(f"https://{network_name}.infura.io/v3/{network_api_key}"))

class Wallet:
    @staticmethod
    async def new_wallet():
        try:
            account = w3.eth.account.create()
            address = account.address
            private_key = account.key.hex()
            balance = w3.eth.get_balance(address)
            balance_in_eth = w3.from_wei(balance, 'ether')
            doller_price = await Wallet.get_eth_current_price()
            balance_in_dollars = doller_price * float(balance_in_eth)
            return private_key, balance_in_eth, balance_in_dollars
        except Exception as e:
            print(e)
            
    async def get_eth_current_price():
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
        data = response.json()
        price = data['ethereum']['usd']
        return price