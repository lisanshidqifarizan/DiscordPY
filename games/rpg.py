import random
import asyncio
from database.register import register_profile
from database.profile import get_profile, update_profile

async def hunt_command(ctx):
    user_profile = get_profile(ctx.author.id)
    
    if not user_profile:
        # Daftarkan dulu kalau belum ada profile
        user_profile = register_profile(ctx.author.id, ctx.author.name)
    
    await ctx.send(f"{ctx.author.mention} kamu mulai berburu... 🐾 Tunggu sebentar...")
    
    # Biar kayak proses beneran
    await asyncio.sleep(2)  # nunggu 2 detik biar dramatis
    
    # Random dapet reward
    coins_earned = random.randint(10, 50)
    exp_gained = random.randint(5, 15)
    
    # Update profile user (kamu tinggal buat fungsi update_profile di database-mu)
    user_profile.coins += coins_earned
    user_profile.exp += exp_gained
    update_profile(user_profile)  # ini simpan ke DB
    
    await ctx.send(
        f"🎯 {ctx.author.mention} selesai berburu!\n"
        f"🏅 Dapet **{coins_earned} coins** dan **{exp_gained} EXP**!\n"
        f"📊 (Sekarang: Level {user_profile.level}, Coins {user_profile.coins})"
    )
