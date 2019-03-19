import discord
import random
import config
from discord import Permissions
from discord.ext import commands
from discord.utils import get

bot = commands.Bot("!")

# used to keep track of what teams the user is watching
role_names = []

# keeps track of team numbers
teams = []

@bot.event
async def on_message(message):
    # prevents bot to responding to itself
    if message.author == bot.user:
        return

    # displays information of what the bot is
    if message.content.startswith('!info'):
        await bot.send_message(message.channel, 'FRC Discord Bot Info')
        info_msg = "Tracks FRC team information during regionals from thebluealliance.com"
        await bot.send_message(message.channel, info_msg)

    # displays information about how to use the text 
    if message.content.startswith('!help'):
        await bot.send_message(message.channel, 'FRC Discord Bot Commands')
        help_msg = "watch - displays a robotics team's stats including overall ranking, W/L ratio, and match " \
                   + "unwatch - stops displaying stats"
        await bot.send_message(message.channel, help_msg)

    # prints out basic team information
    if message.content.startswith('!watch '):
        await bot.send_message(message.channel, 'Tracking FRC Stats!')

        number = message.content.split(" ")
        team_number = int(number[1])
        watch_msg = "Now watching Team " + str(team_number)
        await bot.send_message(message.channel, watch_msg)

        # assigns member to a new role to categorize !watch command users
        role = await bot.create_role(message.server, name=str(team_number)+"_role", permissions=Permissions.all())
        await bot.add_roles(message.author, role)
        role_names.append(str(team_number)+"_role")

    # removes user from a role from watching their specified team
    if message.content.startswith('!unwatch '):
        await bot.send_message(message.channel, 'Stopped Tracking FRC Stats')

        number = message.content.split(" ")
        team_number = int(number[1])
        watch_msg = "Now unwatching Team " + str(team_number)
        await bot.send_message(message.channel, watch_msg)

        for i in role_names:
            if i == str(team_number)+"_role":
                role = discord.utils.get(message.server.roles, name=i)
                await bot.delete_role(message.server, role)        

    # removes user from all roles watching their assigned teams 
    if message.content.startswith('!unwatchall'):
        await bot.send_message(message.channel, 'Stopped Tracking All FRC Stats')
        
        for i in role_names:
            role = discord.utils.get(message.server.roles, name=i)
            await bot.delete_role(message.server, role)
        await bot.send_message(message.channel, 'All teams are now unwatched.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.version_info)

bot.run(config.DISCORD_TOKEN)
