from discord.ext import commands
from database.register import users_collection

@commands.command()
async def profile(ctx):
    user_id = str(ctx.author.id)
    user = users_collection.find_one({"user_id": user_id})

    if user:
        await ctx.send(f"📝 Profile of {user['username']}:\n"
                       f"Coins: {user['coins']}\n"
                       f"Wins: {user['wins']}\n"
                       f"Losses: {user['losses']}")
    else:
        await ctx.send("You are not registered yet. Play a game to auto register!")