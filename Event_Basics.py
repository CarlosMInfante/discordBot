import discord
intents = discord.Intents.all()

# This allows communication with discord server
bot = discord.Client(intents=intents)

# This event is letting me know in the terminal that the bot is online
# The async lets code to be written out of order
@bot.event
async def on_ready():
    print("BOT IS ONLINE!")

# This event is taking in the user message
@bot.event
async def on_message(msg):
    # This is pulling the user's name from the server
    username = msg.author.display_name
    # This statement is used to the bot doesn't answer itself
    if msg.author == bot.user:
        return
    else:
        if msg.content == "hello":
            # await is set because send is a coroutine and is needed to be executed
            await msg.channel.send(f"hello, {username}.")

# This event is greeting the new user to the channel. In discord, the channel is called a "guild"
@bot.event
async def on_member_join(member):
    # This is getting the channel name from the server and assigning it to the variable
    guild = member.guild
    # This is the string of the server name
    guild_name = guild.name
    # Establish a connection between the user and the bot
    dm_channel = await member.create_dm()
    await dm_channel.send(f"Welcome to {guild_name}!")
# This is running the bot with the token from the server.  The hashtags were added to keep discord from
# resetting my token.
bot.run("####OTcwNzI4MTEyOTkwMDg5MjQ2.GYOirs.OGpuiM4oXhwyH5ewsQkus0du9-YtmJkrvJgDJY")