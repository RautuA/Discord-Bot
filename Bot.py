import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'hihi!')

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("---------------------")
    
@client.command()
async def hello(ctx):
    await ctx.send("hihi")
  



client.run('MTI1MjY5NTQ2ODU5Nzg0MTk5MA.G0eQOA.d2CO9g98NDszXnB-FS3ZxKohPwWp_yUDqGdCLQ')
