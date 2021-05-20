from aiogram import types
from typing import Union
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentTypes
from aiogram.types import CallbackQuery
from loader import dp, db, bot
import time
from utils.keyboards.paymentKey import payMark, markone, markfive, markten
from database.config import PAYMENTS_PROVIDER_TOKEN, admin_id
from utils.files.profilePic import prof
from utils.keyboards.profileKey import profMark
from datetime import datetime, date, time


pricesOne = [
    types.LabeledPrice(label='1 прогноз', amount=15000),
]
pricesFive = [
    types.LabeledPrice(label='3 прогноза', amount=30000),
]
pricesTen = [
    types.LabeledPrice(label='5 прогнозов', amount=50000),
]


@dp.callback_query_handler(text='buy_one')
async def put_money1(call: types.CallbackQuery):
    chat, mess = call.from_user.id, call.message.message_id
    dt = datetime.now()
    tmp = 1
    await db.tmpCount(tmp, chat)
    await bot.send_invoice(call.from_user.id, title='Прогнозы 1шт',
                        description=f'Дата покупки: {dt.day}/{dt.month}/{dt.year}',
                        provider_token=PAYMENTS_PROVIDER_TOKEN,
                        currency='UAH',
                        photo_url='https://telegra.ph/file/2ee27a01104bb477e6e92.png',
                        photo_height=512,  # !=0/None or picture won't be shown
                        photo_width=512,
                        photo_size=256,
                        is_flexible=False,  # True If you need to set up Shipping Fee
                        prices=pricesOne,
                        start_parameter='startParametrForKent',
                        payload='byedOnePrognoz', 
                        reply_markup=markone)
    await bot.delete_message(chat, mess)

@dp.callback_query_handler(text='buy_five')
async def put_money3(call: types.CallbackQuery):
    dt = datetime.now()
    chat, mess = call.from_user.id, call.message.message_id
    tmp = 3
    await db.tmpCount(tmp, chat)
    await bot.send_invoice(call.from_user.id, title='Прогнозы 3шт',
                        description=f'Дата покупки: {dt.day}/{dt.month}/{dt.year}',
                        provider_token=PAYMENTS_PROVIDER_TOKEN,
                        currency='UAH',
                        photo_url='https://telegra.ph/file/2ee27a01104bb477e6e92.png',
                        photo_height=512,  # !=0/None or picture won't be shown
                        photo_width=512,
                        photo_size=256,
                        is_flexible=False,  # True If you need to set up Shipping Fee
                        prices=pricesFive,
                        start_parameter='startParametrForKent',
                        payload='byedTreePrognoz',
                        reply_markup=markfive)
    await bot.delete_message(chat, mess)

@dp.callback_query_handler(text='buy_ten')
async def put_money5(call: types.CallbackQuery):
    dt = datetime.now()
    chat, mess = call.from_user.id, call.message.message_id
    tmp = 5
    await db.tmpCount(tmp, chat)
    await bot.send_invoice(call.from_user.id, title='Прогнозы 5шт',
                        description=f'Дата покупки: {dt.day}/{dt.month}/{dt.year}',
                        provider_token=PAYMENTS_PROVIDER_TOKEN,
                        currency='UAH',
                        photo_url='https://telegra.ph/file/2ee27a01104bb477e6e92.png',
                        photo_height=512,  # !=0/None or picture won't be shown
                        photo_width=512,
                        photo_size=256,
                        is_flexible=False,  # True If you need to set up Shipping Fee
                        prices=pricesTen,
                        start_parameter='startParametrForKent',
                        payload='byedFivePrognoz',
                        reply_markup=markten)
    await bot.delete_message(chat, mess)


@dp.pre_checkout_query_handler(lambda query: True)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                        error_message="Упс. Что-то пошло не так!\nПопробуй еще раз через несколько минут.")

@dp.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
async def got_payment(message: types.Message):
    numn = await db.get_counts(message.from_user.id)
    coun = await db.getTmp(message.from_user.id)
    count = numn[0] + coun[0]
    await db.add_counts(count, message.from_user.id)
    num = await db.get_counts(message.from_user.id)
    await db.setTrue(message.from_user.id)
    await bot.send_photo(message.from_user.id, photo=prof, caption=f'{message.from_user.full_name}\n\nПрогнозов осталось: {num[0]}', reply_markup=profMark)
    await bot.delete_message(message.from_user.id, message.message_id-1)
