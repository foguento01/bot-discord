import discord
from discord.ext import commands

import os
TOKEN = os.getenv("MTExNjQxMjgzMjU2OTg4NDcyNQ.G8La_W.ItMPGU3PREVmK14r26RI-Nn_Vbh4QlcNPrMnEw")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Bot online como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

bot.run(TOKEN)
