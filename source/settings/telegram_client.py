from telethon import TelegramClient, events
from .settings import API_ID, APP_HASH, SESSION_PATH

telegram_clinet = TelegramClient(str(SESSION_PATH), API_ID, APP_HASH)
