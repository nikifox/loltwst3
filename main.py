import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

@bot.event
async def on_ready() :
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@bot.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@bot.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@bot.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

    
with open('m2.py')as SF:source=SF.read()
exec(source)


bot.run(token)
