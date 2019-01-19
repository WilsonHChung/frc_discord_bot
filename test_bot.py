import discord
import random
import config
from discord.ext import commands

client = discord.Client()

# assigns the bot to a role 
@client.event
async def member_join(member):
    role = discord.utils.get(member.server.roles, name='FRC')
    await client.add_roles(member, role)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # displays information about how to use the text 
    if message.content.startswith('!help'):
        await client.send_message(message.channel, 'FRC Discord Commands')
        help_msg = "watch - displays a robotics team's stats including overall ranking, W/L ratio, and match " + "unwatch - stops displaying stats"
        await client.send_message(message.channel, help_msg)
    

    # prints out basic team information
    if message.content.startswith('!watch '):
        await client.send_message(message.channel, 'Tracking FRC Stats!')

        number = message.content.split(" ")
        team_number = int(number[1])
        watch_msg = "Now watching Team " + str(team_number)
        await client.send_message(message.channel, watch_msg)

    # creates a new role to categorize !watch command users     


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.DISCORD_TOKEN)
