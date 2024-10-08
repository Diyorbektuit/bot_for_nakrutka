import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
REFERRAL_POINT = os.getenv('REFERRAL_POINT')
# Initialize bot and dispatcher

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

