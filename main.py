import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from commands.minigames.rps import rps  # Importing Rock Paper Scissors game
from commands.minigames.slot import slot  # Importing Slot game
from commands.minigames.battle import battle, hunt  # Importing Battle game
from commands.minigames.tebakangka import tebakangka  # Importing Tebak Angka game
from commands.profile import profile

# Load .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Setup Discord Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="v", intents=intents)

# When bot is ready
@bot.event
async def on_ready():
    # Sync slash commands
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

    # Load slash commands
    from commands import general
    general.setup(bot)

# Register minigames
bot.add_command(rps)
bot.add_command(slot)
bot.add_command(battle)
bot.add_command(hunt)
bot.add_command(tebakangka)
bot.add_command(profile)

# Run the bot with the TOKEN from .env
bot.run(TOKEN)