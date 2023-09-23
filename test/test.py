import os
import sys
sys.path.append(os.path.join(os.getcwd(), os.pardir))
from src.gmo_coin_api import GMOCoinAPI

if __name__ == "__main__":
    client = GMOCoinAPI()
    res_latest_rate = client.get_latest_rate_by_http("JPY")
    print(res_latest_rate)
