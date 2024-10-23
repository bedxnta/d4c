import discord
import random

def setup(bot):
    @bot.slash_command(
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
        description="Generates a random hex color."
    )
    async def rcg(ctx: discord.ApplicationContext):
        # Generate random hex color
        color_code = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        # Convert hex to RGB values
        r = int(color_code[1:3], 16)
        g = int(color_code[3:5], 16)
        b = int(color_code[5:7], 16)

        # Create the embed with color details
        embed = discord.Embed(
            title="Random Color Generator",
            description=f"**Generated Color**: `{color_code}`",
            color=int(color_code[1:], 16)  # Set the embed color to the generated color
        )

        # Add fields for RGB and hexadecimal values
        embed.add_field(name="Hex Code", value=color_code, inline=True)
        embed.add_field(name="RGB Values", value=f"RGB({r}, {g}, {b})", inline=True)

        # Optional: Image of the generated color
        color_image_url = f"https://singlecolorimage.com/get/{color_code[1:]}/200x200"
        embed.set_thumbnail(url=color_image_url)  # Display the color image on the side

        embed.set_footer(text="FA3RP 〣 Made by Cosmo (@bedxnta)")
        await ctx.respond(embed=embed)
