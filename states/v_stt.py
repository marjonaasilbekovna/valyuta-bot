from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


valyut_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="USD 🇺🇸"),KeyboardButton(text="EUR 🇪🇺")],
        [KeyboardButton(text="RUB 🇷🇺"),KeyboardButton(text="JPY 🇯🇵")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Valyuta kurslarini ko'rish uchun valyutani tanlang"
)
