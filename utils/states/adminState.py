from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.dispatcher.filters.state import State

class Mailing(StatesGroup):
    Text = State()
    Confirm = State()