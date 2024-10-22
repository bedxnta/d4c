import discord
import requests

def setup(bot):
    @bot.slash_command(
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
        description="Define a word using either the dictionary or Urban Dictionary.")
    async def define(
        ctx: discord.ApplicationContext,
        query_type: discord.Option(str, "Choose source", choices=["dictionary", "urbandictionary"]),
        word: str
    ):
        try:
            if query_type == "dictionary":
                api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
                response = requests.get(api_url)

                if response.status_code == 200:
                    data = response.json()[0]
                    definition = data['meanings'][0]['definitions'][0]['definition']
                    example = data['meanings'][0]['definitions'][0].get('example', 'No example available.')

                    embed = discord.Embed(
                        title=f"Definition of {word}",
                        description=f"**Definition**: {definition}\n**Example**: {example}",
                        color=discord.Color.blue()
                    )
                    embed.set_footer(text="Byte Crusader 〣 Made by Cosmo (@bedxnta)")
                    await ctx.respond(embed=embed)
                else:
                    await ctx.respond(f"Could not find the word {word} in the dictionary.")

            elif query_type == "urbandictionary":
                api_url = f"http://api.urbandictionary.com/v0/define?term={word}"
                response = requests.get(api_url)

                if response.status_code == 200:
                    data = response.json()['list'][0]
                    definition = data['definition']
                    example = data.get('example', 'No example available.')

                    embed = discord.Embed(
                        title=f"Urban Definition of {word}",
                        description=f"**Definition**: {definition}\n**Example**: {example}",
                        color=discord.Color.orange()
                    )
                    embed.set_footer(text="Byte Crusader 〣 Made by Cosmo (@bedxnta)")
                    await ctx.respond(embed=embed)
                else:
                    await ctx.respond(f"Could not find the word {word} in Urban Dictionary.")

        except Exception as e:
            await ctx.respond(f"An error occurred: {str(e)}")
