import discord
from discord.ext import commands

from commands.slash import slash_help_command, slash_ping_command, slash_info_command, slash_serverinfo_command, make_it_admin

from commands.prefix import prefix_daily_command, prefix_profile_command
from games import casino, rpg

# GUILD_ID = discord.Object(id=1049689849436839987)  # SERVER ID

def setup(bot: commands.Bot):
    # Slash Commands
    @bot.tree.command(name="help", description="Show all commands!")
    async def help(interaction: discord.Interaction):
        await slash_help_command(interaction)

    @bot.tree.command(name="ping", description="What's her status?")
    async def ping(interaction: discord.Interaction):
        await slash_ping_command(bot, interaction)

    @bot.tree.command(name="info", description="Show bot information!")
    async def info(interaction: discord.Interaction):
        await slash_info_command(interaction)

    @bot.tree.command(name="serverinfo", description="Show server info!")
    async def serverinfo(interaction: discord.Interaction):
        await slash_serverinfo_command(interaction)

    @bot.tree.command(name="makeadmin", description="Memberikan role Admin (khusus owner bot ini).")
    async def makeadmin(interaction: discord.Interaction):
        await make_it_admin(interaction)

    # Prefix Commands
    @bot.command(name="daily")
    async def daily(ctx):
        await prefix_daily_command(ctx)

    @bot.command(name="profile")
    async def profile(ctx):
        await prefix_profile_command(ctx)

    @bot.command(name="slot")
    async def slot(ctx):
        await casino.slot_command(ctx)

    @bot.command(name="hunt")
    async def hunt(ctx):
        await rpg.hunt_command(ctx)