from config import TOKEN
import menu
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    ConversationHandler,
)


# Определяем константы этапов разговора
Main_menu, Create_Contact, Find_Contact, All_Contacts = range(4)

# функция обратного вызова точки входа в разговор
def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Создать контакт', 'Поиск контакта', 'Показать все контакты']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        f'Приветствую тебя {update.effective_user.first_name}\n'
        'Ты находишься в ТГ-боте тлф справочника.\n'
        'Команда /cancel, чтобы прекратить разговор.\n'
        'Что желаете сделать?',
        reply_markup=markup_key,)
    return Main_menu

# Обрабатываем выбор кнопки из меню
def main_menu(update, _):
    if update.message.text == 'Создать контакт':
        # logger.my_log(update, CallbackContext, 'Создаем контакт')
        update.message.reply_text(
        'Хорошо. Введите имя контакта', 
        reply_markup=ReplyKeyboardRemove(),)
        return Create_Contact

    elif update.message.text == 'Поиск контакта':
        update.message.reply_text(
        'По какому параметру будем искать?', 
        reply_markup=ReplyKeyboardRemove(),)
        return Find_Contact
    
    elif update.message.text == 'Показать все контакты':
        update.message.reply_text(
        'По какому параметру будем искать?', 
        reply_markup=ReplyKeyboardRemove(),)
        return All_Contacts

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        'Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            Main_menu: [MessageHandler(Filters.text, main_menu)],
            Create_Contact:[MessageHandler(Filters.text, menu.name)],
            menu.surname:[MessageHandler(Filters.text, menu.surname)],
            menu.phone_number:[MessageHandler(Filters.text, menu.phone_number)],
            menu.comment:[MessageHandler(Filters.text, menu.comment)],   
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    print('server started')
    updater.start_polling()
    updater.idle()