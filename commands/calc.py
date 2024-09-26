import discord
import math

# Custom safe eval function to support mathematical constants and functions
def safe_eval(expression):
    allowed_names = {
        'pi': math.pi,
        'e': math.e,
        'g': 9.80665,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'arcsin': math.asin,
        'arccos': math.acos,
        'arctan': math.atan,
        'sqrt': math.sqrt,
        'cbrt': lambda x: x ** (1/3),
        'log': math.log,  # natural logarithm
        'log10': math.log10,  # base-10 logarithm
    }

    # Only allow names in allowed_names
    code = compile(expression, "<string>", "eval")

    for name in code.co_names:
        if name not in allowed_names:
            raise ValueError(
                f"Use of '{name}' is not allowed. Available constants and functions: "
                f"{', '.join(allowed_names.keys())}"
            )

    return eval(code, {"__builtins__": {}}, allowed_names)

def setup(bot):
    @bot.slash_command(
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
        description="Simple calculator with support for constants and functions. Usage: /calc 2 + 2"
    )
    async def calc(ctx: discord.ApplicationContext, expression: str):
        try:
            # Evaluate the expression using the safe_eval function
            result = safe_eval(expression)
            embed = discord.Embed(
                title="Calculator",
                description=f"**Expression**: `{expression}`\n**Result**: `{result}`",
                color=discord.Color.green()
            )
            await ctx.respond(embed=embed)
        except ValueError as e:
            # If an unrecognized constant or function is used
            error_embed = discord.Embed(
                title="Error",
                description=f"{str(e)}",  # Display the list of available constants/functions in the error
                color=discord.Color.red()
            )
            await ctx.respond(embed=error_embed)
        except Exception as e:
            # For any other generic errors (syntax, etc.)
            error_embed = discord.Embed(
                title="Error",
                description=f"Invalid expression: {e}",
                color=discord.Color.red()
            )
            await ctx.respond(embed=error_embed)
