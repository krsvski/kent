import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from database import config
from database.database import Database
from database.commands import Data_comands

storage = MemoryStorage()

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
dt = Database()
db = Data_comands()