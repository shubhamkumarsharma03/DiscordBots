import discord
import requests
import json
import os
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Function to get meme from API
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

# Custom client class
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

        if message.content.startswith('$meme'):
            meme_url = get_meme()
            await message.channel.send(meme_url)

# Enable message content intent
intents = discord.Intents.default()
intents.message_content = True

# Start the bot
client = MyClient(intents=intents)
client.run(TOKEN)
