from asyncio import events
import json
import random
import asyncio
from discord.embeds import Embed
import requests


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
    
    
@client.command(name = "news-start")
async def news_start(ctx):
    auto_send.start()
    print('!news-start command')
    print("Auto Mode = Enabled")
    
    embedVar = discord.Embed(title="", description="", color = random.choice(colors))
    embedVar.add_field(name="**MODE** [auto]  " , value="``Enabled``")
    return await ctx.channel.send(embed=embedVar) 
   
    
        
@client.command(name="news-stop")
async def news_stop(ctx):
    auto_send.cancel()
    print("Auto Mode = Disabled")
    embedVar = discord.Embed(title="", description="", color = random.choice(colors))
    embedVar.add_field(name="**MODE** [auto]  " , value="``Disabled``")
    return await ctx.channel.send(embed=embedVar)


@client.command(name= "news-status")
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

@client.command(name = "news-search")
async def search_news(ctx):
    
    print("search")
    embedVar = discord.Embed(

        title="Search News and Blog Articles",
        description="```yaml"+"\n"+"Enter news articles that mention a specific topic or keyword"+"\n```",
        color=random.choice(colors))
    embedVar.add_field(
        name="\u200b", value="```Reply within 1 min```", inline=False)
    await ctx.send(embed=embedVar)
    # ------client message return-------
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    
    try:
        return_message = await client.wait_for("message", check=check, timeout=60)

    except asyncio.TimeoutError:

       return await ctx.send("```Timeout! you didn't reply in time 😭```")

    query = return_message.content
    print("Client query: ", query)
    urlAPI = 'https://newsapi.org/v2/everything?q='+query+'&sortBy=popularity&apiKey=353a4fcdcbe7413b8c99de9a311dcfc6'

    try:
        searchURL = urlAPI
        response = requests.get(searchURL, verify=True, timeout=2)
        json_url = json.loads(response.text)
        data_str = json.dumps(json_url).replace('null', '"No Data"')
        json_data = json.loads(data_str)

    #-------------------------server connectivity-------------------------------------
    except Exception:
        return await ctx.send("```Connectivity Error! No response from server 😶```")
    
    try:
        json_size = len(json_data['articles'])

    except Exception as e:

        print(e)
        return await ctx.send("```Sorry! No result found```")
    
    print("Length of the Json: ", json_size)
    print("")
    print(json_data)
    # ------------------------------Embed View Start [Available articles] -------------------------------

    embedVar = discord.Embed(title="", description="",
                             color=random.choice(colors))
    embedVar.add_field(name="Avaliable articles: ", value=str(json_size), inline=False)
    await ctx.send(embed=embedVar)

    # ------------------------------Embed View End [Available articles]-------------------------------
      
    dataArray = json_data['articles']
    
    for i in range(len(dataArray)):
            source = (str(dataArray[i]['source']['name']))
            author = dataArray[i]['author']
            title =  dataArray[i]['title']
            description =  dataArray[i]['description']
            url =  dataArray[i]['url']
            urlImage =  dataArray[i]['urlToImage']
            publishedAt =  dataArray[i]['publishedAt']
            content =  dataArray[i]['content']
            embedVar = discord.Embed(title=title, description="", color = random.choice(colors))
            embedVar.add_field(name="Author", value=author, inline=True)
            embedVar.add_field(name="Source", value=source, inline=True)
            embedVar.add_field(name="---------------------------------", value=url, inline=False)
            embedVar.add_field(name="---------------------------------", value=content, inline=False)
            embedVar.add_field(name="---------------------------------", value=description, inline=False)
            embedVar.add_field(name="---------------------------------", value=publishedAt, inline=False)
            embedVar.set_image(url=urlImage)
            await ctx.channel.send(embed=embedVar) 

  

    

@client.command(name="news-india")
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
    source = str(json_data['articles'][rand]['source']['name'])
    title = json_data['articles'][rand]['title']
    description = json_data['articles'][rand]['description']
    url = json_data['articles'][rand]['url']
    urlImage = json_data['articles'][rand]['urlToImage']
    publishedAt = json_data['articles'][rand]['publishedAt']
    content = json_data['articles'][rand]['content']
    

    embedVar = discord.Embed(title=title, description="", color = random.choice(colors))
    embedVar.add_field(name="Author", value=author, inline=True)
    embedVar.add_field(name="Source", value=source, inline=True)
    embedVar.add_field(name="---------------------------------", value=url, inline=False)
    embedVar.add_field(name="---------------------------------", value=content, inline=False)
    embedVar.add_field(name="---------------------------------", value=description, inline=False)
    embedVar.add_field(name="---------------------------------", value=publishedAt, inline=False)
    embedVar.set_image(url=urlImage)
    await ctx.channel.send(embed=embedVar) 

    # await ctx.send("**" + title + "**")
    # await ctx.send("``" + author + "``")
    # await ctx.send(url)

@client.command(name="news-globe")
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
    source = str(json_data['articles'][rand]['source']['name'])
    author = json_data['articles'][rand]['author']
    title = json_data['articles'][rand]['title']
    description = json_data['articles'][rand]['description']
    url = json_data['articles'][rand]['url']
    urlImage = json_data['articles'][rand]['urlToImage']
    publishedAt = json_data['articles'][rand]['publishedAt']
    content = json_data['articles'][rand]['content']
    

    embedVar = discord.Embed(title=title, description="", color = random.choice(colors))
    embedVar.add_field(name="Author", value=author, inline=True)
    embedVar.add_field(name="Source", value=source, inline=True)
    embedVar.add_field(name="---------------------------------", value=url, inline=False)
    embedVar.add_field(name="---------------------------------", value=content, inline=False)
    embedVar.add_field(name="---------------------------------", value=description, inline=False)
    embedVar.add_field(name="---------------------------------", value=publishedAt, inline=False)
    embedVar.set_image(url=urlImage)
    await ctx.channel.send(embed=embedVar) 
    print('Data Fetched successfully') 


    

    
# @client.command()
# async def joke(ctx):
#     data = requests.get("https://official-joke-api.appspot.com/random_joke")
#     y = json.loads(data.text)
#     setup = y["setup"]  
#     punchline = y["punchline"] 
#     embedVar = discord.Embed(title="", description="", color = random.choice(colors))
#     embedVar.add_field(name=setup, value=punchline, inline=False)
#     await ctx.channel.send(embed=embedVar)
#     print('Data Fetched successfully') 



     

@tasks.loop(hours=3)
async def auto_send():
    channel = await client.fetch_channel('874319484389838899')
    if not channel:
            await("Don't have the Permission to send in this Channel!")
    else:
        url = 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=353a4fcdcbe7413b8c99de9a311dcfc6'
    # Do the HTTP get request
        response = requests.get(url, verify=True)
        json_url = json.loads(response.text)
        data_str = json.dumps(json_url).replace('null', '"No Data"')
        json_data = json.loads(data_str)
        print("Clean Json : ",json_data)
        json_size = len(json_data['articles'])
        print("Length of the Json: ",json_size)
        dataArray = json_data['articles']
        total_results = int(json_data['totalResults'])
        rand = random.randint(1, json_size-1)
        source = str(json_data['articles'][rand]['source']['name'])
        author = json_data['articles'][rand]['author']
        title = json_data['articles'][rand]['title']
        description = json_data['articles'][rand]['description']
        url = json_data['articles'][rand]['url']
        urlImage = json_data['articles'][rand]['urlToImage']
        publishedAt = json_data['articles'][rand]['publishedAt']
        content = json_data['articles'][rand]['content']

        embedVar = discord.Embed(title=title, description="", color = random.choice(colors))
        embedVar.add_field(name="Author", value=author, inline=True)
        embedVar.add_field(name="Source", value=source, inline=True)
        embedVar.add_field(name="---------------------------------", value=url, inline=False)
        embedVar.add_field(name="---------------------------------", value=content, inline=False)
        embedVar.add_field(name="---------------------------------", value=description, inline=False)
        embedVar.add_field(name="---------------------------------", value=publishedAt, inline=False)
        embedVar.set_image(url=urlImage)
        await channel.send(embed=embedVar) 
        

@client.command(name="news-dev")
async def news_dev(ctx):
    print('!news_dev command') 
    embedVar = discord.Embed(title="", description="", color = random.choice(colors))
    embedVar.add_field(name="Hello, I am a X Æ A-12 Bot.", value="~", inline=False)
    embedVar.add_field(name="Currently under development.", value="~", inline=False)
    embedVar.add_field(name="Author :: ΜΔK#8374", value="~", inline=False)
    embedVar.add_field(name="Prefix: !  [!news]", value="~", inline=False)
    await ctx.channel.send(embed=embedVar)
       
    
   


@client.command(name="news")
async def news(ctx):
    print('!news command')
    embedVar = discord.Embed(title="", description="", color = random.choice(colors))
    embedVar.add_field(name="\n~", value="**!news-search** ~ Search News and Blog Articles", inline=False)
    embedVar.add_field(name="\n~", value="**!news-india** ~ Top Tech Headlines of India", inline=False)
    embedVar.add_field(name="\n~", value="**!news-globe** ~ Top Tech Headlines of World", inline=False)
    embedVar.add_field(name="\n~", value="**!news-status** ~ Server Status", inline=False)
    embedVar.add_field(name="\n~", value="**!news-dev** ~ Information", inline=False)
    embedVar.add_field(name="\n~", value="**!news-start** ~ Start ``[auto mode]``", inline=False)
    embedVar.add_field(name="\n~", value="**!news-stop** ~ Stop ``[auto mode]``", inline=False)
    # embedVar.add_field(name="\n~", value="**!joke**  ~ 🤪", inline=False)
    embedVar.add_field(name="\n~", value="**Thank you!.**", inline=False)
    await ctx.channel.send(embed=embedVar)
    





client.run("TOKEN")
