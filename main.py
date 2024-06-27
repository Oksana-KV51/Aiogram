
import logging
import aiohttp
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, WEATHER_API_KEY
from aiogram import Bot, Dispatcher, F
import random

# Настройка логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

CITY_NAME = 'Moscow'  # Название города для прогноза погоды

# Функция для получения прогноза погоды
async def get_weather(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric&lang=ru'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if response.status == 200:
                weather = data['weather'][0]['description']
                temp = data['main']['temp']
                return f'Погода в городе {city_name}: {weather}, температура: {temp}°C'
            else:
                return 'Не удалось получить прогноз погоды. Проверьте название города.'


# Обработчик команды /weather
@dp.message(Command('weather'))
async def weather(message: Message):
    weather_report = await get_weather(CITY_NAME)
    await message.answer(weather_report)

@dp.message(F. text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

@dp.message(Command('image'))
async def image(message: Message):
    list = ['https://w.forfun.com/fetch/ec/ecff5e0bb65d194e4c17f8fee00d1ebe.jpeg', 'https://img.razrisyika.ru/kart/24/95248-kotiki-kartinki-18.jpg', 'https://koshka.top/uploads/posts/2021-12/1639894342_27-koshka-top-p-kotiki-na-rabochii-29.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

#Прописываем хендлер и варианты ответов:
@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды: \n /start \n /help \n /photo \n /weather \n /image")
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Приветики, я бот!')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
