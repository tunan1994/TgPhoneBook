import json
from main import*
from menu import *
from telegram import Update, Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN
import check


phonebook = {}
find_contact = []
number_contact = 0

def name(update, _):
    global phonebook
    if check.check_text(update, update.message.text):
        phonebook['name'] = (update.message.text).title()
        update.message.reply_text('Хорошо. Введите фамилию контакта')
        return surname
    else:
        return name

def surname(update, _):
    global phonebook
    if check.check_text(update, update.message.text):
        phonebook['surname'] = (update.message.text).title()
        update.message.reply_text('Хорошо. Введите номер контакта')
        return phone_number
    else:
        return surname

def phone_number(update, _):
    global phonebook
    if check.check_number(update, update.message.text):
        phonebook['phone_number'] = (update.message.text).title()
        update.message.reply_text('Хорошо. Теперь Описание контакта.')
        return comment
    else:
        return phone_number    

def comment(update, _):
    global phonebook
    if check.check_text(update, update.message.text):
        update.message.reply_text('Отлично. Ваш контакт сохранен в справочник')
        return menu.start(update, _)
    else:
        return comment
