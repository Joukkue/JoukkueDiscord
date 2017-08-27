import discord
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="/")
@client.event
async def on_ready():
    print("The bot is online")

@client.command(pass_context=True)
async def test(ctx):
    print("penis")
    #await client.say("pong", tts=True)

@client.event
async def on_voice_state_update(before, after):
    channel = list(client.servers)[0]
    print(channel)
    #await client.send_message(channel,  "joined the channel", tts=True)


@client.event
async def on_message(msg): #msg.content löytää tekstin mitä viestissä on
    print(msg.content)
    if msg.content.startswith("oispa"):
        await client.send_message(msg.channel, "kaljaa")
        print(msg.channel)
    await client.process_commands(msg) #So that commands may be used

client.run("MzUxMjkzNDU3NjEzOTc5NjU4.DIQflg.mUXZck40bzRLg9HOA9QC48nWSTs")

