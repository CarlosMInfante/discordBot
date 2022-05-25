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
# Trying a different way to comment in this one to see how I like it
@bot.event
async def on_member_join(member):
    guild = member.guild  # This is getting the channel name from the server and assigning it to the variable
    guild_name = guild.name  # This is the string of the server name
    dm_channel = await member.create_dm()  # Establish a connection between the user and the bot
    await dm_channel.send(f"Welcome to {guild_name}!")


# This event is for adding Marvel and/or DC roles
@bot.event
async def on_raw_reaction_add(payload):  # event is used because reaction is written before bot online
    emoji = payload.emoji.name
    member = payload.member
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)

    # Determine which reaction is used and which role to place the user
    if emoji == "🕷️" and message_id == 979021413514113034:
        role = discord.utils.get(guild.roles, name="Marvel Fan")
        await member.add_roles(role)

    if emoji == "🦇️" and message_id == 979021448490405958:
        role = discord.utils.get(guild.roles, name="DC Fan")
        await member.add_roles(role)


# This event is for removing the Marvel and/or DC role
@bot.event
async def on_raw_reaction_remove(payload):
    user_id = payload.user_id
    emoji = payload.emoji.name
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    member = guild.get_member(user_id)

    # Determine which reaction is used and which role to place the user
    if emoji == "🕷️" and message_id == 979021413514113034:
        role = discord.utils.get(guild.roles, name="Marvel Fan")
        await member.remove_roles(role)
    if emoji == "🦇️" and message_id == 979021448490405958:
        role = discord.utils.get(guild.roles, name="DC Fan")
        await member.remove_roles(role)

# This is running the bot with the token from the server.  The hashtags were added to keep discord from
# resetting my token.
bot.run("####OTcwNzI4MTEyOTkwMDg5MjQ2.GYOirs.OGpuiM4oXhwyH5ewsQkus0du9-YtmJkrvJgDJY")
