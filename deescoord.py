import os
import discord
import random
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        print(f"whomst has awakened the ancient {client.user}" + '\n' + f"{guild.name} (id: {guild.id})")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hello' in message.content.lower() :
        await message.channel.send(f'General {message.author.mention}!!')

    

@client.event
async def on_member_join(member):
    welcome = [f"Ohh!! Look what the cat dragged in!!. Lets clean {member.name} up!!",
               f"Hola Amigo {member.name}. Gracias por unirte",
               f"Ahhh!! {member.name} smoll pp??.."]
    await member.create_dm()
    await member.dm_channel.send(random.choice(welcome))


client.run(TOKEN)

