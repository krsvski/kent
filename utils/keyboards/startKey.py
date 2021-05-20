from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

mark = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='⚽️Купить прогноз💵', callback_data='buyPrognoz')
        ], 
        [
            InlineKeyboardButton(text='Правила🧑🏼‍⚖️', callback_data='rules')
        ]
    ]
)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙Назад', callback_data='back_to_main')
        ]
    ]
)