from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

profMark = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='⚽️Купить прогноз💵', callback_data='buyPrognoz')
        ], 
        [
            InlineKeyboardButton(text='Обновить🔁', callback_data='reload'),
            InlineKeyboardButton(text='Правила🧑🏼‍⚖️', callback_data='rules')
        ]
    ]
)