import discord
from discord.ext import commands



bot = commands.bot()

@bot.event
async def on_ready():
    print('i am ready')
    print(bot.user.name)
    print(bot.user.id)

bot.run('OTU0MDUwODE1MDg4Mjg3ODQ0.YjNfDw.2k5uqspcp-D7mP66eqZvZ09927E')
