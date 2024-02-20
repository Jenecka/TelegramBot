import telebot
from telebot import types

token = "6828137414:AAGrFOHrYPeeIZ48oqOiE-xNdNxJVdS9sKY"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Оформить литературу")
    button2 = types.KeyboardButton("Проверить орфографию")
    markup.add(button1, button2)
    bot.send_message(message.from_user.id, "Salam", reply_markup=markup) #тут была хуйня
# @bot.message_handler(commands=['button'])
# def button_message(message):
bot.infinity_polling()
