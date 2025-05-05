import discord
from discord.ext import commands
import datetime
# GUILD_ID = discord.Object(id=1049689849436839987)  # SERVER ID

def setup(bot: commands.Bot):
    @bot.tree.command(name="help", description="Show all commands!")
    async def help(interaction: discord.Interaction):
        embed = discord.Embed(
            title="🆘 Help Menu",
            description="Here's what you need ( *^-^)ρ(^0^* )\n\n**Command List:**",
            color=discord.Color.blue(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name="Slash Commands", value="`/ping`, `/info`, `/profile`", inline=False)
        embed.add_field(name="Prefix Commands", value="`vprofile`, `vrps`, `vslot`, `vbattle`, `vhunt`, `vtebakangka`", inline=False)
        await interaction.response.send_message(embed=embed)

    @bot.tree.command(name="ping", description="What's her status?")
    async def ping(interaction: discord.Interaction):
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

    @bot.tree.command(name="info", description="Show bot information!")
    async def info(interaction: discord.Interaction):
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

    @bot.tree.command(name="serverinfo", description="Show server info!")
    async def serverinfo(interaction: discord.Interaction):
        server_name = interaction.guild.name  # Ambil nama server
        member_count = interaction.guild.member_count  # Ambil jumlah member

        embed = discord.Embed(
            title=f"📊 Server Info: {server_name}",
            description=f"Members: {member_count}",
            color=discord.Color.blurple(),
            timestamp=datetime.datetime.utcnow()
        )
        await interaction.response.send_message(embed=embed)

    @bot.tree.command(name="mediainfo", description="Show all media examples!")
    async def mediainfo(interaction: discord.Interaction):
        embed = discord.Embed(
            title="📦 Media Example",
            description="Ini contoh lengkap penggunaan media di embed Discord!",
            color=discord.Color.gold(),
            timestamp=datetime.datetime.utcnow()
        )

        # ✅ Author (judul kecil di atas Title)
        embed.set_author(
            name=interaction.user.name,
            icon_url=interaction.user.display_avatar.url
        )

        # ✅ Thumbnail (gambar kecil di pojok kanan atas embed)
        embed.set_thumbnail(url="https://images2.alphacoders.com/947/thumb-1920-947457.jpg")

        # ✅ Gambar besar (tampil di bawah field)
        embed.set_image(url="https://images2.alphacoders.com/947/thumb-1920-947457.jpg")

        # ✅ Footer (catatan bawah)
        embed.set_footer(
            text="Developed by Lisan ❤️",
            icon_url=bot.user.display_avatar.url
        )
        await interaction.response.send_message(embed=embed)

    @bot.tree.command(name="joinvc", description="Join voice channel kamu!")
    async def joinvc(interaction: discord.Interaction):
        if interaction.user.voice:
            channel = interaction.user.voice.channel
            await channel.connect()
            await interaction.response.send_message(f"✅ Joined {channel.name}!", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Kamu harus join voice channel dulu!", ephemeral=True)