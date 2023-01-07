import telebot
from see_all import *
from search_names import *
from new_contact import *


bot = telebot.TeleBot("5916857325:AAFg8c6yV39L51A1pThFWwxz6Kofs0IGx8I")


@bot.message_handler(commands=['start'])
def welcome_messages(message):
    text = 'Привет! Для поиска контакта введи /search\nДля просмотра всех контактов введи /see\n Для нового контакта введи /new'
    bot.reply_to(message, text)


@bot.message_handler(commands=['search'])
def get_text_messages(message):
    text = 'Введите имя для поиска контакта: '
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, make_search)


@bot.message_handler(commands=['see'])
def get_text_messages(message):
    text = see_all()
    bot.reply_to(message, text)
    with open("Log.txt", "a", encoding="utf-8") as data:
        data.write(f'Просмотрены все контакты; {time.asctime()}\n')


def make_search(message):
    s_name = message.text
    res = search_names(s_name)
    bot.send_message(message.chat.id, f'{res}\n')
    with open("Log.txt", "a", encoding="utf-8") as data:
        data.write(f'Поиск контакта {s_name}; {time.asctime()}\n')


@bot.message_handler(commands=['new'])
def get_new_contact(message):
    text = 'Введите Фамилию, Имя, телефон и описание через пробел: '
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, make_new_contact)


def make_new_contact(message):
    contact = message.text
    writing_csv(contact)
    bot.send_message(message.chat.id, 'Сделано =)')


bot.polling(none_stop=True)