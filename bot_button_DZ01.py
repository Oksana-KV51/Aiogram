import asyncio
from aiogram import Bot, Dispatcher,F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN
import random

import keyboards_DZ as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.callback_query(F.data == 'info')
async def info(callback: CallbackQuery):
    await callback.answer("Информация подгужается", show_alert=True)
    await callback.message.edit_text(text='Показать больше', reply_markup= kb.inline_keyboard3)


@dp.message(F.text == "Привет")
async def test_button(message: Message):
    await message.answer(f'Приветики, {message.from_user.full_name}')

@dp.message(F.text == "Пока")
async def test_button(message: Message):
    await message.answer(f'Чау бамбино, {message.from_user.first_name}')



@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup= kb.main)

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f'Выберете сервер, {message.from_user.first_name}', reply_markup= kb.inline_keyboard)

@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer(f'Нажми на кнопку , {message.from_user.first_name} и выбере опцию', reply_markup= kb.inline_keyboard2)


@dp.message()
async def start(message: Message):
    await message.send_copy(chat_id=message.chat.id)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())