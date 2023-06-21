# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

with open('token.txt', 'r') as f:
	token = f.read()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'With the ID: {client.user.id}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('!test'):
        await message.channel.dm_channel.send('Hello!')

client.run(token)