import discord
import requests

def setup(bot):
    @bot.slash_command(
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
        description="Fetches information about a JoJo stand or user."
    )
    async def standinfo(
        ctx: discord.ApplicationContext, 
        search_type: discord.Option(str, "Choose to search for a stand or user.", choices=["stand", "user"]),
        query: str
    ):
        await ctx.defer()  # Acknowledge the interaction to prevent timeout

        try:
            if search_type == "stand":
                # Query Stand information
                api_url = f"https://stand-by-me.herokuapp.com/api/v1/stands/query/query?name={query}"
                response = requests.get(api_url)

                if response.status_code == 200 and response.json():
                    stand = response.json()[0]  # Get the first result

                    # Extract stand details
                    stand_name = stand.get("name", "Unknown")
                    user_id = stand.get("standUser", "Unknown")
                    abilities = stand.get("abilities", "Unknown")
                    japanese_name = stand.get("japaneseName", "Unknown")
                    battlecry = stand.get("battlecry", "None")
                    image_filename = stand.get("image", None)

                    # Fetch the stand user's name using the user ID
                    user_api_url = f"https://stand-by-me.herokuapp.com/api/v1/characters/{user_id}"
                    user_response = requests.get(user_api_url)

                    user_name = "Unknown User"
                    if user_response.status_code == 200:
                        user_data = user_response.json()
                        user_name = user_data.get("name", "Unknown User")

                    # Construct the full image URL for the stand
                    base_image_url = "https://jojos-bizarre-api.netlify.app/assets/"
                    image_url = f"{base_image_url}{image_filename}" if image_filename else None

                    # Create embed for stand information
                    embed = discord.Embed(
                        title=stand_name,
                        description=f"**Stand User**: {user_name}\n"
                                    f"**JP Name**: {japanese_name}\n"
                                    f"**Abilities**: {abilities}\n"
                                    f"**Battle Cry**: {battlecry}",
                        color=discord.Color.blue()
                    )

                    if image_url and isinstance(image_url, str) and image_url.startswith('http'):
                        embed.set_image(url=image_url)

                    # Add footer
                    embed.set_footer(text="Byte Crusader 〣 Made by Cosmo (@bedxnta)")

                    await ctx.respond(embed=embed)
                else:
                    await ctx.respond("Sorry, I couldn't find any stands matching that query.")
            elif search_type == "user":
                # Query User information
                user_api_url = f"https://stand-by-me.herokuapp.com/api/v1/characters/query/query?name={query}"
                user_response = requests.get(user_api_url)

                if user_response.status_code == 200 and user_response.json():
                    user_data = user_response.json()[0]  # Get the first result

                    # Extract user details
                    user_name = user_data.get("name", "Unknown")
                    family = user_data.get("family", "Unknown")
                    abilities = user_data.get("abilities", "Unknown")
                    jpname = user_data.get("japaneseName", "Unknown")
                    nationality = user_data.get("nationality", "Unknown")
                    image_filename = user_data.get("image", None)

                    # Construct the full image URL for the user
                    base_image_url = "https://jojos-bizarre-api.netlify.app/assets/"
                    image_url = f"{base_image_url}{image_filename}" if image_filename else None

                    # Create embed for user information
                    embed = discord.Embed(
                        title=user_name,
                        description=f"**JP Name**: {jpname}\n"
                                    f"**Family**: {family}\n"
                                    f"**Nationality**: {nationality}\n"
                                    f"**Abilities**: {abilities}",
                        color=discord.Color.green()
                    )

                    if image_url and isinstance(image_url, str) and image_url.startswith('http'):
                        embed.set_image(url=image_url)

                    # Add footer
                    embed.set_footer(text="Byte Crusader 〣 Made by Cosmo (@bedxnta)")

                    await ctx.respond(embed=embed)
                else:
                    await ctx.respond("Sorry, I couldn't find any users matching that query.")
        except Exception as e:
            await ctx.respond(f"An error occurred: {str(e)}")
