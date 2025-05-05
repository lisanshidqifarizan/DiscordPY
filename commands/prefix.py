import discord
from discord.ext import commands
import datetime
from database.profile import get_profile, update_profile
from games import casino, rpg

def setup(bot: commands.Bot):
    @bot.command(name="daily")
    async def daily(ctx):
        # ! PR PERLU NAMBAHIN HARIAN
        user_profile = get_profile(ctx.author.id)
        if not user_profile:
            await ctx.send(f"{ctx.author.mention}, kamu belum punya profile. Gunakan `vhunt` dulu!")
            return

        user_profile.coins += 50 # Tambah coins
        update_profile(user_profile) # Simpan perubahan ke database

        await ctx.send(f"{ctx.author.mention} kamu klaim hadiah harian dan mendapat 💰 **50 coins**! Total coins kamu sekarang: **{user_profile.coins}**!")

    @bot.command(name="slot")
    async def slot(ctx):
        await casino.slot_command(ctx)

    @bot.command(name="hunt")
    async def hunt(ctx):
        await rpg.hunt_command(ctx)

    @bot.command(name="profile")
    async def profile(ctx):
        user_profile = get_profile(ctx.author.id)
        if not user_profile:
            await ctx.send(f"{ctx.author.mention} kamu belum punya profile. Gunakan command `vhunt` dulu!")
            return

        profile_text = (
            f"Level: {user_profile.level}\n"
            f"HP: {user_profile.hp}\n"
            f"EXP: {user_profile.exp}\n"
            f"Attack: {user_profile.attack}\n"
            f"Defense: {user_profile.defense}\n"
            f"Coins: {user_profile.coins}"
        )

        # 🔥 Format equipments biar tampil rapi
        equip_text = ""
        for slot, item in user_profile.equipment.items():
            equip_text += f"- {slot.capitalize()}: {item if item else 'Kosong'}\n"

        embed = discord.Embed(
            title=f"{user_profile.username}",
            color=discord.Color.red(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url=f"{ctx.author.avatar.url}")
        embed.add_field(name="", value=profile_text, inline=False)

        await ctx.send(embed=embed)