import sqlite3

import telebot
import sqlite3 as sl
from telebot import types
from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime
import config

token = config.TOKEN
bot = telebot.TeleBot(token)

# def CreateBase():
#     db = sl.connect('db.sqlite3')
#     sql = db.cursor()
#     sql.execute("""""")
def greeting(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton('Просмотр книг', callback_data='GetCard'),
        types.InlineKeyboardButton('Найти книгу', callback_data='FindBook')
    )
    bot.send_message(message.from_user.id, 'Введите /start для перехода к приветственному меню в любой момент времени. '
                                           'Выберите действие', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def messages(message):
    if message.chat.type == 'private':
        if message.text == '/start':
           greeting(message)
        else:
            bot.send_message(message.chat.id, "Извините, я Вас не понимаю")
            greeting(message)


def find_book(message):
    bot.reply_to(message, 'Введите название книги')  # Bot reply 'Введите текст'

    @bot.message_handler(content_types=['text'])  # Создаём новую функцию ,реагирующую на любое сообщение
    def message_input_step(message):
        db = sl.connect("db.sqlite3")
        sql = db.cursor()
        global text  # объявляем глобальную переменную
        text = message.text
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton('Buy', callback_data='Buy')
        )
        try:
            id = sql.execute(f'select id FROM mainapp_product where name="{text}"').fetchone()[0]
            path = sql.execute(f'SELECT image FROM mainapp_product where rowid={id}').fetchone()[0]
            name = sql.execute(f'SELECT name FROM mainapp_product where rowid={id}').fetchone()[0]
            description = sql.execute(f'SELECT description FROM mainapp_product where rowid={id}').fetchone()[0]
            price = sql.execute(f'SELECT price FROM mainapp_product where rowid={id}').fetchone()[0]
            author = sql.execute(
                f'select name FROM mainapp_author where id=(SELECT author_id FROM mainapp_product where rowid={id})').fetchone()[
                0]
            bot.send_photo(message.chat.id, open(f'media/{path}', 'rb'), caption=f"""
                Название: <b>{name}</b> \nАвтор: <b>{author}</b> \nОписание: <b>{description}</b>\nЦена: <b>{price}</b>""",
                           parse_mode="html", reply_markup=markup)
        except TypeError as _:
            bot.send_message(message.chat.id, 'Такой книги у нас нет(((')
            greeting(message)
    bot.register_next_step_handler(message, message_input_step)


SelectedCardId = 0


def GetCard(message):
    db = sl.connect("db.sqlite3")
    sql = db.cursor()
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton('<=== Back Item', callback_data='BackCard'),
        types.InlineKeyboardButton('Next Item ===>', callback_data='NextCard'),
        types.InlineKeyboardButton('Buy', callback_data='Buy')
    )
    id = SelectedCardId + 7
    path = sql.execute(f'SELECT image FROM mainapp_product where rowid={id}').fetchone()[0]
    name = sql.execute(f'SELECT name FROM mainapp_product where rowid={id}').fetchone()[0]
    description = sql.execute(f'SELECT description FROM mainapp_product where rowid={id}').fetchone()[0]
    price = sql.execute(f'SELECT price FROM mainapp_product where rowid={id}').fetchone()[0]
    author = sql.execute(f'select name FROM mainapp_author where id=(SELECT author_id FROM mainapp_product where rowid={id})').fetchone()[0]
    bot.send_photo(message.chat.id, open(f'media/{path}', 'rb'), caption=f"""
    Название: <b>{name}</b> \nАвтор: <b>{author}</b> \nОписание: <b>{description}</b>\nЦена: <b>{price}</b>""", parse_mode="html", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    db = sl.connect("db.sqlite3")
    sql = db.cursor()
    global SelectedCardId
    length = sql.execute("SELECT Count(*) FROM mainapp_product").fetchone()[0] - 1
    if call.data == 'GetCard':
        GetCard(call.message)
    elif call.data == 'NextCard':
        if SelectedCardId == length:
            return bot.send_message(call.message.chat.id, "Это последний товар")
        else:
            SelectedCardId += 1
            GetCard(call.message)
    elif call.data == 'BackCard':
        if SelectedCardId == 1:
            return bot.send_message(call.message.chat.id, "Это последний товар")
        else:
            SelectedCardId -= 1
            GetCard(call.message)
    elif call.data == 'FindBook':
        find_book(call.message)
    elif call.data == 'Buy':
        bot.reply_to(call.message, 'Введите адрес')  # Bot reply 'Введите текст'

        @bot.message_handler(content_types=['text'])  # Создаём новую функцию ,реагирующую на любое сообщение
        def message_input_step(message):
            db = sl.connect("db.sqlite3")
            sql = db.cursor()
            global text  # объявляем глобальную переменную
            text = message.text
            bot.reply_to(message, f'Ваш адрес: {message.text}')
            s = sql.execute(f'INSERT INTO tg_order (product_id, address) VALUES ({SelectedCardId + 7}, "{text}") ')
            db.commit()
            db.close()
            bot.send_message(call.message.chat.id, "Ожидайте получения товара на указанный адрес")
            greeting(message)
        bot.register_next_step_handler(call.message, message_input_step)


bot.polling()
