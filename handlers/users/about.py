from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Hurmatli foydalanuvchi \nBu bot yordamida siz osonlik bilan valyuta kurslarini kuzatib borishingiz va eng dolzarb ma'lumotlarni olishingiz mumkin.\n\nBot admini bilan bog'lanish uchun /xabar tugmasini bosing \nyordam uchun /help tugmasini bosing")

