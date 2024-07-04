import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery


import  random

from gtts import gTTS
import os

from config import TOKEN
import keyboardsdz as kbz

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kbz.main_dz)

# Обработчик команды /links
@dp.message(Command('links'))
async def send_links(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=kbz.inline_keyboard_dz)


# Reply-кнопки
# Обработчик кнопки "Привет"
@dp.message(F.text == "Привет")
async def salu_button(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

# Обработчик кнопки "Пока"
@dp.message(F.text == "Пока")
async def adu_button(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}!')

# Обработчик команды /dynamic
@dp.message(Command('dynamic'))
async def send_dynamic_keyboard(message: Message):
    await message.answer("Нажмите кнопку ниже:", reply_markup=kbz.inline_keyboard_dz_d)

# Обработчик callback запроса для кнопки "Показать больше"
@dp.callback_query(F.data == 'show_more')
async def show_more_options(callback_query: CallbackQuery):
    await bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id, reply_markup=kbz.keyboard)

# Обработчик callback запроса для кнопок "Опция 1" и "Опция 2"
@dp.callback_query(F.data.startswith('option_'))
async def handle_option(callback_query: CallbackQuery):
    selected_option = callback_query.data.split('_')[1]
    if selected_option == '1':
        await bot.send_message(callback_query.message.chat.id, "Вы выбрали Опция 1")
    elif selected_option == '2':
        await bot.send_message(callback_query.message.chat.id, "Вы выбрали Опция 2")
    await bot.answer_callback_query(callback_query.id)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
