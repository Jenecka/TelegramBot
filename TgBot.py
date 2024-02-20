import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup
from aiogram.dispatcher import Command

bot = Bot(token="6828137414:AAGrFOHrYPeeIZ48oqOiE-xNdNxJVdS9sKY")
dispatcher = Dispatcher(bot=bot)

@dispatcher.message(Command('start'))
async def start(message: types.Message):
    await message.answer("UR started, check keyboard")
    kb = [
        [types.KeyboardButton(text="С пюрешкой")],
        [types.KeyboardButton(text="Без пюрешки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

async def main():
    await dispatcher.start_polling()

asyncio.run(main())
