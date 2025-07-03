from discord.ext import commands

class Resources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.links = {
            "math": "https://www.khanacademy.org/math",
            "java": "https://www.w3schools.com/java/",
            "python": "https://www.geeksforgeeks.org/python-programming-language/",
            "dsa": "https://takeuforward.org/",
        }

    @commands.command()
    async def resources(self, ctx, subject: str):
        subject = subject.lower()
        if subject in self.links:
            await ctx.send(f'📚 Resource for {subject}: {self.links[subject]}')
        else:
            await ctx.send("❌ Subject not found. Try: math, java, python, dsa.")