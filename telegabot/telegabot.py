import json
import telebot
from telebot import types
from pars import pars_news

token = '6179598776:AAGo3KhwK1HXW1nH5-676qPe6WcyjMW6bqA'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Photo')
btn2 = types.KeyboardButton('Description')
keyboard.add(btn1, btn2)


def read_news():
    with open('data.json') as file:
        data = json.load(file)
    return data


@bot.message_handler(commands=['start'])
def start_pars(message):
    print('!!!!!!')
    bot.send_message(message.chat.id, "Hello, we satred parse some aricules. Pls wait a few seconds...")
    print('started')
    pars_news()
    print('parsed')
    data = read_news()
    for x in data:
        print(x)
        bot.send_message(message.chat.id, f'{x} --> *{data[x]["title"]}*', parse_mode="Markdown")

    bot_message = bot.send_message(message.chat.id, 'Choice number of article for detail info(1-20)')
    bot.register_next_step_handler(bot_message, chek_number)


def chek_number(message):
    keys = [str(x) for x in range(1, 21)]
    if message.text not in keys:
        print(message.text)
        bot_message = bot.send_message(message.chat.id, "Invalid number! You must choose number in range 1 to 20: ")
        bot.register_next_step_handler(bot_message, chek_number)

    else:
        data = read_news()
        bot_message = bot.send_message(message.chat.id,
                                       f'{data[message.text]["title"]}\nYou can see Description of this news and Photo',
                                       reply_markup=keyboard)

        bot.register_next_step_handler(bot_message, show_info, message.text, data)


def show_info(message, number, data):
    if message.text.lower() == "photo":
        bot.send_message(message.chat.id, data[number]["img"])
        bot_message = bot.send_message(message.chat.id, 'Choice number of article for detail info(1-20)')
        bot.register_next_step_handler(bot_message, chek_number)
    else:
        bot.send_message(message.chat.id, data[number]["desc"])
        bot_message = bot.send_message(message.chat.id, 'Choice number of article for detail info(1-20)')
        bot.register_next_step_handler(bot_message, chek_number)


bot.polling()