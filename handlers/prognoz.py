from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from typing import Union
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentTypes
from aiogram.types import CallbackQuery
from loader import dp, db, bot
import time

from utils.keyboards.paymentKey import payMark
from utils.text.profTex import priceT



pic = 'https://telegra.ph/file/50f392032e276fb1f3c4a.jpg'

@dp.callback_query_handler(text='buyPrognoz')
async def prognoz(call: types.CallbackQuery):
    chat, mess = call.from_user.id, call.message.message_id
    await bot.edit_message_media(types.InputMediaPhoto(pic, priceT), chat, mess, reply_markup=payMark)


@dp.callback_query_handler(text='back_to_pay')
async def back_to_pay(call: types.CallbackQuery):
    chat, mess = call.from_user.id, call.message.message_id
    await bot.send_photo(chat, pic, priceT, reply_markup=payMark)
    await bot.delete_message(chat, mess)
