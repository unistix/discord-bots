import discord
import asyncio
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
import random


commandmessageID = ""

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('client ready')

@client.event
async def on_member_join(member):
	channel = member.guild.system_channel

	file = 'pics/pic1.gif'
	_file = 'pics/pic' + str(random.randint(1,14)) +'.gif'
	print(_file)

	#background = Editor("pics/pic1.gif")
	#profile_image = await load_image_async(str(member.avatar_url)) #users image url
	#profile = Editor(profile_image).resize((150,150)).circle_image()
	#poppins = Font.poppins(size=50, variant="bold")

	#poppins_small = Font.poppins(size=50, variant="light")

	#background.paste(profile, (325,90))
	#background.ellipse((325,90), 150, 150, outline="white", stroke_width=5)
	#background.text((400, 260), f"Welcome to {member.guild.name}", color="white", font=poppins, align="center")
	#background.text((400, 325), f"{member.name} #{member.discriminator}", color="white", font=poppins_small, align="center")

	#file = File(fp=background.image_bytes, filename="pic1.gif")
	await channel.send(f"Hello {member.mention}! Welcome to **{member.guild.name}** please select your role in **#role-select **for cookies type !cookie")
	await channel.send(file=discord.File(_file));



@client.command(pass_context=True)
async def welcome(ctx):
	#message = await ctx.channel.send("Testing Welcome Bot")
	#channel = member.guild.system_channel
	member = ctx.author
	channel = member.guild.system_channel


	background = Editor("pics/pic1.gif")
	profile_image = await load_image_async(str(ctx.author.avatar_url)) #users image url
	profile = Editor(profile_image).resize((150,150)).circle_image()
	poppins = Font.poppins(size=50, variant="bold")

	poppins_small = Font.poppins(size=50, variant="light")

	background.paste(profile, (325,90))
	background.ellipse((325,90), 150, 150, outline="white", stroke_width=5)
	background.text((400, 260), f"Welcome to {member.guild.name}", color="white", font=poppins, align="center")
	background.text((400, 325), f"{member.name} #{member.discriminator}", color="white", font=poppins_small, align="center")

	file = File(fp=background.image_bytes, filename="pic1.gif")
	await channel.send(f"Hello {member.mention}! Welcome to **{member.guild.name}** for cookies type !cookie**")
	await channel.send(file=file);
    
	#global commandmessageID
	#commandmessageID = message.id 
	#print(commandmessageID)


client.run('')