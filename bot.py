from telebot import util
from main import Car
from random import choice
from config import TOKEN

import telebot

bot = telebot.TeleBot(TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['car'])
def create_car(message):
    car = Car()
    bot.reply_to(message, "Вы создали автомобиль:" + car.info())


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(commands=['car'])
def car_handler(message):
    # Получаем аргументы команды: цвет и марку
    args = util.extract_arguments(message.text).split()

    if len(args) < 2:
        bot.reply_to(
            message,
            "❗ Используй команду так:\n/car цвет марка\n"
        )
        return

    color = args[0]
    brand = " ".join(args[1:])

    car = Car(color, brand)

    bot.send_message(message.chat.id, car.info()) 


bot.infinity_polling()