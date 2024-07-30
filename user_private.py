from aiogram import F, types, Router
from aiogram.filters import CommandStart
from keybords import kbd

user_private_router = Router()
@user_private_router.message(CommandStart())
async def button_start(message: types.message):
    await message.answer("Привет! Я бот, который поможет тебе с оформлением твоей курсовой работы)",
                         reply_markup=kbd.start_kb)


@user_private_router.message(F.text.lower() == 'оформить курсовую работу')
async def button_kursach(message: types.message):
    await message.answer("Сбросьте файл формата docx для оформления курсовой работы", reply_markup=kbd.end_kb)


@user_private_router.message(F.text.lower() == 'информация об авторах')
async def button_kursach(message: types.message):
    await message.answer("3 парня - легенды АУППРБ,среди них:\n"
                         "Жендос(Библиотекарь) - книг на его полке больше, чем в библиотеке Петра |\n"
                         "Бугор - управляет командой и рулит движухой на районе\n"
                         "Шнапс - местный подпивасник", reply_markup=kbd.end_kb)


@user_private_router.message(F.text.lower() == 'в начало')
async def button_v_nachalo(message: types.message):
    await message.answer("Вы выбрали кнопку \"В начало\"",
                         reply_markup=kbd.start_kb)



