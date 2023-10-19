import discord
import asyncio
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font


commandmessageID = ""

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('client ready')


client.run('MTAyOTA0NDUxNzA5OTI3ODM2Ng.GSK47G.UjgqFI1RtX4u50AoVoc9LFEHcP0ZbOw67O5_8E')