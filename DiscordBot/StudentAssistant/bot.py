import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

from commands.timetable import Timetable
from commands.notes import Notes
from commands.resources import Resources
from utils.memes import get_meme
from utils.quotes import get_quote

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ Register cogs inside on_ready (asynchronously)
@bot.event
async def on_ready():
    await bot.add_cog(Timetable(bot))
    await bot.add_cog(Notes(bot))
    await bot.add_cog(Resources(bot))
    print(f"✅ Bot is ready. Logged in as {bot.user}")
    print("📚 Cogs loaded: Timetable, Notes, Resources")

# ✅ Quote tag validator
def is_valid_tag(tag):
    valid_tags = ["inspire", "management", "sports", "life", "funny"]
    return tag in valid_tags

# ✅ Meme command
@bot.command()
async def meme(ctx):
    """Send a random meme."""
    await ctx.send(get_meme())

# ✅ Motivate command with optional tag
@bot.command()
async def motivate(ctx, tag: str = None):
    """
    Send a motivational quote. Optionally filter by tag.
    Usage: !motivate [tag]
    """
    if tag:
        tag = tag.lower()
        if not is_valid_tag(tag):
            await ctx.send("❌ Invalid tag. Try one of: inspire, management, sports, life, funny")
            return
    await ctx.send(get_quote(tag))

bot.run(TOKEN)
