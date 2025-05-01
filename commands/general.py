import discord
from discord import app_commands

# Ganti dengan server ID kamu (klik kanan server ➔ Copy ID)
GUILD_ID = 123456789012345678

def setup(bot: discord.Client):

    @bot.tree.command(name="ping", description="Check if the bot is alive", guild=discord.Object(id=GUILD_ID))
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! 🏓 Latency: {round(bot.latency * 1000)}ms")

    @bot.tree.command(name="info", description="Get bot information", guild=discord.Object(id=GUILD_ID))
    async def info(interaction: discord.Interaction):
        await interaction.response.send_message("🤖 I am Veodcpy Bot!\nMinigames & fun commands powered by Lisan!")

    @bot.tree.command(name="help", description="Show list of commands", guild=discord.Object(id=GUILD_ID))
    async def help_command(interaction: discord.Interaction):
        embed = discord.Embed(
            title="🆘 Help Menu",
            description="Here are the available commands:",
            color=discord.Color.blue()
        )
        embed.add_field(name="/ping", value="Check bot latency", inline=False)
        embed.add_field(name="/info", value="Get bot info", inline=False)
        embed.add_field(name="vprofile", value="Show your profile (coins, wins, losses)", inline=False)
        embed.add_field(name="vrps <choice>", value="Play Rock Paper Scissors", inline=False)
        embed.add_field(name="vhunt", value="Go hunting to earn coins", inline=False)
        embed.add_field(name="vbattle <@opponent>", value="Battle against another player", inline=False)
        await interaction.response.send_message(embed=embed)