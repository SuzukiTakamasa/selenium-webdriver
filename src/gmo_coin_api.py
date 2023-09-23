
import os
import requests
import hmac
import hashlib
import time
import json

from datetime import datetime
from requests import Response

from dotenv import load_dotenv

from src.constants import (
    PUBLIC_API_ENDPOINT_HTTP,
    PRIVATE_API_ENDPOINT_HTTP
)


class GMOCoinAPI():
    def __init__(self):
        load_dotenv()
        self.api_key: str = os.environ["GMO_COIN_API_KEY"]
        self.secret_key: str = os.environ["GMO_COIN_SECRET_KEY"]
    
    def _request(self, method: str, **kwargs) -> Response | str:
        """
        @**kwargs:
        -  url: str
        -  headers: dict
        -  body: dict
        """
        if method == "GET":
            response: Response = requests.get(**kwargs)
        elif method == "POST":
            response: Response = requests.post(**kwargs)
        else:
            return "Invalid method"
        return response
    
    def _order(self, symbol: str, side: str, exec_type: str, price: str | None, size: str) -> Response:
        path: str = '/v1/order'
        url: str = PRIVATE_API_ENDPOINT_HTTP + path

        body: dict = {
            "symbol": symbol,
            "side": side,
            "executionType": exec_type,
            "size": size
        }

        if price:
            body |= {"price": price}
        
        timestamp: str = f'{int(time.mktime(datetime.now().timetuple()))}000'
        text: str = timestamp + 'POST' + path + json.dumps(body)
        sign: str = hmac.new(bytes(self.secret_key.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()

        headers: dict = {
            "API-KEY": self.api_key,
            "API-TIMESTAMP": timestamp,
            "API-SIGN": sign
        }

        response: Response = self._request(method="POST", url=url, headers=headers, body=body)
        return response
    
    def get_latest_rate_by_http(self, symbol: str | None) -> Response:
        url: str = PUBLIC_API_ENDPOINT_HTTP + '/vi/ticker'
        if symbol:
            url += f'?symbol={symbol}'

        response = self._request(method="GET", url=url)
        
        return response
    
    def buy_order(self, symbol: str, exec_type: str, price: str | None, size: str) -> Response:
        response: Response = self._order(symbol=symbol, side='BUY', exec_type=exec_type, price=price, size=size)
        return response
    
    def sell_order(self, symbol: str, exec_type: str, price: str | None, size: str) -> Response:
        response: Response = self._order(symbol=symbol, side='SELL', exec_type=exec_type, price=price, size=size)
        return response



        
        