import logging
import aiohttp
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN, WEATHER_API_KEY
from aiogram import Bot, Dispatcher, F, types
import random

from gtts import gTTS # библиотека для озвучки
import os

from googletrans import Translator
translator = Translator()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

CITY_NAME = 'Samara'  # Название города для прогноза погоды

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
    await message.answer("Введите название города:")

@dp.message()
async def get_city_name(message: Message):
    city_name = message.text
    weather_report = await get_weather(city_name)
    await message.answer(weather_report)

#отправка видео
@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')# сообщение о загрузке видео в верху чата
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)

#отправка аудио
@dp.message(Command('audio'))
async def audio(message: Message):
    audio = FSInputFile('sound1.mp3')
    await bot.send_audio(message.chat.id, audio)

# озвучивание текста
@dp.message(Command('training'))
async def training(message: Message):
   training_list = [
       "Тренировка 1: \n1. Скручивания: 3 подхода по 15 повторений \n2. Велосипед: 3 подхода по 20 повторений (каждая сторона) \n3. Планка: 3 подхода по 30 секунд",
       "Тренировка 2: \n1. Подъемы ног: 3 подхода по 15 повторений \n2. Русский твист: 3 подхода по 20 повторений (каждая сторона) \n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
       "Тренировка 3: \n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений \n2. Горизонтальные ножницы: 3 подхода по 20 повторений \n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
   ]
   rand_tr = random.choice(training_list)
   await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")

   tts = gTTS(text=rand_tr, lang='ru')
   tts.save("training.ogg") #mp3
   audio = FSInputFile('training.ogg')#mp3
   await bot.send_voice(message.chat.id, audio) #audio
   os.remove("training.ogg")#mp3

# отправка голосового сообщения - sample.ogg
#@dp.message(Command('voice'))
#async def voice(message: Message):
   # voice = FSInputFile("sample.ogg")
    #await message.answer_voice(voice)

# отправка документа в pdf
@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile("TG02.pdf")
    await bot.send_document(message.chat.id, doc)

@dp.message(Command('image')) #, prefix='%'
async def image(message: Message):
    list = ['https://w.forfun.com/fetch/ec/ecff5e0bb65d194e4c17f8fee00d1ebe.jpeg',
            'https://img.razrisyika.ru/kart/24/95248-kotiki-kartinki-18.jpg',
            'https://koshka.top/uploads/posts/2021-12/1639894342_27-koshka-top-p-kotiki-na-rabochii-29.jpg'
    ]
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')


#Прописываем варианты ответов для полученных фото:
@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды: \n /start \n /help \n /photo \n /weather \n /image")
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Салют, {message.from_user.first_name}, как дела? Я бот!') #{message.from_user.full_name}

# ответ на любой запрос
#@dp.message()
#async def start(message: Message):
    #await message.answer("Приветики, я бот!")

#@dp.message(F. text == "что такое ИИ?")
#async def aitext(message: Message):
    #await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')
@dp.message()
#async def start(message: Message):
   # if message.text.lower() == 'test':
       # await message.answer('Тестируем')

#бот переводчик
@dp.message(F.text)
async def handle_text(message: Message):
    text_to_translate = message.text
    translated_text = translator.translate(text_to_translate, src='auto', dest='en').text
    await message.answer(translated_text)

#эхо бот
# #@dp.message()
#async def start(message: Message):
    #await message.send_copy(chat_id=message.chat.id)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
