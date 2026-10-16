import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import set_time

import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login com {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá {ctx.author.mention}!')


@bot.command()
async def password(ctx):
    password = gen_pass(10)
    await ctx.send(f'Sua senha gerada é: {password}!')

@bot.command()
async def time(ctx):
    clock = set_time(10)
    await ctx.send(clock)







bot.run('TOKEN')