import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
from aiogram import Bot, Dispatcher, F
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

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
