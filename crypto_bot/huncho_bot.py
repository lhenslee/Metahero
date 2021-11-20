import discord
import requests
from tokens import huncho_token

client = discord.Client()
session = requests.Session()
session.headers = {'Content-Type': 'application/json'}
cg = 'https://api.coingecko.com/api/v3'
hero = 'metahero'
bnb = 'binancecoin'
blok = 'bloktopia'
sol = 'solana'

def get_price_summary(id):
    result = session.get(f'{cg}/simple/price/?ids={id}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true').json()[id]
    return f"""
Price: ${result['usd']}
Market Cap: ${result['usd_market_cap']:,.2f}
24H Volume: ${result['usd_24h_vol']:,.2f}
24H Change: {result['usd_24h_change']:.2f}%"""

@client.event
async def on_ready():
    print(f'You have logged in as {client}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('hero'):
        await message.channel.send(get_price_summary(hero))

    if message.content.startswith('bnb'):
        await message.channel.send(get_price_summary(bnb))

    if message.content.startswith('blok'):
        await message.channel.send(get_price_summary(blok))

    if message.content.startswith('sol'):
        await message.channel.send(get_price_summary(sol))

    if message.content.startswith('squid'):
        await message.channel.send(get_price_summary('squid'))


client.run(huncho_token)