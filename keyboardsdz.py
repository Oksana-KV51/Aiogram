from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder #Inline-клавиатура. Builder


main_dz = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет")],
   [KeyboardButton(text="Пока")]
], resize_keyboard=True)


# Клавиатура для динамического изменения
inline_keyboard_dz_d = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Показать больше', callback_data='show_more')

)

# Клавиатура, которая будет показана после нажатия "Показать больше"
keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Опция 1", callback_data='option_1'),
    InlineKeyboardButton("Опция 2", callback_data='option_2')
)


#Inline-кнопки
inline_keyboard_dz = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://www.youtube.com/watch?v=HfaIcB4Ogxkx>')],
   [InlineKeyboardButton(text="Музыка", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk>')],
   [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk')]
])





