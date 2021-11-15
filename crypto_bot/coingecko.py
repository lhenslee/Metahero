import requests


class CoinGecko(requests.Session):
    headers = {'Content-Type': 'application/json'}
    cg_url = 'https://api.coingecko.com/api/v3'

    def __init__(self, name, token_id, **kwargs):
        super(CoinGecko, self).__init__(**kwargs)
        self.name = name
        self.token_id = token_id

    def get_price_summary(self):
        result = self.get_price_info()
        return f"""
Price: ${result['usd']}
Market Cap: ${result['usd_market_cap']:,.2f}
24H Volume: ${result['usd_24h_vol']:,.2f}
24H Change: {result['usd_24h_change']:.2f}%"""

    def get_price_info(self):
        return self.get(f'{self.cg_url}/simple/price/?ids={self.token_id}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true').json()[self.token_id]

    def get_price(self):
        return self.get_price_info()['usd']
    