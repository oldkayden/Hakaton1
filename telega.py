import telebot
from telebot import types

import random

token = "6265736827:AAEjM1Oas4b-9x0yjCon3HC-W_WR15KmK2U"

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton("Play")
btn2 = types.KeyboardButton("Nope")
keyboard.add(btn1, btn2)


@bot.message_handler(commands=["start", "game"])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, "Welcome my friend! Let's star the game?", reply_markup=keyboard)

    bot.register_next_step_handler(bot_message, chek_answer)


def chek_answer(message):
    if message.text == "Play":
        bot.send_message(message.chat.id,
                         """Ok. Now look at rules of this game. You need to guess number what I guessed in range - 1 - 10! You have 3 lifes. If you lose I kill you!Good luck!(^з^)""")
#         number = random.randint(1, 10)
#         print(number, "!!!!!!!!")
#         game(message, 3, number)
#     elif message.text == "Nope":
#         bot.send_message(message.chat.id, "Go away and never come back!")
#     else:
#         bot_message = bot.send_message(message.chat.id, "What is this?", reply_markup=keyboard)
#         bot.register_next_step_handler(bot_message, chek_answer)
#
#
# def game(message, attemps, number):
#     message_bot = bot.send_message(message.chat.id, "Choice the number: ")
#     bot.register_next_step_handler(message_bot, chek_number, attemps - 1, number)
#
#
# def chek_number(message, attemps, number):
#     if message.text == str(number):
#         bot.send_message(message.chat.id, "You win! Lucky boy! (0___0)")
#     elif attemps == 0:
#         bot.send_message(message.chat.id, "You lose! I come for you!")
#     else:
#         bot.send_message(message.chat.id, "Wrong number, try again!")
#         game(message, attemps, number)
#
#
# bot.polling()
