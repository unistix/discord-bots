import discord
import asyncio
from discord.ext import commands

#intents = discord.Intents(messages=True, guilds=True)
#intents=intents

commandmessageID = ""

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('client ready')

#@client.command()
#async def ping():
#    await client.say('Pong')

@client.command(pass_context=True)
async def cookie(ctx):
    message = await ctx.channel.send("Would you like a cookie \n <:yes:997480185618247721> Yes \n <:no:997480228223987782> No")
    
    
    global commandmessageID
    commandmessageID = message.id 
    print(commandmessageID)
    




@client.event
async def on_raw_reaction_add(payload):
    #We can actually add this to Timmy because of the message ID system

    print(payload.emoji.name)
    print(payload.message_id)
    print(commandmessageID)
    #setting variables for payload contents
    user_name = payload.member.name
    #user_name = user_name.split('#',1)[0]
    print(user_name)

    message_id = payload.message_id
    if message_id == commandmessageID:
        
        #print(payload.me)
    #compare the ID of the specific role message so the bot only responds to this specific role message,
    # don't want bot responding to random messages. 
        guild_id = payload.guild_id #server ID
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds) #using discord find from ultilites library and search through the guild ID from a list of guilds IDs of guilds the bot is in.
        
        #roles = discord.utils.get(guild.roles, name='C++')
        if payload.emoji.name == 'yes':
            
            channel_id = payload.channel_id
            channel = client.get_channel(channel_id)
            await channel.send(f' Here you go {user_name} :cookie:! ')
            

            #this is finds the role based on the name but doesn't actually ad user
            #role = discord.utils.get(guild.roles, name='bomb')

        if payload.emoji.name == 'no':
            
            channel_id = payload.channel_id
            channel = client.get_channel(channel_id)
            await channel.send(f' Alright then')


        
#@client.event
#async def on_message(message):
#    if client.user.id != message.author.id:
#        if 'foo' in message.content:
#            await client.send_message(message.channel, 'bar')

#    await client.process_commands(message)
#loop = asyncio.get_event_loop()
#    tasks = func_normal(), func_infinite()
#    x = loop.run_until_complete(asyncio.gather(*tasks))
#    print(x)
#    loop.close()

client.run(TOKEN)