import telebot
from telebot import types
import random


bot = telebot.TeleBot('5675313094:AAGTfeobYhgw6qb9LvOTTxMFf_qR4X9SZ3E')

@bot.message_handler(commands=['start'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # (кроссплатформенность, кол-во в строке)

    generator = types.KeyboardButton("Сгенерировать новый пароль")  # кнопки в клавиатуре
    dev_tg = types.KeyboardButton("dev telegram")

    markup.add(generator, dev_tg)
    bot.send_message(message.chat.id, "Пользуйтесь кнопками снизу", reply_markup=markup)


@bot.message_handler()
def buttons(message):

    if message.text == 'dev telegram':
        bot.send_message(message.chat.id, "@SshorinsS", parse_mode='html')

    elif message.text == 'Сгенерировать новый пароль':
        lower_case = 'abcdefghijklmnopqrstuvwxyz'
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        special_simbols = '@#$%&*/\?'
        numbers = '0123456789'

        use_for = lower_case + upper_case + special_simbols + numbers
        length_for_pass = 16

        generated_pass = ''.join(random.sample(use_for, length_for_pass))

        mess = f'Твой новый пароль:\n<code>{generated_pass}</code>'
        bot.send_message(message.chat.id, mess, parse_mode='html')



bot.polling(none_stop=True)  # запуск бота


# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Привет, <b>{message.from_user.first_name}</b>!'
#     mess_2 = 'Введи команду /password чтобы сгенерировать новый пароль'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#     bot.send_message(message.chat.id, mess_2, parse_mode='html')


# @bot.message_handler(commands=['password'])
# def password(message):
#
#     lower_case = 'abcdefghijklmnopqrstuvwxyz'
#     upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     special_simbols = '@#$%&*/\?'
#     numbers = '0123456789'
#
#     use_for = lower_case + upper_case + special_simbols + numbers
#     length_for_pass = 16
#
#     generated_pass = ''.join(random.sample(use_for, length_for_pass))
#
#     mess = f'Твой новый пароль:\n<code>{generated_pass}</code>'
#     mess_2 = 'Нажми /password чтобы сгенерировать ещё!'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#     bot.send_message(message.chat.id, mess_2, parse_mode='html')


# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("telegram разработчика", url="sshorinss.t.me"))  # кнопка в сообщении
#     bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=markup)