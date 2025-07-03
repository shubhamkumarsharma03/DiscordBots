from discord.ext import commands

class Timetable(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.schedule = {
            "monday": "OS, DBMS, Python",
            "tuesday": "OOPs, DSA, DBMS",
            "wednesday": "OS, Java, DSA",
            "thursday": "DBMS, OOPs, Python",
            "friday": "DSA, OS, Project Lab"
        }

    @commands.command()
    async def timetable(self, ctx, day: str = None):
        if day is None:
            full = "**📅 Weekly Timetable**\n" + "\n".join(
                [f"**{d.title()}**: {subj}" for d, subj in self.schedule.items()]
            )
            await ctx.send(full)
        else:
            day = day.lower()
            if day in self.schedule:
                await ctx.send(f"**{day.title()}**: {self.schedule[day]}")
            else:
                await ctx.send("❌ Invalid day. Try Monday, Tuesday... or use `!timetable` for full schedule.")
