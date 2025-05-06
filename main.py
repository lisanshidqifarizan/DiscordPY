import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('FTOKEN')

class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f'Logged in as {self.user}!')

        try:
            synced = await self.tree.sync() # Sinkronisasi global
            print(f'Synced {len(synced)} global commands')
        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'[{message.author}]: {message.content}')
        await self.process_commands(message)

intents = discord.Intents.default()
intents.message_content = True
bot = Client(command_prefix='v', intents=intents)

# ✅ Load prefix & slash commands
from commands import prefix, slash
slash.setup(bot)
prefix.setup(bot)

bot.run(TOKEN)