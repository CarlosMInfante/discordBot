import discord

# This allows communication with discord server
bot = discord.Client()

# This decorator is letting me know in the terminal that the bot is online
# The async lets code to be written out of order
@bot.event
async def on_ready():
    print("BOT IS ONLINE!")


# This is running the bot with the token from the server.  The hashtags were added to keep discord from
# resetting my token.
bot.run("####OTcwNzI4MTEyOTkwMDg5MjQ2.GYOirs.OGpuiM4oXhwyH5ewsQkus0du9-YtmJkrvJgDJY")