import discord
from discord import app_commands, Intents, Client, Interaction
import asyncio
import time
from discord.ext import commands
# import requests




class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)


bot = Bot(intents=Intents.default())


@bot.event
async def on_ready():
    print(f"Conectado como: {bot.user}")


@bot.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")


@bot.tree.command()
async def profile(interaction: Interaction):
    user = interaction.user
    await interaction.response.send_message(f"Username: {user.name}\nAvatar URL: {user.avatar_url}\nAccount created at: {user.created_at}")



@bot.tree.command()
async def ban(interaction: Interaction, user: discord.Member, *, reason: str = None):
    await user.ban(reason=reason)
    await interaction.response.send_message(f"{user.name} ha sido baneado del servidor.")


# @bot.tree.command()
# async def stats(interaction: Interaction, username: str, game: str):
#    api_key = "your_api_key_here"
 #   url = f"https://api.example.com/stats/{game}/{username}?api_key={api_key}"
 #   response = requests.get(url)
 #   stats = response.json()
#    await interaction.response.send_message(f"Estadísticas de {username} en {game}: {stats}")


# @bot.tree.command()
# async def search(interaction: Interaction, query: str):
#   api_key = "your_api_key_here"
#  url = f"https://api.example.com/search?q={query}&api_key={api_key}"
#  response = requests.get(url)
#  results = response.json()
# image_url = results[0]["url"]
# await interaction.response.send_message(image_url)

@bot.tree.command()
async def ping(interaction: Interaction):
    try:
        print(interaction)  # Agrega esta línea para depurar el objeto interaction
        start_time = time.monotonic()
        msg = await interaction.response.send_message("Pong!")
        end_time = time.monotonic()
        await msg.edit(content=f"Pong! Latencia: {round((end_time - start_time) * 1000)}ms")
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")



@bot.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="a Andrés"
    )
    await bot.change_presence(activity=activity)

        


@bot.event
async def on_ready():
    print ('------')
    print('El bot está listo')
    print (bot.user.name)
    print (bot.user.id)
    print ('------')
    print('Conectado como: {0.user}'.format(bot))

while True:
    bot.run('Clave')


