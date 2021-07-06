import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

token1 = os.environ['token']
server1 = os.environ['server']


bot = commands.Bot(command_prefix="!")
@bot.command(name='sleep')
async def work_pls(ctx, name, num):
  r_list = ['Got to bed!', 'Sleep is really good for your health!', 'Dreams are sometimes fun', 'You need sleep!', 'Please go to sleep!', 'Go to sleep or no choco wafflez for you', 'Sleep or I will get a board', '']
  emoji_list = ['💤','😴', '🛌']
  num2 = int(num)
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




bot.run(token1)
