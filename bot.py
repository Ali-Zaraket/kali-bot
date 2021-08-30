from discord import Client
from dotenv import load_dotenv
import os

#LOADING AND ASSIGNING CONSTANTS
load_dotenv()

# constants
BOT_TOKEN = os.getenv('TOKEN')
SERVER_ID = int(os.getenv('SERVER_ID'))
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))
CHAT_CHANNEL_ID = int(os.getenv("CHAT_CHANNEL_ID"))
MEMBER_COUNT_CHANNEL_ID = int(os.getenv("MEMBER_COUNT_CHANNEL_ID"))


class ServerBot(Client):
	async def on_ready(self):
		pass

	async def on_message(self, message):
		if message.author == self.user: return
		if message.content in ['hi', 'Hi', 'hello', 'Hello', 'HI', 'HELLO']:
			if message.channel.id == CHAT_CHANNEL_ID:
				await message.channel.send(f"Hello {message.author.mention}")

	async def on_member_join(self, member):
		if not member.bot:
			member_count_channel = self.get_channel(MEMBER_COUNT_CHANNEL_ID)
			await member_count_channel.edit(name=f"🔵 Members: {member_count_channel.guild.member_count}")

			channel = self.get_channel(WELCOME_CHANNEL_ID)
			await channel.send(f"Welcome to kali's server {member.mention} !")

	async def on_member_remove(self, member):
		member_count_channel = self.get_channel(MEMBER_COUNT_CHANNEL_ID)
		await member_count_channel.edit(name=f"🔵 Members: {member_count_channel.guild.member_count}")
