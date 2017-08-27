import discord
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    print("The bot is online")

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("pong")

@client.event
async def on_message(msg): #msg.content löytää tekstin mitä viestissä on
    print(msg.content)
    if msg.content.startswith("oispa"):
        await client.send_message(msg.channel, "kaljaa")

client.run("MzUxMjkzNDU3NjEzOTc5NjU4.DIQflg.mUXZck40bzRLg9HOA9QC48nWSTs")