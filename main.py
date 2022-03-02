```import discord
import asyncio
import colorama
import json
from discord.ext import commands
import os 


client = commands.Bot(command_prefix="owo ",intents = discord.Intents.all())

token = "Your Bot token"

@client.command(pass_context=True)
async def cash(ctx):
  await ctx.send("💳 | **YouraccountName**, you currently have **__4,645,371__** cowoncy")
  
@client.command(pass_context=True)
async def give(ctx, arg1, arg2):
  await ctx.send('💳 | **YouraccountName*** sent **{}** cowoncy to **{}**!'.format(arg2, arg1))
 
client.run(token);

```
