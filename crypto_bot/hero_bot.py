from price_bot import PriceBot


BOT_TOKEN = 'OTA5NjgyMDIwMzEyMDU1ODM4.YZH1Zg.GljY27N1YXNHAY-p1LsuwEaJlNo'
hero_bot = PriceBot('HERO', 'metahero', BOT_TOKEN)

#@hero_bot.event
#async def on_ready():
#    await hero_bot.continue_price_update()

#hero_bot.run(BOT_TOKEN)