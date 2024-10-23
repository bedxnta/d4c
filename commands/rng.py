import discord
import random

def setup(bot):
    @bot.slash_command(
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
        description="Generates a random number between min and max."
    )
    async def rng(ctx: discord.ApplicationContext, min: int, max: int):
        if min > max:
            await ctx.respond("Error: Min cannot be greater than Max.")
        else:
            number = random.randint(min, max)
            embed = discord.Embed(
                title="Random Number Generator",
                description=f"Your random number between {min} and {max} is **{number}**",
                color=discord.Color.blue()
            )
            embed.set_footer(text="FA3RP 〣 Made by Cosmo (@bedxnta)")
            await ctx.respond(embed=embed)
