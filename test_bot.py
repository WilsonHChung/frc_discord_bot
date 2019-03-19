import discord
import random
import config
from discord import Permissions
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="!")
#remove default help command
bot.remove_command("help")

# used to keep track of what teams the user is watching
role_names = []

# keeps track of team numbers
teams = []

@bot.command()
async def info(ctx):
    await ctx.send('FRC Discord Bot Info')
    info_msg = "Tracks FRC team information during regionals from thebluealliance.com"
    await ctx.send(info_msg)

@bot.command()
async def help(ctx):
    await ctx.send('FRC Discord Bot Commands')
    help_msg = "watch - displays a robotics team's stats including overall ranking, W/L ratio, and match " \
               + "unwatch - stops displaying stats"
    await ctx.send(help_msg)

@bot.command()
async def watch(ctx, arg):
    await ctx.send('Tracking FRC Stats!')

    team_number = arg
    watch_msg = "Now watching Team " + str(team_number)
    await ctx.send(watch_msg)

    # assigns member to a new role to categorize !watch command users
    role = await ctx.guild.create_role(name=str(team_number)+"_role")
    await ctx.message.author.add_roles(role)
    role_names.append(str(team_number)+"_role")

@bot.command()
async def unwatch(ctx, arg):
    await ctx.send('Stopped Tracking FRC Stats')

    team_number = arg
    watch_msg = "Now unwatching Team " + str(team_number)
    await ctx.send(watch_msg)

    for i in role_names:
        if i == str(team_number)+"_role":
            role = discord.utils.get(ctx.message.guild.roles, name=i)
            print(role)
            if role:
                await role.delete()

@bot.command()
async def unwatchall(ctx):
    await ctx.send('Stopped Tracking All FRC Stats')
        
    for i in role_names:
        role = discord.utils.get(ctx.message.guild.roles, name=i)
        print(role)
        if role:
            await role.delete()
    await ctx.send('All teams are now unwatched.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.version_info)

bot.run(config.DISCORD_TOKEN)
