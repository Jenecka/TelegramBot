from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from keybords import kbd
user_private_router = Router()

@user_private_router.message(CommandStart())
async def button_start(message: types.message):
    await message.answer("Привет! Я бот, который поможет тебе с оформлением твоей курсовой работы)",
                         reply_markup=kbd.start_kb)

@user_private_router.message(F.text.lower() == 'оформить список литературы')
async def button_spis_ltr(message: types.message):
    await message.answer("Сбросьте файл формата docx для оформления списка литературы", reply_markup=kbd.end_kb)

@user_private_router.message(F.text.lower() == 'оформить курсовую работу')
async def button_kursach(message: types.message):
    await message.answer("Сбросьте файл формата docx для оформления курсовой работы", reply_markup=kbd.end_kb)

@user_private_router.message(F.text.lower() == 'в начало')
async def button_v_nachalo(message: types.message):
    await message.answer("Вы выбрали кнопку \"В начало\"",
                         reply_markup=kbd.start_kb)





@user_private_router.message()
async def cmd(message: types.Message):
    await message.answer('Пожалуйста, выберите корректный пункт меню.')