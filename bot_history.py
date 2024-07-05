import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import aiohttp
from googletrans import Translator
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()

FACT_TYPES_TRANSLATION = {
    'trivia': 'факт из жизни',
    'math': 'математический факт',
    'date': 'факт о дате',
    'year': 'факт о годе'
}

async def fetch_fact(fact_type: str) -> str:
    url = f'http://numbersapi.com/random/{fact_type}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def translate_text(text: str, dest_language: str = 'ru') -> str:
    translation = translator.translate(text, dest=dest_language)
    return translation.text

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот 'Этот день в истории'. Пожалуйста, выберите тип факта:\n"
                         "1. trivia — факт из жизни\n"
                         "2. math — математический факт\n"
                         "3. date — факт о дате (в формате MM/DD)\n"
                         "4. year — факт о годе")

@dp.message(Command("fact"))
async def fact_command(message: Message):
    await message.answer("Введите тип факта (trivia, math, date, year):")

@dp.message()
async def handle_fact_type(message: Message):
    fact_type = message.text.lower()
    if fact_type not in ['trivia', 'math', 'date', 'year']:
        await message.answer(
            "Неверный тип факта. Пожалуйста, введите один из следующих типов: trivia, math, date, year.")
        return

    fact = await fetch_fact(fact_type)
    translated_fact = await translate_text(fact)
    translated_fact_type = FACT_TYPES_TRANSLATION.get(fact_type, fact_type)
    await message.answer(f"{translated_fact_type.capitalize()}: {translated_fact}")


async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())