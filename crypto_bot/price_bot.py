import asyncio
import json
import discord
from coingecko.coin import Coin
from logger import make_logger


class PriceBot(discord.Client):

    def __init__(self, name, token_id, bot_token=None, frequency=10, **kwargs):
        super(PriceBot, self).__init__(**kwargs)
        self.logger = make_logger(name)
        self.coin = Coin(name, token_id)
        self.name = name
        self.frequency = frequency
        self.price = 0
        self.ready = False
        self.run(bot_token)

    async def update_nickname(self):
        """Update bot nickname"""
        for guild in self.guilds:
            for member in guild.members:
                self.logger.info(
                    f'Updating the price to {self.price} in {guild}.')
                await member.edit(nick=f'{self.name} ${self.price}')
                self.logger.info(f'Successfully updated the price in {guild}.')

    async def update_price(self):
        """Update the price of the bot"""
        try:
            price = self.coin.get_price()
        except json.decoder.JSONDecodeError:
            self.logger.warning(
                'Coingecko failed to get price while updating.')
            await asyncio.sleep(60)
            return
        if price != self.price:
            self.price = price
            await self.update_nickname()

    async def continue_price_update(self):
        """Make sure the price updates at the frequency specified."""
        while True:
            await self.update_price()
            await asyncio.sleep(self.frequency)

    async def on_ready(self):
        self.ready = True
        await self.continue_price_update()

    async def on_message(self, message):
        if message.author == self.user:
            return
