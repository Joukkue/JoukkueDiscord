import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import json
from credentials import joukkue

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
    if msg.channel.id == '351285503116443668':
        await forward_message(msg.content)
    if msg.content.startswith("oispa"):
        await client.send_message(msg.channel, "kaljaa")
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
    PORT = 8250

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
            message = json.loads(reply)
            if not reply:
                break
            embed = discord.Embed(title=message['chat']["title"], color=0x00ff00)
            embed.add_field(name=message['from']['username'], value=message['text'], inline=False)
            await client.send_message(discord.Object(id='351285503116443668'), embed=embed)
            print("Server reply: " + reply)

        except socket.timeout:
            pass

    await s.close()



async def custom_sleep(time):
        await asyncio.sleep(time)

async def forward_message(msg):
    HOST = ''
    PORT = 8252
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    addr = ('127.0.0.1', 8253)
    reply = json.dumps(msg)
    s.sendto(reply.encode(), addr)

    s.close()



client.run(joukkue)

