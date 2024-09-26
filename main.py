import discord

# debug_guilds must not be set if we want to set contexts and integration_types on commands
import discord
import os
from commands import calc, avatar, rng, rcg, standinfo, define

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

bot.run("ENTER TOKEN")
