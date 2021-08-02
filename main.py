# bot.py
import json
import os
import random

import discord
import requests
from discord.ext import commands

client = commands.Bot(command_prefix="!")



@client.event
async def on_ready():
    print("Iam ready!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!news"))
    
    




@client.command()
async def news_status(ctx):
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=353a4fcdcbe7413b8c99de9a311dcfc6'
    # Do the HTTP get request
    response = requests.get(url, verify=True)
    json_data = json.loads(response.text)
    status_server = json_data['status']
    total_results = json_data['totalResults']
    await ctx.send('Status is: {}'.format(status_server))
    await ctx.send('Total Articles: {}'.format(total_results))


@client.command()
async def news_india(ctx):

    url = 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=353a4fcdcbe7413b8c99de9a311dcfc6'
    # Do the HTTP get request
    response = requests.get(url, verify=True)
    json_data = json.loads(response.text)
    
    
    total_results = int(json_data['totalResults'])
    rand = random.randint(1, 10)
    author = json_data['articles'][rand]['author']
    title = json_data['articles'][rand]['title']
    description = json_data['articles'][rand]['description']
    url = json_data['articles'][rand]['url']
    urlImage = json_data['articles'][rand]['urlToImage']
    publishedAt = json_data['articles'][rand]['publishedAt']
    content = json_data['articles'][rand]['content']
    await ctx.send("**" + title + "**")
    await ctx.send("``" + author + "``")
    await ctx.send(url)

@client.command()
async def news_glob(ctx):

    url = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=353a4fcdcbe7413b8c99de9a311dcfc6'
    # Do the HTTP get request
    response = requests.get(url, verify=True)
    json_data = json.loads(response.text)
    rand = random.randint(1, 5)
    print(rand)

    author = json_data['articles'][rand]['author']
    title = json_data['articles'][rand]['title']
    description = json_data['articles'][rand]['description']
    url = json_data['articles'][rand]['url']
    urlImage = json_data['articles'][rand]['urlToImage']
    publishedAt = json_data['articles'][rand]['publishedAt']
    content = json_data['articles'][rand]['content']
    await ctx.send("**"+title+"**")
    await ctx.send("``"+author+"``")
    await ctx.send(url)

@client.command()
async def news_dev(ctx):
    await ctx.channel.send("``"+"| Hello, I am a X Æ A-12 Bot."+"``")
    await ctx.channel.send("``"+"| Currently under development."+"``")
    await ctx.channel.send("``"+"| Author :: ΜΔK#8374"+"``")
    await ctx.channel.send("``"+"| Prefix: !  [!news]"+"``")


@client.command()
async def news(ctx):
    await ctx.send("``"+"| !news_india > Top Tech Headlines of India"+"``")
    await ctx.send("``"+"| !news_glob > Top Tech Headlines of World"+"``")
    await ctx.send("``"+"| !news_status > Server Status"+"``")
    await ctx.send("``"+"| !news_dev > Information"+"``")
    await ctx.send("``"+"| !joke > :)🤪"+"``")
    await ctx.send("``"+"| Thank you!"+"``")

@client.command()
async def joke(ctx):
    data = requests.get("https://official-joke-api.appspot.com/random_joke")
    y = json.loads(data.text)
    await ctx.channel.send(y["setup"])  # Prints the joke question
    await ctx.channel.send(y["punchline"])  # Prints the joke answer    



#hello there






client.run("ODcxNjMxNDExNzEzNTQ0MjAz.YQeIAg.dFRVr5pXo9tAinK_Yxaye-yXYfY")
