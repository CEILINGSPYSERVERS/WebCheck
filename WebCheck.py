#    __          __  _      _____ _               _
#    \ \        / / | |    / ____| |             | |
#     \ \  /\  / /__| |__ | |    | |__   ___  ___| | __
#      \ \/  \/ / _ \ '_ \| |    | '_ \ / _ \/ __| |/ /
#       \  /\  /  __/ |_) | |____| | | |  __/ (__|   <
#        \/  \/ \___|_.__/ \_____|_| |_|\___|\___|_|\_\ v.1


# WebCheck is a siple discord.py bot that pings a user defined url or ip address to see if it responds.

# library imports
import discord
from discord.ext import commands
import os
from icmplib import ping, traceroute, Host, Hop
import variable_lib as vl

os.system("cls")

# set prefix and remove default help command
client = commands.Bot(command_prefix=".")
client.remove_command("help")

# user input filter function
def IO(address, count, interval, timeout):
    address = address.replace("https:", "")
    address = address.replace("/", "")

    try:
        if count > 10:
            count = 10
        elif count <= 0:
            count = 1

        if interval > 2:
            interval = 2
        elif interval < 0.1:
            interval = 0.1

        if timeout > 5:
            timeout = 5
        elif timeout <= 0:
            timeout = 1
    except:
        return False, False

    host = ping(address, count, interval, timeout)

    return address, host


# console output making sure bot launched properly
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


# basic check command
@client.command()
async def check(ctx, address="", count=2, interval=0.25, timeout=1):
    address, host = IO(address, count, interval, timeout)
    if not host:
        await ctx.channel.send(f"```ERROR: {address} could not be resolved```")
    else:
        await ctx.channel.send(f"```{address} is alive: {host.is_alive}```")


# average ping time check command
@client.command()
async def acheck(ctx, address="", count=2, interval=0.25, timeout=1):
    address, host = IO(address, count, interval, timeout)
    if not host:
        await ctx.channel.send(f"```ERROR: {address} could not be resolved```")
    else:
        await ctx.channel.send(
            f"""```
{address} is alive: {host.is_alive}
avgRTT: {host.avg_rtt}ms
Jitter: {host.jitter}ms```"""
        )


# loss ping time check command
@client.command()
async def lcheck(ctx, address="", count=2, interval=0.25, timeout=1):
    address, host = IO(address, count, interval, timeout)
    if not host:
        await ctx.channel.send(f"```ERROR: {address} could not be resolved```")
    else:
        await ctx.channel.send(
            f"""```
{address} is alive: {host.is_alive}
Loss: {host.packet_loss}%
Sent: {host.packets_sent}```"""
        )


# times ping time check command
@client.command()
async def tcheck(ctx, address="", count=2, interval=0.25, timeout=1):
    address, host = IO(address, count, interval, timeout)
    if not host:
        await ctx.channel.send(f"```ERROR: {address} could not be resolved```")
    else:
        await ctx.channel.send(
            f"""```
{address} is alive: {host.is_alive}
Packet times: {host.rtts}```"""
        )


# full ping time check command
@client.command()
async def fcheck(ctx, address="", count=2, interval=0.25, timeout=1):
    address, host = IO(address, count, interval, timeout)
    if not host:
        await ctx.channel.send(f"```ERROR: {address} could not be resolved```")
    else:
        await ctx.channel.send(
            f"""```
{address} is alive: {host.is_alive}
avgRTT: {host.avg_rtt}ms
minRTT: {host.min_rtt}ms
maxRTT: {host.max_rtt}ms
Jitter: {host.jitter}ms
Loss: {host.packet_loss}%
Sent: {host.packets_sent}
Recieved: {host.packets_received}
Packet times: {host.rtts}```"""
        )


# help command
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(colour=discord.Colour.blue())

    embed.set_author(name="Help")
    embed.add_field(
        name="Variables",
        value="""
Required: address (url or ipv4/6)
Optional: count, interval, and timeout
Defualt: 2, .25, 1
Maximum: 10, 2, 5""",
        inline=False,
    )
    embed.add_field(name=".check", value="Basic check up/down", inline=False)
    embed.add_field(
        name=".acheck",
        value="Average check up/down and average ping time",
        inline=False,
    )
    embed.add_field(
        name=".tcheck", value="Time check up/down and displays all pings", inline=False
    )
    embed.add_field(name=".lcheck", value="Loss check up/down and loss", inline=False)
    embed.add_field(
        name=".fcheck",
        value="Full check up/down, average, min, and max ping times",
        inline=False,
    )

    # send help message via pm
    # await author.send(author, embed=embed)
    # send help message chat
    await ctx.send(author, embed=embed)


# bot token stored in variable_lib.py
client.run(vl.TOKEN)
