import yaml


data = yaml.safe_load("""
baseUrl: https://api.coingecko.com/api/v3

# Configuration
session:
  headers:
    Content-Type: application/json
  timeout: .5

# Ping
ping: /ping

# Simple
simplePrice: /simple/price?ids={ids}&vs_currencies={vs_currencies}&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true
simpleTokenPrice: /simple/token_price?ids={id}&contract_addresses={contract_addresses}&vs_currencies={vs_currencies}
simpleSupportedVsCurrencies: /simple/supported_vs_currencies

# Coins
coinsList: /coins/list
coinsMarkets: /coins/markets?vs_currency={vs_currency}
coin: /coins/{id}
coinTickers: /coins/{id}/tickers
coinHistory: /coins/{id}/history
coinmarketChart: /coins/{id}/market_chart?vs_currency={vs_currency}&days={days}&interval={interval}
coinMarketChartRange: /coins/{id}/market_chart/range?vs_currency={vs_currency}&from={from}&to={to}
coinStatusUpdates: /coins/{id}/status_updates
coinOhlc: /coins/{id}/ohlc?vs_currency={vs_currency}&days={days}
""")
