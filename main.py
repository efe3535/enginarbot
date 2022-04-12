from unicodedata import name
import dotenv,discord
from discord.ext import commands
from random import randint

intents = discord.Intents.default()
intents.members = True
# 
description = "enginarbot: simple, useful."

bot = commands.Bot(command_prefix="&", description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ")

@bot.command()
async def seks(ctx, kim: str, kime=""):
    if kime == "":
        await ctx.reply(f"<@{ctx.author.id}> {kim}'i sikiyor ulan!")
    else:
        await ctx.reply(f"{kim} {kime}'i sikiyor ulan!", mention_author=False)

bot.run(dotenv.get_key(key_to_get="TOKEN", dotenv_path=".env"))
