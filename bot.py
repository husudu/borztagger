from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN

bot = TelegramClient("borztagger", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)

bot.start()
bot.run_until_disconnected()
