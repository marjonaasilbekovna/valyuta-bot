from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from states.v_stt import valyut_button

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="Assalomu alaykum 😉\nValyuta botimizga hush kelibsiz 💱",  reply_markup=valyut_button)
    except:
        await message.answer(text="Assalomu alaykum 😉\nValyuta botimizga hush kelibsiz 💱",  reply_markup=valyut_button)
