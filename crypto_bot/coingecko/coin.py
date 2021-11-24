import os
import requests
from .endpoints import data


class Coin(requests.Session):
    headers = {'Content-Type': 'application/json'}
    cg_url = 'https://api.coingecko.com/api/v3'
    vs_currencies = 'usd'

    def __init__(self, name, token_id, **kwargs):
        super(Coin, self).__init__(**kwargs)
        self.name = name
        self.token_id = token_id

    def api_request(self, endpoint, **kwargs):
        return self.get(data['baseUrl']+data[endpoint].format(**kwargs))

    def get_price(self):
        return self.get_price_info()[self.vs_currencies]

    def get_price_info(self):
        return self.api_request('simplePrice', ids=self.token_id, vs_currencies=self.vs_currencies).json()[self.token_id]

    def get_price_summary(self):
        result = self.get_price_info()
        return f"""
Price: ${result['usd']}
Market Cap: ${result['usd_market_cap']:,.2f}
24H Volume: ${result['usd_24h_vol']:,.2f}
24H Change: {result['usd_24h_change']:.2f}%"""
