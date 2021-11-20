@echo off
Taskkill /IM "BitcoinBot.exe" /F
Taskkill /IM "BinanceBot.exe" /F
Taskkill /IM "HeroBot.exe" /F
Taskkill /IM "HunchoBot.exe" /F
pyinstaller -y -F -w -i .\ico\bitcoin.ico -n BitcoinBot bitcoin_bot.py 
pyinstaller -y -F -w -i .\ico\hero.ico -n HeroBot hero_bot.py 
pyinstaller -y -F -w -i .\ico\bnb.ico -n BinanceBot bnb.py 
pyinstaller -y -F -w -i .\ico\huncho.ico -n HunchoBot huncho_bot.py 
DEL *.spec