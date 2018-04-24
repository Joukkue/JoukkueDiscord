import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

client = discord.Client()
client = commands.Bot(command_prefix="/")
@client.event
async def on_ready():
    await udp_client("asd")
    print("The bot is online")

@client.command(pass_context=True)
async def test(ctx):
    print("penis")
    await client.say("pong")

@client.command(pass_context=True)
async def bileet(ctx):
    await client.say("Are you coming to a party?")

@client.event
async def on_voice_state_update(before, after):
    channel = list(client.get_all_channels())
    #print(channel)
    #await client.send_message(channel,  "joined the channel", tts=True)


@client.event
async def on_message(msg): #msg.content löytää tekstin mitä viestissä on
    print(msg.content)
    if msg.content.startswith("oispa"):
        await client.send_message(msg.channel, "kaljaa")
        print(msg.channel)
    await client.process_commands(msg) #So that commands may be used

@client.event
async def on_reaction_add(reaction, user):
    text = "Tervetuloa bileisiin " + user.nick
    #print(reaction.message.channel)
    if reaction.message.author.name == "Joukkue-Bot":
        await client.send_message(reaction.message.channel, text)

import socket
import sys

async def udp_client(asd):

    HOST = "127.0.0.1"
    PORT = 80

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Client socket created")
    except socket.error as msg:
        print("Client failed to create socket. Error: " + str(msg))
        sys.exit()
    s.bind((HOST, PORT))

    while True:
        await custom_sleep(1)
        try:
            s.settimeout(1)
            d = s.recvfrom(1024)
            reply = d[0].decode()
            addr = d[1]
            if not reply:
                break
            await client.send_message(discord.Object(id='351285503116443668'), reply)
            print("Server reply: " + reply)

        except socket.timeout:
            pass



async def custom_sleep(time):
        await asyncio.sleep(time)


client.run("MzUxMjkzNDU3NjEzOTc5NjU4.DX65NA.sqfgxgvL9aaaX0zSlvxBoWckx0M")

