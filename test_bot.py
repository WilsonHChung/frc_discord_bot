import discord
import random
import config
from discord import Permissions
from discord.ext import commands
from discord.utils import get

client = discord.Client()

# used to keep track of what teams the user is watching
role_names = []

@client.event
async def on_message(message):
    # prevents bot to responding to itself
    if message.author == client.user:
        return

    # displays information about how to use the text 
    if message.content.startswith('!help'):
        await client.send_message(message.channel, 'FRC Discord Commands')
        help_msg = "watch - displays a robotics team's stats including overall ranking, W/L ratio, and match " \
                   + "unwatch - stops displaying stats"
        await client.send_message(message.channel, help_msg)

    # prints out basic team information
    if message.content.startswith('!watch '):
        await client.send_message(message.channel, 'Tracking FRC Stats!')

        number = message.content.split(" ")
        team_number = int(number[1])
        watch_msg = "Now watching Team " + str(team_number)
        await client.send_message(message.channel, watch_msg)

        # assigns member to a new role to categorize !watch command users
        role = await client.create_role(message.server, name=str(team_number)+"_role", permissions=Permissions.all())
        await client.add_roles(message.author, role)
        role_names.append(str(team_number)+"_role")

    if message.content.startswith('!unwatchall'):
        await client.send_message(message.channel, 'Stopped Tracking FRC Stats')
        for i in role_names:
            # await client.remove_role(message.author, i)
            await client.send_message(message.channel, 'Unfollowed')
            # print(i)

        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(discord.version_info)

client.run(config.DISCORD_TOKEN)
