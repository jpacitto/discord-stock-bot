import os
import discord
from datetime import date
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries

load_dotenv()

bot = discord.Client()

key = os.getenv("ALPHA_VANTAGE_API_KEY")
ts = TimeSeries(key)

@bot.event
async def on_ready():
        guild_count = 0

        for guild in bot.guilds:
            print(f"- {guild.id} (name: {guild.name}")
            guild_count = guild_count + 1
        
        print("Stock_Bot is in " + str(guild_count) + " guilds.")
    

@bot.event
async def on_message(message):
    
    words = message.content.split()
    for word in words:
        if(word.startswith("$")):
            print("found ", word)
            aapl, meta = ts.get_daily(symbol=word[1:])
            print(aapl['2021-02-19'])
            await message.channel.send("opkpokpo")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))