import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery


import  random

from gtts import gTTS
import os

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

#создаём обработчик запросов callback
@dp.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
   await callback.answer('Каталог подгружается', show_alert=True)
   await callback.message.edit_text('Выберите из списка!', reply_markup=await kb.dz_keyboard())

# Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.main_dz_inline)

# Обработчик команды /links
@dp.message(Command('links'))
async def send_links(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=kb.inline_keyboard_dz)

# Обработчик команды /dynamic
@dp.message(Command('dynamic'))
async def send_dynamic(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=kb.inline_keyboard_dz_d)

#Reply-кнопки
# Обработчик кнопки "Привет"
@dp.message(F.text == "Привет")
async def salu_button(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

# Обработчик кнопки "Пока"
@dp.message(F.text == "Пока")
async def adu_button(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}!')

# Обработчик кнопки "Опция 1"
@dp.message(F.text == "Опция 1")
async def adu_button(message: Message):
    await message.answer(f'Сегодня, {message.from_user.first_name}, ты идешь в спортзал')

# Обработчик кнопки "Опция 2"
@dp.message(F.text == "Опция 2")
async def adu_button(message: Message):
    await message.answer(f'Сегодня, {message.from_user.first_name}, у тебя встреча с друзьями')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
