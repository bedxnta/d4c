import discord
import os
from commands import calc, avatar, rng, rcg, standinfo, define

bot_token = os.environ['TOKEN']

# Create a bot instance
bot = discord.Bot()

# Load all commands
calc.setup(bot)
avatar.setup(bot)
rng.setup(bot)
rcg.setup(bot)
standinfo.setup(bot)
# shorten.setup(bot)
define.setup(bot)

print("Bot is running...")
bot.run(bot_token)
