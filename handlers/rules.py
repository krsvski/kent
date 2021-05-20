from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from typing import Union
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from loader import dp, db, bot
import time

from utils.keyboards.startKey import back
from utils.text.startText import rulesTex
from utils.files.startPic import rulesPic

@dp.callback_query_handler(text='rules')
async def rules(call: types.CallbackQuery):
    chat, mess = call.from_user.id, call.message.message_id
    await bot.edit_message_media(types.InputMediaPhoto(rulesPic, rulesTex), chat, mess, reply_markup=back)