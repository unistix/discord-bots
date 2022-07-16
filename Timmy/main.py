import discord
import random

TOKEN = 'TOKEN'

client = discord.Client()


# Log in 
@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): #message is every message which comes into the server [Not just addressed to the bot]
	username = str(message.author).split('#')[0] #gets the username of the author of the message then splits it at the #
	user_message = str(message.content) #content coming in
	channel =str(message.channel.name) #log which channel the message is coming from 
	print(f'{username}: {user_message} ({channel})') #logs the interation 

#make sure bot doesn't spiral and always reply to itself
	if message.author == client.user:
		return

#make sure to only reply in a specific channel
	if message.channel.name == 'bot-test':
		if user_message.lower() == 'hello': #recogrnise message before responding 
			await message.channel.send(f' Hi {username}!') #respond to user name that sent it to use 
			print(user_message)
			return 
		elif user_message.lower() == 'bye':
			await message.channel.send(f' See you later {username}!') #respond to user name that sent it to use 
			print('bye working')
			return 

		elif user_message.lower() == '!random':
			response = f'This is your random number:{random.randrange(10000)}'
			await message.channel.send(response) #respond to user name that sent it to use 
			return 
		else: 
			return

	#make sure to only reply in a specific channel can be used for anywhere	
	else:
		
		if user_message.lower() == 'hello timmy': #recogrnise message before responding 

			await message.channel.send(f' Hi {username}!') #respond to user name that sent it to use 

			await message.channel.send("I'm Timmy, I'm a bot would you like a cookie reply !yes or !no?")
			#good place to test basic reaction with emotes 
			if user_message.lower() == '!yes':
				await message.channel.send(f' Here you go :cookie: {username}!')
			
			print(user_message)
			
		elif user_message.lower() == 'bye timmy':
			await message.channel.send(f' See you later {username}!') #respond to user name that sent it to use 
			print('bye working')
			return 

		elif user_message.lower() == '!random':
			response = f'This is your random number:{random.randrange(10000)}'
			await message.channel.send(response) #respond to user name that sent it to use 
			return 

		elif user_message.lower() == '!yes':
				await message.channel.send(f' Here you go :cookie: {username}!')

		elif user_message.lower() == '!no':
				await message.channel.send(f' Alrighty then')
			
			
		else: 
			return



client.run(TOKEN)