import discord
from discord.channel import VoiceChannel
from discord.errors import ClientException
from discord.ext import commands
import time
from random import choice
import asyncio

import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "!", intents=intents)


@client.event 
async def on_ready():
    print("Gouday")

@client.command()
async def Gouday(ctx):
    user = ctx.author
    server = ctx.guild
    for vc in server.voice_channels:
        if user in vc.members:
            vc_name = vc.name
    VoiceChannel = discord.utils.get(ctx.guild.voice_channels, name = vc_name)
    try:
        await VoiceChannel.connect()
    except ClientException:
        await ctx.channel.send("I'm already talking to someone!")
        return

    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    voice.play(discord.FFmpegPCMAudio("meet_you.mp3"))

    await ctx.channel.send(f"Cheesed to meet you {user.name}")
    await asyncio.sleep(5)
    await ctx.channel.send("Hm.......")
    await asyncio.sleep(5)
    outcome = choice(['cheesed', 'discheesed'])
    if outcome == 'cheesed':
        voice.play(discord.FFmpegPCMAudio("cheesed.mp3"))
        await ctx.channel.send("You have left me quite cheesed")
    else:
        voice.play(discord.FFmpegPCMAudio("discheesed.mp3"))
        await ctx.channel.send("You have left me quite discheesed")

    await asyncio.sleep(10)
    await ctx.voice_client.disconnect()


##have the bot stay in there and talk to people

        
    


client.run(os.getenv('TOKEN'))