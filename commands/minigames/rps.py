from discord.ext import commands
import os
from dotenv import load_dotenv
import random
from database.register import users_collection, create_user  # Import the users_collection

# Load .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Command: !rps (Rock Paper Scissors)
@commands.command()
async def rps(ctx, choice: str):
    user_id = str(ctx.author.id)
    username = ctx.author.name

    # Auto register
    create_user(user_id, username)

    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)

    choice = choice.lower()
    if choice not in choices:
        await ctx.send("Please choose rock, paper, or scissors!")
        return

    result = ""
    if choice == bot_choice:
        result = "It's a tie!"
    elif (choice == "rock" and bot_choice == "scissors") or \
         (choice == "paper" and bot_choice == "rock") or \
         (choice == "scissors" and bot_choice == "paper"):
        result = "You win!"
        users_collection.update_one({"user_id": user_id}, {"$inc": {"coins": 10, "wins": 1}})
    else:
        result = "You lose!"
        users_collection.update_one({"user_id": user_id}, {"$inc": {"coins": -5, "losses": 1}})

    await ctx.send(f"Bot chose **{bot_choice}**. {result}")