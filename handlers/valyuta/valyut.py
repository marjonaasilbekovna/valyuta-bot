from aiogram.types import Message
from loader import dp
from aiogram import F
from valyuta import get_val_malum

@dp.message(F.text == "USD 🇺🇸")
async def valyuta_usd(message:Message):
    natija = get_val_malum("USD")
    await message.answer(natija)

@dp.message(F.text == "EUR 🇪🇺")
async def valyuta_eur(message:Message):
    natija = get_val_malum("EUR")
    await message.answer(natija)

@dp.message(F.text == "RUB 🇷🇺")
async def valyuta_rub(message:Message):
    natija = get_val_malum("RUB")
    await message.answer(natija)

@dp.message(F.text == "JPY 🇯🇵")
async def valyuta_jpy(message:Message):
    natija = get_val_malum("JPY")
    await message.answer(natija)