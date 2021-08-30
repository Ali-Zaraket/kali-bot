import discord
from bot import ServerBot, BOT_TOKEN

# BOT INTENTS
intents = discord.Intents.default()
intents.members = True

bot = ServerBot(intents=intents)

bot.run(BOT_TOKEN)
