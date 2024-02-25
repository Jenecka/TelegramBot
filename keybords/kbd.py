from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_kb = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="Оформить список литературы"),
        ],
        [
            KeyboardButton(text='Оформить курсовую работу')
        ],
        [
            KeyboardButton(text='Оформить титульный лист')
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вам нужно?"
)

del_kb = ReplyKeyboardRemove()

end_kb = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='В начало')
        ],
    ],
    resize_keyboard=True
)

tit_list_kb = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Получить файл')
        ],
    ],
    resize_keyboard=True
)