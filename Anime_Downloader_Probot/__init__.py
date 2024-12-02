import os
import time
import logging
from telethon import TelegramClient

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = os.environ.get("API_ID", "21740783")
API_HASH = os.environ.get("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
BOT_TOKEN = os.environ.get("TOKEN", "7766709030:AAEHnIF6EkNttAij4cOCZat74PMK5Ymm6is")

GogoAnime = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
