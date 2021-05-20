from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from typing import Union
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from loader import dp, db, bot
import time

from utils.files.startPic import startPic
from utils.keyboards.startKey import mark
from utils.text.startText import text
from utils.files.profilePic import prof
from utils.keyboards.profileKey import profMark
from utils.text.profTex import profT

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.from_user.id
    mess = message.message_id
    status = await db.subscriptions_exist(chat_id)
    if await db.sub_exist(chat_id) == False:
        await db.add_user(chat_id, message.from_user.full_name)
        await bot.send_photo(chat_id, photo=startPic, caption=text, reply_markup=mark)
        await bot.delete_message(chat_id, mess)
    elif status[0] == False:
        await bot.send_photo(chat_id, photo=startPic, caption=text, reply_markup=mark)
        await bot.delete_message(chat_id, mess)
    else: 
        num = await db.get_counts(message.from_user.id)
        await bot.send_photo(chat_id, prof, profT.format(message.from_user.full_name, num[0]), reply_markup=profMark)
        await bot.delete_message(chat_id, mess)

@dp.callback_query_handler(text='back_to_main')
async def back_to_main(call: types.CallbackQuery):
    chat, mess = call.from_user.id, call.message.message_id
    status = await db.subscriptions_exist(chat)
    num = await db.get_counts(chat)
    if status[0] == False:
        await bot.edit_message_media(types.InputMediaPhoto(startPic, text), chat, mess, reply_markup=mark)
    else:
        await bot.edit_message_media(types.InputMediaPhoto(prof, profT.format(call.from_user.full_name, num[0])), chat, mess, reply_markup=profMark)

@dp.callback_query_handler(text='delete_message')
async def back_to_main(call: types.CallbackQuery):
    chat, mess = call.from_user.id, call.message.message_id
    await bot.delete_message(chat, mess)

@dp.callback_query_handler(text='reload')
async def reload_prof(call: types.CallbackQuery):
    chat, mess = call.from_user.id, call.message.message_id
    num = await db.get_counts(chat)
    try:
        await bot.edit_message_media(types.InputMediaPhoto(prof, profT.format(call.from_user.full_name, num[0])), chat, mess, reply_markup=profMark)
    except:
        await bot.answer_callback_query(call.id, text=f'Обновлено✅\n\nКогда прогноз будет готов я тебе напишу\n\nОсталось прогнозов: {num[0]}', show_alert=True)