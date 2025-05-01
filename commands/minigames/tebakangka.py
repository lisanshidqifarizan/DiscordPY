from discord.ext import commands
import random
from database.register import create_user  # Impor register_user

# Fungsi untuk permainan Tebak Angka
@commands.command()
async def tebakangka(ctx):
        # Registrasi pengguna
    user_id = str(ctx.author.id)
    username = ctx.author.name
    create_user(user_id, username)  # Registrasi pengguna

    angka_rahasia = random.randint(1, 100)
    await ctx.send("Saya telah memilih angka antara 1 dan 100. Tebak angka saya!")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    while True:
        try:
            guess = await ctx.bot.wait_for('message', check=check, timeout=30.0)  # Gunakan ctx.bot
            user_guess = int(guess.content)

            if user_guess < angka_rahasia:
                await ctx.send("Tebakanmu terlalu rendah. Coba lagi!")
            elif user_guess > angka_rahasia:
                await ctx.send("Tebakanmu terlalu tinggi. Coba lagi!")
            else:
                await ctx.send(f"Selamat! Kamu berhasil menebak angka {angka_rahasia}.")
                break
        except ValueError:
            await ctx.send("Tolong masukkan angka yang valid.")
        except TimeoutError:
            await ctx.send("Waktu habis! Coba lagi lain waktu.")
            break