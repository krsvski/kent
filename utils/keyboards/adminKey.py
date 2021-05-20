from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

adminMark = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассылка', callback_data='mailling')
        ],
        [
            InlineKeyboardButton(text='❌Закрыть', callback_data='delete_message')
        ]
    ]
)

beforeSend = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅', callback_data='yesAllRight'),
            InlineKeyboardButton(text='❌', callback_data='NoIsnt')
        ]
    ]
)

delMark = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='❌Закрыть', callback_data='delete_message')
        ]
    ]
)