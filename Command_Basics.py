import discord
import random  # Calling this for the coin flip command
from discord.ext import commands

# The "!" is so the bot can recognize a command string from the server chat
bot = commands.Bot(command_prefix="!")


# This function is the Ping-Pong command
@bot.command()
# This function responds to !ping with Pong!
async def ping(context):
    await context.send("Pong!")


# This function is the coin flip command
@bot.command()
async def coinflip(context):
    # Random integer and inside () is the set number limit
    num = random.randint(1, 2)
    # Outputting the results of the flip
    if num == 1:
        await context.send("Heads")
    if num == 2:
        await context.send("Tails")


# This function is the Rock/Paper/Scissors Command
@bot.command()
async def rps(context, hand):  # rps is Rock Paper Scissors, but short because command is typed by user
    hands = ["✌", "✋", "✊"]
    bot_hand = random.choice(hands)
    await context.send(bot_hand)

    # Logic for the Rock Paper Scissors roll
    if hand == bot_hand:
        await context.send("It's a Draw!")
    elif hand == "✌":
        if bot_hand == "✊":
            await context.send("I won!")
        if bot_hand == "✋":
            await context.send("You won 😞")
    elif hand == "✋":
        if bot_hand == "✌":
            await context.send("I won!")
        if bot_hand == "✊":
            await context.send("You won 😞")
    elif hand == "✊":
        if bot_hand == "✌":
            await context.send("I won!")
        if bot_hand == "✋":
            await context.send("You won 😞")

# This is running the bot with the token from the server.  The hashtags were added to keep discord from
# resetting my token.
bot.run("####OTcwNzI4MTEyOTkwMDg5MjQ2.GYOirs.OGpuiM4oXhwyH5ewsQkus0du9-YtmJkrvJgDJY")
