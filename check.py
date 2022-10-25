def check_text(update, text):
    if len(text)>20:
        update.message.reply_text('Слишком длинное значение')
        return False
    else:
        return True


def check_number(update, text):
    if  text.isdigit and len(text)>15:
        update.message.reply_text('Некорректный ввод')
        return False
    else:
        return True


