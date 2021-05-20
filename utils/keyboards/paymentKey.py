from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

payMark = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='5️⃣💲', callback_data='buy_one'),
            InlineKeyboardButton(text='1️⃣2️⃣💲', callback_data='buy_five'),
            InlineKeyboardButton(text='2️⃣0️⃣💲', callback_data='buy_ten')
        ], 
        [
            InlineKeyboardButton(text='🔙Назад', callback_data='back_to_main')
        ]
    ]
)

markone = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Заплатить 5 USD', pay=True)
        ],
        [
            InlineKeyboardButton(text='❌Закрыть', callback_data='back_to_pay')
        ]
    ]
)

markfive = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Заплатить 12USD', pay=True)
        ],
        [
            InlineKeyboardButton(text='❌Закрыть', callback_data='back_to_pay')
        ]
    ]
)

markten = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Заплатить 20USD', pay=True)
        ],
        [
            InlineKeyboardButton(text='❌Закрыть', callback_data='back_to_pay')
        ]
    ]
)
