import asyncio
import json
import discord
from coingecko import CoinGecko
from logger import make_logger


class PriceBot(discord.Client):

    def __init__(self, name, token_id, bot_token, **kwargs):
        super(PriceBot, self).__init__(**kwargs)
        self.logger = make_logger(name)
        self.cg = CoinGecko(name, token_id)
        self.name = name
        self.run(bot_token)

    async def update_price(self, price):
        """Update the price to the bot nickname."""
        for guild in self.guilds:
            for member in guild.members:
                self.logger.info(f'Updating the price to {price}.')
                await member.edit(nick=f'{self.name} ${price}')
                self.logger.info('Successfully updated the price.')
    
    async def continue_price_update(self):
        """Make sure the price updates atleast every second."""
        last_price = None
        while True:
            try:
                self.logger.info('Trying to get the price.')
                price = self.cg.get_price()
            except json.decoder.JSONDecodeError:
                self.logger.warning('Coingecko failed to get price while updating.')
                await asyncio.sleep(60)
                continue
            if price != last_price:
                last_price = price
                await self.update_price(price)
            await asyncio.sleep(1)
        
    async def on_ready(self):
        await self.continue_price_update()

    async def on_message(self, message):
        if message.author == self.user:
            return 

