import discord

def setup(bot):
    @bot.slash_command(
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
        description="Fetches the avatar of a user."
    )
    async def avatar(ctx: discord.ApplicationContext, user: discord.User):
        embed = discord.Embed(
            title=f":frame_photo: {user.display_name}'s Avatar",
            color=discord.Color.blue()
        )
        embed.set_image(url=user.avatar.url)  # Adds the avatar as an image in the embed
        embed.set_footer(text="D4C 〣 Made by Cosmo (@bedxnta)")
        await ctx.respond(embed=embed)
        
