import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import requests

load_dotenv()

token1 = os.environ['token']
server1 = os.environ['server']
pin = os.environ['close_pin']

@bot.command(name="close")
async def shutdown(ctx, num='0'):
  num2 = int(num)
  a = int(pin)
  if num2 == a:
    await ctx.send('request granted')
    await ctx.bot.close()
  elif num2 != a:
    await ctx.send('request denied')

@bot.command(name="backfire")
async def backfireFunction(ctx):
  global backfire
  backfire = True

bot = commands.Bot(command_prefix="!")
@bot.command(name='sleep')
async def work_pls(ctx, name, num):
  r_list = ['Got to bed!', 'Sleep is really good for your health!', 'Dreams are sometimes fun', 'You need sleep!', 'Please go to sleep!', 'Go to sleep or no choco wafflez for you', 'Sleep or I will get a board', '']
  emoji_list = ['💤','😴', '🛌']
  num2 = int(num)
  if num2 >= 40:
    num2 = 40
    r4 = "i dont feel like spamming that messgae for that long"
    await ctx.send(r4)
  for i in range(num2):
    r1 = random.choice(r_list)
    emoji = random.choice(emoji_list)
    response = r1 + " " + emoji + " " + name
    await ctx.send(response)

@bot.command(name='eat')
async def func2(ctx):
  await ctx.send(ctx.message.author.mention)

@bot.command(name="books")
async def read1(ctx):
  books = ['PJO', 'HOO', 'A Night Divided', 'Words On Fire', 'Giver', 'A Swiftly Tilting Planet']
  response = 'You should read ' + random.choice(books)
  await ctx.send(response)
  
@bot.command(name="spam")
async def spam1(ctx,emoji,num):
  num2 = int(num)
  for i in range(num2):
    response = emoji
    await ctx.send(response)
@bot.command(name='ISS')
async def find_ISS(ctx, item):
  iss = requests.get('https://api.wheretheiss.at/v1/satellites/25544').json()
  response = ""
  if item == "index":
    for i in iss:
      response += i
      response += ", "
  else:
    lat = iss[f'{item}']
    response = f"The {item} of the ISS is:{lat}"
  await ctx.send(response)

@bot.command(name="API")
async def func3(ctx, api_link, key):
  api = requests.get(api_link).json()
  response = ''
  if key == 'index':
    for i in api:
      response += i
      response += ", "
  else: 
    response = api[f'{key}']
  await ctx.send(response)

@bot.command(name="ship")
async def func5(ctx, name1, name2):
  extra_functions.ship(name1,name2)
  extra_functions.ship(name2,name1)
  names2 = tuple(extra_functions.names)
   
  response = """That sounds like a great ship! :heart:, I LOVE it already!!
  """
  num3 = 0
  for i in names2:
    num3 += 1
    if num3 > 500:
      await ctx.send(response)
      num3 = 0
      response = ""
    else:
      response += i + ", "
  
  await ctx.send(response)

bot.run(token1)
