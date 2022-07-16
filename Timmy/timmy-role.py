import discord
from discord.ext import commands

#intents = discord.Intents(messages=True, guilds=True)
#intents=intents

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=',', intents=intents)

#client = discord.Client()
#print(discord.__version__)

#intents = discord.Intents.default()
#intents.members = True

#client = commands.Bot(command_prefix=',', intents=intents)

@client.event
async def on_ready():
	print("Bot is logged in.")

#on_raw_reaction_add
#Called when a message has a rection added called regardless of state compared to on_reaction_add()
#None raw will only use messages stored in cache so if bot is offline and message is not cached it wont work
#We will need to parse user and reaction from the raw reaction payload



@client.event
async def on_raw_reaction_add(payload):
	#We can actually add this to Timmy because of the message ID system
	print("Hello")
	print(payload.emoji.name)
	print(payload.message_id)
	#setting variables for payload contents
	message_id = payload.message_id
	if message_id == 997476036453343312: #Interests
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
	elif message_id == 997477187919810580: #Games 
		print("debug")
	#compare the ID of the specific role message so the bot only responds to this specific role message,
	# don't want bot responding to random messages. 
		guild_id = payload.guild_id #server ID
		guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds) #using discord find from ultilites library and search through the guild ID from a list of guilds IDs of guilds the bot is in.

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

	elif message_id == 997477606100324428: #NFT
		print("debug")
	#compare the ID of the specific role message so the bot only responds to this specific role message,
	# don't want bot responding to random messages. 
		guild_id = payload.guild_id #server ID
		guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds) #using discord find from ultilites library and search through the guild ID from a list of guilds IDs of guilds the bot is in.

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

	elif message_id == 997495502365020200: #Commentators
		print("debug")
	#compare the ID of the specific role message so the bot only responds to this specific role message,
	# don't want bot responding to random messages. 
		guild_id = payload.guild_id #server ID
		guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds) #using discord find from ultilites library and search through the guild ID from a list of guilds IDs of guilds the bot is in.

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




@client.event
async def on_raw_reaction_remove(payload):
	print("Remove")
#We can actually add this to Timmy because of the message ID system

	print(payload.emoji.name)
	print(payload.message_id)
	#setting variables for payload contents
	message_id = payload.message_id
	if message_id == 997476036453343312: #Interests
		#print(payload.me)
	#compare the ID of the specific role message so the bot only responds to this specific role message,
	# don't want bot responding to random messages. 
		guild_id = payload.guild_id #server ID
		guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds) #using discord find from ultilites library and search through the guild ID from a list of guilds IDs of guilds the bot is in.
		

		#else:
		role = discord.utils.get(guild.roles, name=payload.emoji.name)

		if role is not None:
			#this is 
			#print(payload.user_id)
			#print(guild.members)
			print('Removed Role %s ' % (role.name))
			member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

			if member is not None:
				await member.remove_roles(role)
				print("done")
			else:
				print("Member not found")
		else:
			print("Role not found")
	elif message_id == 997477187919810580: #Games 
		print("debug")
	#compare the ID of the specific role message so the bot only responds to this specific role message,
	# don't want bot responding to random messages. 
		guild_id = payload.guild_id #server ID
		guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds) #using discord find from ultilites library and search through the guild ID from a list of guilds IDs of guilds the bot is in.

		role = discord.utils.get(guild.roles, name=payload.emoji.name)

		if role is not None:
			#this is 
			#print(payload.user_id)
			#print(guild.members)
			print('Removed Role %s ' % (role.name))
			member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

			if member is not None:
				await member.remove_roles(role)
				print("done")
			else:
				print("Member not found")
		else:
			print("Role not found")

	elif message_id == 997477606100324428: #NFT
		print("debug")
	#compare the ID of the specific role message so the bot only responds to this specific role message,
	# don't want bot responding to random messages. 
		guild_id = payload.guild_id #server ID
		guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds) #using discord find from ultilites library and search through the guild ID from a list of guilds IDs of guilds the bot is in.

		role = discord.utils.get(guild.roles, name=payload.emoji.name)

		if role is not None:
			#this is 
			#print(payload.user_id)
			#print(guild.members)
			print('Removed Role %s ' % (role.name))
			member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

			if member is not None:
				await member.remove_roles(role)
				print("done")
			else:
				print("Member not found")
		else:
			print("Role not found")

	elif message_id == 997495502365020200: #Commentators
		print("debug")
	#compare the ID of the specific role message so the bot only responds to this specific role message,
	# don't want bot responding to random messages. 
		guild_id = payload.guild_id #server ID
		guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds) #using discord find from ultilites library and search through the guild ID from a list of guilds IDs of guilds the bot is in.

		role = discord.utils.get(guild.roles, name=payload.emoji.name)

		if role is not None:
			#this is 
			#print(payload.user_id)
			#print(guild.members)
			print('Removed Role  %s ' % (role.name))
			member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

			if member is not None:
				await member.remove_roles(role)
				print("done")
			else:
				print("Member not found")
		else:
			print("Role not found")



client.run('TOKEN')