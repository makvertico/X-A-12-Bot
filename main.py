import json
import random

from pprint import pprint
import discord
from discord import channel
import requests
from discord.ext import commands ,tasks

client = commands.Bot(command_prefix="!")
colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]



@client.event
async def on_ready():
    print("Iam Ready!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!news"))
    
    
@client.command()
async def news_start(ctx):
    auto_send.start()
    print('!news_start command')
    print("Auto Mode = Enabled")
    
    embedVar = discord.Embed(title="", description="", color = random.choice(colors))
    embedVar.add_field(name="**MODE** [auto]  " , value="``Enabled``")
    return await ctx.channel.send(embed=embedVar) 
   
    
        
@client.command()
async def news_stop(ctx):
    auto_send.cancel()
    print("Auto Mode = Disabled")
    embedVar = discord.Embed(title="", description="", color = random.choice(colors))
    embedVar.add_field(name="**MODE** [auto]  " , value="``Disabled``")
    return await ctx.channel.send(embed=embedVar)


@client.command()
async def news_status(ctx):
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=353a4fcdcbe7413b8c99de9a311dcfc6'
    #request
    response = requests.get(url, verify=True)
    json_data = json.loads(response.text)
    status_server = json_data['status']
    total_results = json_data['totalResults']
 
    embedVar = discord.Embed(title="", description="", color= 0x00ff00)
    embedVar.add_field(name="Server Status\n", value=status_server, inline=False)
    embedVar.add_field(name="Total Results\n", value=total_results, inline=False)
    await ctx.channel.send(embed=embedVar)
    print("Fetching Headlines from country = US ")
    
    # await ctx.send('Status is: {}'.format(status_server))
    # await ctx.send('Total Articles: {}'.format(total_results))



@client.command()
async def news_india(ctx):
    

    url = 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=353a4fcdcbe7413b8c99de9a311dcfc6'
    #request
    response = requests.get(url, verify=True)
    json_url = json.loads(response.text)
    data_str = json.dumps(json_url).replace('null', '"No Data"')
    json_data = json.loads(data_str)
    print(json_data)
    print("Clean Json : ",json_data)
    json_size = len(json_data['articles'])
    print("Length of the Json: ",json_size)
    
    total_results = int(json_data['totalResults'])
    rand = random.randint(1, json_size-1)
    author = json_data['articles'][rand]['author']
    title = json_data['articles'][rand]['title']
    description = json_data['articles'][rand]['description']
    url = json_data['articles'][rand]['url']
    urlImage = json_data['articles'][rand]['urlToImage']
    publishedAt = json_data['articles'][rand]['publishedAt']
    content = json_data['articles'][rand]['content']
    

    embedVar = discord.Embed(title=title, description="", color = random.choice(colors))
    embedVar.add_field(name="Author", value=author, inline=True)
    embedVar.add_field(name="---------------------------------", value=url, inline=False)
    embedVar.add_field(name="---------------------------------", value=content, inline=False)
    embedVar.add_field(name="---------------------------------", value=description, inline=False)
    embedVar.add_field(name="---------------------------------", value=publishedAt, inline=False)
    await ctx.channel.send(embed=embedVar)

    # await ctx.send("**" + title + "**")
    # await ctx.send("``" + author + "``")
    # await ctx.send(url)

@client.command()
async def news_globe(ctx):
    print('!news_globe command') 
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=353a4fcdcbe7413b8c99de9a311dcfc6'
    response = requests.get(url, verify=True)
    json_url = json.loads(response.text)
    data_str = json.dumps(json_url).replace('null', '"No Data"')
    json_data = json.loads(data_str)
    print(json_data)
    print("Clean Json : ",json_data)
    json_size = len(json_data['articles'])
    print("Length of the Json: ",json_size)
    
    total_results = int(json_data['totalResults'])
    rand = random.randint(1, json_size-1)
    author = json_data['articles'][rand]['author']
    title = json_data['articles'][rand]['title']
    description = json_data['articles'][rand]['description']
    url = json_data['articles'][rand]['url']
    urlImage = json_data['articles'][rand]['urlToImage']
    publishedAt = json_data['articles'][rand]['publishedAt']
    content = json_data['articles'][rand]['content']
    

    embedVar = discord.Embed(title=title, description="", color = random.choice(colors))
    embedVar.add_field(name="Author", value=author, inline=True)
    embedVar.add_field(name="---------------------------------", value=url, inline=False)
    embedVar.add_field(name="---------------------------------", value=content, inline=False)
    embedVar.add_field(name="---------------------------------", value=description, inline=False)
    embedVar.add_field(name="---------------------------------", value=publishedAt, inline=False)
    await ctx.channel.send(embed=embedVar)
    print('Data Fetched successfully') 


    

    
@client.command()
async def joke(ctx):
    data = requests.get("https://official-joke-api.appspot.com/random_joke")
    y = json.loads(data.text)
    setup = y["setup"]  
    punchline = y["punchline"] 
    embedVar = discord.Embed(title="", description="", color = random.choice(colors))
    embedVar.add_field(name=setup, value=punchline, inline=False)
    await ctx.channel.send(embed=embedVar)
    print('Data Fetched successfully') 



     

@tasks.loop(minutes=30)
async def auto_send():
    channel = await client.fetch_channel('852579630807777376')
    if not channel:
            await("Don't have the Permission to send in this Channel!")
    else:
        url = 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=353a4fcdcbe7413b8c99de9a311dcfc6'
    # Do the HTTP get request
        response = requests.get(url, verify=True)
        json_url = json.loads(response.text)
        data_str = json.dumps(json_url).replace('null', '"No Data"')
        json_data = json.loads(data_str)
        print(json_data)
    
        total_results = int(json_data['totalResults'])
        rand = random.randint(1, 20)
        author = json_data['articles'][rand]['author']
        title = json_data['articles'][rand]['title']
        description = json_data['articles'][rand]['description']
        url = json_data['articles'][rand]['url']
        urlImage = json_data['articles'][rand]['urlToImage']
        publishedAt = json_data['articles'][rand]['publishedAt']
        content = json_data['articles'][rand]['content']
    

        embedVar = discord.Embed(title=title, description="", color = random.choice(colors))
        embedVar.add_field(name="Author", value=author, inline=True)
        embedVar.add_field(name="---------------------------------", value=url, inline=False)
        embedVar.add_field(name="---------------------------------", value=content, inline=False)
        embedVar.add_field(name="---------------------------------", value=description, inline=False)
        embedVar.add_field(name="---------------------------------", value=publishedAt, inline=False)
        await channel.send(embed=embedVar)  
        

@client.command()
async def news_dev(ctx):
    print('!news_dev command') 
    embedVar = discord.Embed(title="", description="", color = random.choice(colors))
    embedVar.add_field(name="Hello, I am a X Æ A-12 Bot.", value="~", inline=False)
    embedVar.add_field(name="Currently under development.", value="~", inline=False)
    embedVar.add_field(name="Author :: ΜΔK#8374", value="~", inline=False)
    embedVar.add_field(name="Prefix: !  [!news]", value="~", inline=False)
    await ctx.channel.send(embed=embedVar)
       
    
   


@client.command()
async def news(ctx):
    print('!news command')
    embedVar = discord.Embed(title="", description="", color = random.choice(colors))
    embedVar.add_field(name="\n~", value="**!news_india** ~ Top Tech Headlines of India", inline=False)
    embedVar.add_field(name="\n~", value="**!news_globe** ~ Top Tech Headlines of World", inline=False)
    embedVar.add_field(name="\n~", value="**!news_status** ~ Server Status", inline=False)
    embedVar.add_field(name="\n~", value="**!news_dev** ~ Information", inline=False)
    embedVar.add_field(name="\n~", value="**!news_start** ~ Start ``[auto mode]``", inline=False)
    embedVar.add_field(name="\n~", value="**!news_stop** ~ Stop ``[auto mode]``", inline=False)
    embedVar.add_field(name="\n~", value="**!joke**  ~ 🤪", inline=False)
    embedVar.add_field(name="\n~", value="**Thank you!.**", inline=False)
    await ctx.channel.send(embed=embedVar)
    





client.run("ODcxNjMxNDExNzEzNTQ0MjAz.YQeIAg.dFRVr5pXo9tAinK_Yxaye-yXYfY")