import telebot
from telebot import types
import random

token = "6080430388:AAG_RR_CTHa3aS3w30QHUt5mCQ12UkAo2Ek"

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton("Играть")
btn2 = types.KeyboardButton("Нээт")
keyboard.add(btn1, btn2)


@bot.message_handler(commands=["start", "game"])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, "Добро пожаловать, мой друг! Начнем игру?", reply_markup=keyboard)

    bot.register_next_step_handler(bot_message, chek_answer)


def chek_answer(message):
    if message.text == "Играть":
        bot.send_message(message.chat.id,
                        """Хорошо. Теперь посмотрите на правила этой игры. Вам нужно угадать число, которое я задал в диапазоне - 1 - 10! У тебя есть 3 жизни. Если ты проиграешь, я убью тебя! Удачи!(^з^)""")
        number = random.randint(1, 10)
        print(number, "!!!!!!!!")
        game(message, 3, number)
    elif message.text == "Нээт":
        bot.send_message(message.chat.id, "Уходи и никогда не возвращайся!")
    else:
        bot_message = bot.send_message(message.chat.id, "Что это за нах?", reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, chek_answer)


def game(message, attemps, number):
    message_bot = bot.send_message(message.chat.id, "Выбирай цифру: ")
    bot.register_next_step_handler(message_bot, chek_number, attemps - 1, number)


def chek_number(message, attemps, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, "Ты выйграл красавчик, Удачи тебе! (0___0)")
    elif attemps == 0:
        bot.send_message(message.chat.id, "Ты проиграл! Я иду за тобой!")
    else:
        bot.send_message(message.chat.id, "Неверный номер, попробуйте еще раз!")
        game(message, attemps, number)


bot.polling()
