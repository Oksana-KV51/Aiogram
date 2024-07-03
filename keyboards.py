from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder #Inline-клавиатура. Builder

#Reply-кнопки
main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Тестовая кнопка 1")],
   [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)

main_dz = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет")],
   [KeyboardButton(text="Пока")]
], resize_keyboard=True)

# Пример главной клавиатуры
main_dz_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Каталог", callback_data="catalog")]
    ])


#Inline-кнопки
inline_keyboard_dz = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://www.youtube.com/watch?v=HfaIcB4Ogxkx>')],
   [InlineKeyboardButton(text="Музыка", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk>')],
   [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk')]
])

inline_keyboard_dz_d = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callbac_data='show_more')]
])

catalog = ["Опция 1", "Опция 2"]
async def dz_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test:
      keyboard.add(InlineKeyboardButton(text=key))
   return keyboard.adjust(2).as_markup()

#inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
 #  [InlineKeyboardButton(text="Видео", url='<https://www.youtube.com/watch?v=HfaIcB4Ogxk>')]
#])


#Inline-клавиатура. Builder
test = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4"]
async def test_keyboard():
   keyboard = ReplyKeyboardBuilder()
   for key in test:
      keyboard.add(KeyboardButton(text=key))
   return keyboard.adjust(2).as_markup()


async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test:
       keyboard.add(InlineKeyboardButton(text=key, url='<https://www.youtube.com/watch?v=HfaIcB4Ogxk>'))
   return keyboard.adjust(2).as_markup()



