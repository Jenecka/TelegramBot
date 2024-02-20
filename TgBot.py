import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token="6828137414:AAGrFOHrYPeeIZ48oqOiE-xNdNxJVdS9sKY")
dispatcher = Dispatcher(bot=bot)

button1 = KeyboardButton(text="Оформить курсовую работу")
button2 = KeyboardButton(text="Оформить список литературы")
keyboard = ReplyKeyboardMarkup(keyboard=[[button1], [button2]], resize_keyboard=True)

@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("UR started, check keyboard", reply_markup=keyboard)

async def main():
    await dispatcher.start_polling()

asyncio.run(main())
