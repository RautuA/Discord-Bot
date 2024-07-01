import discord
from discord.ext import commands
import youtube_dl
from discord import FFmpegOpusAudio
from apikeys import BOTTOKEN
import sys


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'noplaylist': 'True'
}

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='/', intents=intents, application_id= insert_your_aplication_id)
        
    async def setup_hook(self):
        try:
            await self.tree.sync()
            print("Slash commands synced globally")
        except discord.errors.Forbidden as e:
            print(f"Failed to sync slash commands due to missing permissions: {e}")
        except Exception as e:
            print(f"An error occurred during sync: {e}")

    async def on_member_join(self, member):
        channel = self.get_channel(insert your channel id)
        if channel:
            await channel.send(f"Hihi {member.mention}")

    async def on_member_remove(self, member):
        channel = self.get_channel(insert your channel id)
        if channel:
            await channel.send(f"pa {member.mention}")

    async def log_error(self, error_message: str):
        log_channel = self.get_channel(insert your channel id)  
        if log_channel:
            await log_channel.send(f"Error: {error_message}")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        await bot.tree.sync()
        print("Slash commands synced successfully globally.")
        print([command.name for command in bot.tree.get_commands()])
    except discord.errors.Forbidden as e:
        print(f"Failed to sync slash commands due to missing permissions: {e}")
    except Exception as e:
        print(f"An error occurred during sync: {e}")

@bot.tree.command(name="ping", description="Show bot latency")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    print(f"'ping' command used by {interaction.user}")
    await interaction.response.send_message(f'Bot latency is {latency}ms')

@bot.tree.command(name="leave", description="Leave the voice channel")
async def leave(interaction: discord.Interaction):
    if interaction.guild.voice_client:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("Disconnected")
    else:
        await interaction.response.send_message("Not connected to a voice channel")

@bot.tree.command(name="play", description="Play a YouTube music in a voice channel")
async def play(interaction: discord.Interaction, *, music_name: str):
    guild = interaction.guild
    voice_client = guild.voice_client
    
    if not voice_client:
        if interaction.user.voice:
            channel = interaction.user.voice.channel
            voice_client = await channel.connect()
        else:
            await interaction.response.send_message("You need to be in a voice channel to play music.")
            return
    
    await interaction.response.send_message(f"Searching for '{music_name}' on YouTube...")

    try:
        
        results = YoutubeSearch(music_name, max_results=1).to_dict()
        
        if results:
            video_url = f"https://www.youtube.com{results[0]['url_suffix']}"
            await interaction.response.send_message(f"Attempting to play '{results[0]['title']}'")

            try:
                with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(video_url, download=False)

                    if 'formats' in info and len(info['formats']) > 0:
                        format_url = info['formats'][0]['url']

                        try:
                            source = await discord.FFmpegOpusAudio.from_probe(format_url, **FFMPEG_OPTIONS)
                            voice_client.play(source)
                        except Exception as e:
                            error_message = f"Error creating FFmpegOpusAudio source: {e}"
                            await interaction.response.send_message(error_message)
                            print(error_message)
                            await bot.log_error(error_message)
                    else:
                        error_message = "No suitable formats found in the info dictionary"
                        await interaction.response.send_message(error_message)
                        print(error_message)
                        await bot.log_error(error_message)
            except youtube_dl.DownloadError as e:
                error_message = f"Download error: {e}"
                await interaction.response.send_message(error_message)
                print(error_message)
                await bot.log_error(error_message)
            except discord.errors.ClientException as e:
                error_message = f"Audio error: {e}"
                await interaction.response.send_message(error_message)
                print(error_message)
                await bot.log_error(error_message)
            except Exception as e:
                error_message = f"An error occurred: {e}"
                await interaction.response.send_message(error_message)
                print(error_message)
                await bot.log_error(error_message)
        else:
            await interaction.response.send_message(f"No results found for '{music_name}' on YouTube.")
    except Exception as e:
        error_message = f"An error occurred during YouTube search: {e}"
        await interaction.response.send_message(error_message)
        print(error_message)
        await bot.log_error(error_message)

bot.run(BOTTOKEN)
