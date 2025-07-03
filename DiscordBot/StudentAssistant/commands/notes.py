from discord.ext import commands

class Notes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.notes = {
            "oops": "🔹 OOPs includes: Encapsulation, Abstraction, Inheritance, Polymorphism.",
            "dbms": "🔹 DBMS: A system for managing and retrieving structured data efficiently.",
            "os": "🔹 OS: Manages hardware/software. Topics: Process, Threads, Memory, Scheduling.",
            "dsa": "🔹 DSA covers: Arrays, Linked Lists, Trees, Graphs, Stacks, Queues, Sorting/Searching.",
            "python": "🔹 Python: High-level, interpreted. Used for scripting, automation, ML, web dev.",
        }

    @commands.command()
    async def notes(self, ctx, topic: str):
        topic = topic.lower()
        if topic == "list":
            topics = ', '.join(self.notes.keys())
            await ctx.send(f"🗒️ Available topics: {topics}")
        elif topic in self.notes:
            await ctx.send(f'📝 Notes on **{topic}**:\n{self.notes[topic]}')
        else:
            await ctx.send("❌ Notes not found. Try `!notes list` to see available topics.")
