from discord.ext import commands
import random
from database.register import create_user  # Impor register_user

@commands.command()
async def slot(ctx):
    user_id = str(ctx.author.id)
    username = ctx.author.name

    # Auto register
    create_user(user_id, username)

    # Slot machine symbols
    symbols = ["🍎", "🍌", "🍒", "🍇", "🍊"]
    result = [random.choice(symbols) for _ in range(3)]

    # Check win condition
    if result[0] == result[1] == result[2]:
        await ctx.send(f"🎰 Kamu menang! Hasilnya: {''.join(result)}")
        # Update MongoDB (kamu dapat menambahkan update koin dan kemenangan di sini)
    else:
        await ctx.send(f"🎰 Kamu kalah! Hasilnya: {''.join(result)}")
        # Update MongoDB (kamu dapat menambahkan update koin dan kekalahan di sini)