import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import  random

from gtts import gTTS
import os

from config import TOKEN, WEATHER_API_KEY
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

#создаём обработчик запросов callback
@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
   await callback.answer("Новости подгружаются", show_alert=True)
   await callback.message.answer('Вот свежие новости!')

#Inline-кнопки
@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.main) #kb.inline_keyboard_test   await kb.test_keyboard()  kb.main


#Reply-кнопки
@dp.message(F.text == "Тестовая кнопка 1")
async def test_button(message: Message):
   await message.answer('Обработка нажатия на reply кнопку')

#Inline-клавиатура. Builder

@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
   await callback.answer("Новости подгружаются", show_alert=True)
   await callback.message.edit_text('Вот свежие новости!')



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
