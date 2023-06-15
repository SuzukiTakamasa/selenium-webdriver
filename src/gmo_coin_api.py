
import os
import requests
from constants import PUBLIC_API_ENDPOINT


class GMOCoinAPI():
    def __init__(self, api_key: str, secret_key: str):
        self_api_key = os.environ["GMO_COIN_API_KEY"]
        self_secret_key = os.environ["GMO_COIN_SECREET_KEY"]
    
    def get_latest_rate(symbol: str | None) ->dict:
        endpoint = PUBLIC_API_ENDPOINT+'/vi/ticker'
        if symbol:
            endpoint += f'?symbol={symbol}'

        response = requests.get(endpoint)

        if response["status"] != 0:
            return f"Error: {response}"
        
        return response

        
        