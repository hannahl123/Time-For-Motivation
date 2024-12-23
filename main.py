# Link to invite the bot to your Discord server: https://discord.com/api/oauth2/authorize?client_id=937347049979006986&permissions=534723939392&scope=bot

import discord
import os
import json
import requests
import random
from discord.ext import commands
from discord.utils import find
from keep_alive import keep_alive

client = commands.Bot(command_prefix=".")
client.remove_command('help')

@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello! Type ?help to see the commands')

@client.command()
async def help(ctx):
  embed = discord.Embed(title="Commands", value="help command", color=0x64e8c3)
  # Daily command
  embed.add_field(name = ".daily", value = "Get the daily featured  quote")
  #Inspire command
  embed.add_field(name = ".inspire", value = "Generates a random inspirational quote")
  #Invite command
  embed.add_field(name = ".invite", value = "Instructions on inviting the bot to other servers")
  embed.add_field(name = "More commands in progress", value = "Visit later again to try them out!")
  await ctx.send(embed=embed)

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

@client.command()
async def code(ctx):
    await ctx.send("Here's the link to the code of this bot on Replit: https://replit.com/@hannahliu123/Time-For-Motivation#main.py")

@client.command()
async def hi(ctx):
  msg = f"Hello {ctx.author.mention}. Hope you're having a good day :)"
  await ctx.send(msg)

@client.command()
async def ping(ctx):
  await ctx.send("Pong! {}ms".format(round(client.latency * 1000)))

@client.command()
async def daily(ctx):
  reply = requests.get("https://zenquotes.io/api/today")
  json_data = json.loads(reply.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  embed = discord.Embed(title="Daily Featured Quotation", description=quote, color=discord.Colour.random())
  await ctx.send(embed=embed)

@client.command()
async def inspire(ctx):
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']
  embed = discord.Embed(title="Quotation by " + json_data[0]['a'], description=quote, color=discord.Colour.random())
  await ctx.send(embed=embed)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "sadness"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!",
  "You're better than you think!"
  "A positive mindset is more important than anything else."
  "Try your best and be happy."
]

@client.command()
async def on_message(message):
  if any(word in message for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

@client.command()
async def setdaily(ctx):
  channel_name = ctx.channel.mention
  await ctx.channel.send(f"You have set it up successfully. A random quote will be sent in {channel_name} daily.")

@client.command()
async def invite(ctx):
  link = "https://discord.com/api/oauth2/authorize?client_id=937347049979006986&permissions=534723939392&scope=bot"
  embed = discord.Embed(title="Invite the bot to another server!", value="invitelink", color=0x64e8c3)
  embed.add_field(name = "Option 1", value = f"Click this link to invite the bot to another server: {link}")
  embed.add_field(name = "Option 2", value = "OR click the bot profile to find the **Add to Server** button")
  await ctx.channel.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))