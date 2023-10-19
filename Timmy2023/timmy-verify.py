import discord
import asyncio
import os 
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
DISCORDTOKEN=os.environ.get('DISCORD_TOKEN')

commandmessageID = ""

print("testing")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('client ready')


@client.event
async def on_raw_reaction_add(payload):
	#We can actually add this to Timmy because of the message ID system
	print("Hello")
	print(payload.emoji.name)
	print(payload.message_id)
	#setting variables for payload contents
	message_id = payload.message_id
	if message_id == 1164514527371603998: #Pinned verify message
		#print(payload.me)
	#compare the ID of the specific role message so the bot only responds to this specific role message,
	# don't want bot responding to random messages. 
		guild_id = payload.guild_id #server ID
		guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds) #using discord find from ultilites library and search through the guild ID from a list of guilds IDs of guilds the bot is in.
		
		#roles = discord.utils.get(guild.roles, name='C++')
		#if payload.emoji.name == 'bomb':
		#	print("Bomb Role")
			#this is finds the role based on the name but doesn't actually ad user
		#	role = discord.utils.get(guild.roles, name='bomb')


		#elif payload.emoji.name == "chocolatechip":
		#	print("Cookie Role")
		#	role = discord.utils.get(guild.roles, name='cookie')
		#else:
		role = discord.utils.get(guild.roles, name=payload.emoji.name)

		if role is not None:
			#this is 
			#print(payload.user_id)
			#print(guild.members)
			print('Role is %s ' % (role.name))
			member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

			if member is not None:
				await member.add_roles(role)
				print("done")
			else:
				print("Member not found")
		else:
			print("Role not found")


client.run(DISCORDTOKEN)