import discord
import time
from coingecko import CoinGecko


class PriceBot(discord.Client):

    def __init__(self, name, token_id, bot_token, **kwargs):
        super(PriceBot, self).__init__(**kwargs)
        self.cg = CoinGecko(name, token_id)
        self.name = name
        self.run(bot_token)

    async def update_price(self):
        price = self.cg.get_price()
        for guild in self.guilds:
            for member in guild.members:
                await member.edit(nick=f'{self.name} ${price}')
                print(price)

    async def continue_price_update(self):
        while True:
            time.sleep(1)
            await self.update_price()
        
    async def on_ready(self):
        #await self.continue_price_update()
        await self.update_price()

    async def on_message(self, message):
        if message.author == self.user:
            return 

