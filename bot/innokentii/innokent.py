# coding=utf-8
import telebot
import config

from telebot import types
from rassilka import *

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome_start(message): bot.send_message(message.chat.id, 'Для начала работы напиши мне "Привет"')

@bot.message_handler(commands=['vsem'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message[message.text.find(' '):])

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, меня зовут Иннокентий, я - бот который поможет тебе с работой в CoddySchool! В 10:00 я отправлю тебе видео, а в 11:00 отправлю тест, обязательно посмотри!")

        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)

        key_no = types.InlineKeyboardButton(text='Хочу сейчас', callback_data='no')
        keyboard.add(key_no)

        bot.send_message(message.from_user.id, text='Такое время подходит?', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, 'Чтобы начать работу, нужно поздороваться. Напиши "Привет"')

    elif message.text == "/time":
        keyboard = types.InlineKeyboardMarkup()
        key_now = types.InlineKeyboardButton(text='Сейчас', callback_data='now')
        keyboard.add(key_now)
        bot.send_message(message.from_user.id, 'Нажми кнопку "Сейчас"', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'yes':
        answer = 'Отлично! Увидимся в назначенное время'
    elif call.data == 'no':
        answer = 'Введи команду /time'
    if call.data == 'now':
        answer = 'https://www.youtube.com/watch?v=-452p_9ESbM'
        bot.send_message(call.message.chat.id, 'https://konstruktortestov.ru/test-14061')
    bot.send_message(call.message.chat.id, answer)

bot.polling(none_stop=True, interval=0)
