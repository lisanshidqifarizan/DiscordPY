import discord
import datetime

async def slash_help_command(interaction):
    embed = discord.Embed(
        title="🆘 Help Menu",
        description="Here's what you need ( *^-^)ρ(^0^* )\n\n**Command List:**",
        color=discord.Color.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name="Slash Commands", value="`/ping`, `/info`, `/profile`", inline=False)
    embed.add_field(name="Prefix Commands", value="`vprofile`, `vrps`, `vslot`, `vbattle`, `vhunt`, `vtebakangka`", inline=False)
    await interaction.response.send_message(embed=embed)

async def slash_ping_command(bot, interaction):
    latency_ms = round(bot.latency * 1000)  # Convert latency ke ms (milisecond)
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"Here's the bot ping status:",
        color=discord.Color.green(),
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name="Latency", value=f"{latency_ms} ms", inline=False)
    if latency_ms < 100:
        embed.add_field(name="Status", value="✅ Excellent connection!", inline=False)
    elif latency_ms < 200:
        embed.add_field(name="Status", value="⚠️ Okay, a bit slow.", inline=False)
    else:
        embed.add_field(name="Status", value="❌ High latency! Check connection.", inline=False)
    await interaction.response.send_message(embed=embed)

async def slash_info_command(interaction):
    embed = discord.Embed(
        title="🤖 Bot Info", 
        description="Welcome to the multipurpose bot with fun features and a coin system!",
        color=discord.Color.light_embed(),
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(
        name="🎮 Minigame Features", 
        value="• Guess the Number\n• Rock Paper Scissors (RPS)\n• Slot Machine\n• Battle & Hunt", 
        inline=False
    )
    embed.add_field(
        name="💰 Coin System", 
        value="Collect coins by playing games and hunting!\nCheck your profile with `vprofile`.", 
        inline=False
    )
    embed.add_field(
        name="⚙️ Server Settings", 
        value="Set up special channels for bot features (e.g., gender channel).", 
        inline=False
    )
    embed.set_footer(text="Developed with ❤️ by Lisan")

    await interaction.response.send_message(embed=embed)

async def slash_serverinfo_command(interaction):
    server_name = interaction.guild.name  # Ambil nama server
    member_count = interaction.guild.member_count  # Ambil jumlah member

    embed = discord.Embed(
        title=f"📊 Server Info: {server_name}",
        description=f"Members: {member_count}",
        color=discord.Color.blurple(),
        timestamp=datetime.datetime.utcnow()
    )
    await interaction.response.send_message(embed=embed)