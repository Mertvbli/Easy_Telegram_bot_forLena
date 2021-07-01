import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("♥")
    item2 = types.KeyboardButton("😊 Как дела?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Категорически вас приветствую, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот создан, чтобы тебе помогать!".format(message.from_user, bot.get_me()),
                    parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def boto_govor(message):
    if message.chat.type == 'private':
        if message.text == "♥":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton("Конечно, я тебя 😘 очень сильно люблю!❤", callback_data='love')

            markup.add(item3)

            bot.send_message(message.chat.id, "Я ЛЮБЛЮ ТЕБЯ! А ты меня?", reply_markup=markup)

        elif message.text == "😊 Как дела?":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Потянет", callback_data='good')
            item2 = types.InlineKeyboardButton("Воняет", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Лена, с тобой всегда 12/10 А у тебя?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Прости, но я тупой :( Игорь меня больше ничему не научил. xD')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    sticker1 = open('static/good.webp', 'rb')
    sticker2 = open('static/bad.webp', 'rb')
    sticker3 = open('static/bad1.webp', 'rb')
    sticker4 = open('static/love.tgs', 'rb')
    try:
        if call.message:
            if call.data == 'love':
                bot.send_sticker(call.message.chat.id, sticker4)
            elif call.data == 'good':
                bot.send_sticker(call.message.chat.id, sticker1)
                bot.send_message(call.message.chat.id, 'Я рад это слышать!')
            elif call.data == 'bad':
                bot.send_sticker(call.message.chat.id, sticker2)
                bot.send_message(call.message.chat.id, 'Ну ты чё? Всё будет отлично у тебя! Ты же моя самая самая 🤪')
                bot.send_sticker(call.message.chat.id, sticker3)

    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)

