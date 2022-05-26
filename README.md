# discordBot
This is where I will add steps that are not included in the comments.
For git help type: git <command> --help
Use this link for discord.py library https://discordpy.readthedocs.io/en/stable/

1: Make sure you install the library
  On Windows:
    Open up your Command Prompt (go the Windows Search Bar and type in "cmd")
    Type in this command: "py -3 -m pip install -U discord.py"
  On Mac:
    Open up your Terminal
    Type in "python3 -m pip install -U discord.py"
2: Go to link https://discord.com/developers/applications
    Click on "New Application" and name your bot.
    Click on the Bot tab and then add bot.
3: Make sure you copy the token and keep it private
    You will use this toke in the Event_Basics.py file in the bot.run()
4: Click on the OAuth2 tab
    Go to URL Generator tab
    Select bot and then give the bot the roles you want
    Copy link and paste into browser, then add bot to your server
    Open Discord and verify bot is in your server
5: In the Bot tab scroll to the "Privileged Gateway Intents" section
    Select the two tabs "Presence Intent" and "Server Members Intent"
6: To create the roles got to the discord server and select settings
    Select roles and then create them
