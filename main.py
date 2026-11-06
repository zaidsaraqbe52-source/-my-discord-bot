import os
import discord

client = discord.Client(
    intents=discord.Intents.default()
)

@client.event
async def on_ready():
    print(f"Bot is online: {client.user}")

client.run(os.environ["DISCORD_TOKEN"])
