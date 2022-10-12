import discord, requests, random, os, asyncio
from discord.ext import commands

#Delete after production: python3 -m pip install <library>
#TODO: Make a help command and make it well formatted
#TODO: Make a backup system for SQL database
#TODO: Make a README discussing SQL format, commands, etc.


#Add more cogs as needed
cog_list = ['Admin', 'Member']

#Init Bot
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)


#Loading Cogs and Starting Bot
@client.command(name="load")
async def load(ctx, name):
  await client.load_extension("cogs.{}".format(name.lower()))
  print(f"Cog {name.lower()} has been loaded")

@client.command(name="unload")
async def unload(ctx, name):
  await client.unload_extension("cogs.{}".format(name.lower()))
  print(f"Cog {name.lower()} has been unloaded")
	
async def load_extensions():
	for filename in os.listdir("./cogs"):
	    if filename.endswith(".py"):
	      await client.load_extension("cogs.{}".format(filename[:-3]))

@client.event
async def on_ready():
	print("Ready")
	await load_extensions()

os.environ['TOKEN'] = 'MTAyMDgzMjY4OTYxMzQ1OTQ4Ng.Gkpjsj.jKmSUl-dbSP4HLiMonsJILz4YAvj4kHklQT6tQ' #Enter Your Own Token Here
client.run(os.getenv('TOKEN'))


'''
Audio File System Format:

audio
    -comp_name
        -user_name
            -song_file
        -user_name
            -song_file
    -comp_name
        -user_name
            -song_file
        -user_name
            -song_file

'''


'''
For format of database, look at sql_start.py
'''