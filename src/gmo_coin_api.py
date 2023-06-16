
import os
import requests
import hmac
import hashlib
import time
import json

from datetime import datetime
from requests import Response

from constants import (
    PUBLIC_API_ENDPOINT_HTTP,
    PRIVATE_API_ENDPOINT_HTTP
)


class GMOCoinAPI():
    def __init__(self):
        self.api_key: str = os.environ["GMO_COIN_API_KEY"]
        self.secret_key: str = os.environ["GMO_COIN_SECREET_KEY"]
    
    def _report_error(response: Response):
        if response["status"] != 0:
            return f'Error: {response}'
    
    def _order(self, symbol: str, side: str, exec_type: str, price: str | None, size: str) -> Response:
        path: str = '/v1/order'
        endpoint: str = PRIVATE_API_ENDPOINT_HTTP + path

        req_body: dict = {
            "symbol": symbol,
            "side": side,
            "executionType": exec_type,
            "size": size
        }

        if price:
            req_body |= {"price": price}
        
        timestamp: str = f'{int(time.mktime(datetime.now().timetuple()))}000'
        text: str = timestamp + 'POST' + path + json.dumps(req_body)
        sign: str = hmac.new(bytes(self.secret_key.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()

        headers: dict = {
            "API-KEY": self.api_key,
            "API-TIMESTAMP": timestamp,
            "API-SIGN": sign
        }

        response: Response = requests.post(endpoint, headers=headers, data=json.dumps(req_body))

        self._report_error(response)

        return response
    
    def get_latest_rate_by_http(self, symbol: str | None) -> Response:
        endpoint: str = PUBLIC_API_ENDPOINT_HTTP + '/vi/ticker'
        if symbol:
            endpoint += f'?symbol={symbol}'

        response: Response = requests.get(endpoint)

        self._report_error(response)
        
        return response
    
    def buy_order(self, symbol: str, exec_type: str, price: str | None, size: str):
        self._order(symbol=symbol, side='BUY', exec_type=exec_type, price=price, size=size)
    
    def sell_order(self, symbol: str, exec_type: str, price: str | None, size: str):
        self._order(symbol=symbol, side='SELL', exec_type=exec_type, price=price, size=size)



        
        