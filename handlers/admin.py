from aiogram import types
from typing import Union
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from loader import dp, db, bot
import time

from utils.states.adminState import Mailing
from database.config import admin_id
from utils.keyboards.adminKey import adminMark, beforeSend, delMark

@dp.callback_query_handler(text='delete_message')
async def delete_message(call: types.CallbackQuery):
    chat, mess = call.from_user.id, call.message.message_id
    await bot.delete_message(chat, mess)

@dp.message_handler(user_id=admin_id, commands=['admin'])
async def admin_panel(message: types.Message):
    chat, mess = message.from_user.id, message.message_id
    await bot.send_message(chat, text='Админ панель!', reply_markup=adminMark)
    await bot.delete_message(chat, mess)

@dp.callback_query_handler(text='mailling')
async def mailling(call: types.CallbackQuery):
    await bot.edit_message_text("Отправь мне сообщение для рассылки!", call.from_user.id, call.message.message_id)
    await Mailing.Text.set()

@dp.message_handler(user_id=admin_id, state=Mailing.Text)
async def getMaillingMess(message: types.Message, state: FSMContext):
    chat, mess = message.from_user.id, message.message_id
    text = message.text
    await state.update_data (Text = text)
    print(text)
    await bot.delete_message(chat, mess)
    await bot.edit_message_text(text=f"Все ли правильно написано?\n\n{text}", chat_id=chat, message_id=mess-1, reply_markup=beforeSend)
    await Mailing.Confirm.set()

@dp.callback_query_handler(text='yesAllRight', state=Mailing.Confirm)
async def yesAllRight(call: types.CallbackQuery, state: FSMContext):
    chat, mess = call.from_user.id, call.message.message_id
    data = await state.get_data()
    text = data.get('Text')
    users = await db.getUsers()
    await bot.edit_message_text(text='Раcылка начнеться через 5 сек', chat_id=chat, message_id=mess)
    for user in users:
        coun = await db.get_counts(user[0])
        try:
            print(coun[0])
            if coun[0] == 1:
                await bot.send_message(text=f"{text}\n\nЭто твой последний прогноз🙁\nЧто бы получать новые прогнозы пополни счет!", chat_id=user[0], reply_markup=delMark)
                await db.countMinus(user[0])
                await db.setFalse(user[0])
                await bot.edit_message_text(text=f"Рассылка идет!\n\nОтправлено {users.index(user)+1} из {len(users)}", chat_id=chat, message_id=mess)
                time.sleep(2)
            else:
                print(coun)
                await bot.send_message(text=f"{text}\n\nУ тебя осталось {coun[0]-1} прогноза", chat_id=user[0], reply_markup=delMark)
                await db.countMinus(user[0])
                await bot.edit_message_text(text=f"Рассылка идет!\n\nОтправлено {users.index(user)+1} из {len(users)}", chat_id=chat, message_id=mess)
                time.sleep(2)
        except:
            pass
    await bot.edit_message_text(text=f'Раccылка оконченна!\n\nПрогноз отправлено {len(users)} людям', chat_id=chat, message_id=mess, reply_markup=delMark)
    await state.reset_state()
    

@dp.callback_query_handler(text='NoIsnt', state=Mailing.Confirm)
async def NoIsnt(call: types.CallbackQuery, state: FSMContext):
    print("This is not")
    await state.reset_state()
    chat, mess = call.from_user.id, call.message.message_id
    await bot.send_message(chat, text='Админ панель!', reply_markup=adminMark)
    await bot.delete_message(chat, mess)

