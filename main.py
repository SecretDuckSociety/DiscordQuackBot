# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from os import listdir

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
image_path = "./duck_images/"
images_names = listdir(image_path)


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.channel.id == 898689132543479858 and 'quack' in message.content.lower():
        image_name = random.choice(images_names)
        await message.channel.send(file=discord.File(image_path + image_name))


client.run(TOKEN)
