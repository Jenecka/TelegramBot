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


# import telebot
# from telebot import types
#
# token = "6828137414:AAGrFOHrYPeeIZ48oqOiE-xNdNxJVdS9sKY"
# bot = telebot.TeleBot(token)
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton("Оформить литературу")
#     button2 = types.KeyboardButton("Проверить орфографию")
#     markup.add(button1, button2)
#     bot.send_message(message.from_user.id, "Salam", reply_markup=markup)
# # @bot.message_handler(commands=['button'])
# # def button_message(message):
# bot.infinity_polling()