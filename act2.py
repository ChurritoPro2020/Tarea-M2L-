import random
import discord 
import os
import requests
from discord.ext import commands

description = '''Vamos interactuar con imagenes'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/',intents = intents)

list_memes = os.listdir('imagenes')
list_animales = os.listdir('animales')
list_futbol = os.listdir('futbol')
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'logeado como {bot.user} (ID: {bot.user.id})')

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def meme(ctx):
    select_meme = random.choice(list_memes)
    with open(f'imagenes/{select_meme}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(content='aqui esta tu meme recien horneado',file=picture)

@bot.command()
async def animales(ctx):
    select_meme = random.choice(list_animales)
    with open(f'animales/{select_meme}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(content='aqui esta tu meme de animalito :)',file=picture)

@bot.command()
async def futbol(ctx):
    select_meme = random.choice(list_futbol)
    with open(f'futbol/{select_meme}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(content='aqui esta tu meme de futbol',file=picture)

bot.run('')

