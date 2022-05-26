import discord
import random  # Calling this for the coin flip command
from discord.ext import commands

# The "!" is so the bot can recognize a command string from the server chat
bot = commands.Bot(command_prefix="!")


@bot.command()
async def ping(context):
    await context.send("Pong!")


@bot.command()
async def coinflip(context):
    num = random.randint(1, 2)

    if num == 1:
        await context.send("Heads")
    if num == 2:
        await context.send("Tails")


bot.run("OTcwNzI4MTEyOTkwMDg5MjQ2.GYOirs.OGpuiM4oXhwyH5ewsQkus0du9-YtmJkrvJgDJY")
