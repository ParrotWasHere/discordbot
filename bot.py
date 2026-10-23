import discord
import random
import requests
import os
from discord.ext import commands
from bot_logic import gen_pass

import random

intents = discord.Intents.default()
intents.message_content = True
images = [f for f in os.listdir('./images')]

bot = commands.Bot(command_prefix='-', intents=intents)

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
async def meme(ctx):
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        picture = discord.File(f)
        await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)



bot.run('TOKEN')