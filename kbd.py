from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оформить список литературы"),
        ],
        [
            KeyboardButton(text='Оформить курсовую работу')
        ],
        [
            KeyboardButton(text='Оформить титульный лист')
        ],
        [
            KeyboardButton(text='Информация об авторах')
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Что вам нужно?"
)

del_kb = ReplyKeyboardRemove()

end_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='В начало')
        ],
    ],
    resize_keyboard=True
)

tit_list_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Получить файл')
        ],
    ],
    resize_keyboard=True
)

litrature_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='издания до 4-ех авторов'),
            KeyboardButton(text='издания более 4-ех авторов')
        ],
        [
            KeyboardButton(text='эл. ресурсы удаленного доступа'),
            KeyboardButton(text='учебники и статьи')
        ],
    ],
    resize_keyboard=True
)
literature_more_1_author = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Один автор")
        ],
        [
            KeyboardButton(text="Два автора")
        ],
        [
            KeyboardButton(text="Три автора")
        ],
    ],
    resize_keyboard=True
)

