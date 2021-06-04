from telebot import types


def weather_markup():
    markup = types.ReplyKeyboardMarkup(
        row_width=2,
        selective=True,
        one_time_keyboard=False
    )
    markup.add(
        types.KeyboardButton('current'),
        types.KeyboardButton('subscribe')
    )
    return markup
