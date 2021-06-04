import telebot
import weather_queries
import weather
import formatting
import markups
import timed

bot = telebot.TeleBot(
    "1842123074:AAFjwvOywwR1xDH5G5KfxNBsSvuVJYKKl40",
    parse_mode=None
)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(
        chat_id=chat_id,
        text="Choose the option: current or subscribe",
        reply_markup=markups.weather_markup()
    )


@bot.message_handler(regexp="current")
def handle_current(message):
    send_weather_data(message)


@bot.message_handler(regexp="subscribe")
def handle_subscribe(message):
    timed.periodically(
        lambda: send_weather_data(message),
        14400
    )


@bot.message_handler(regexp="maska")
def send_masochny(message):
    file = open("/Users/ethereos/Downloads/masochny.mp4", 'rb')
    bot.send_video(
        message.chat.id,
        file
    )
    file.close()


@bot.message_handler(regexp="where is my sunshine?")
def reply_to_text(message):
    bot.reply_to(message, "Vlad always beside you")


def send_weather_data(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=formatting.prettier(
            weather.weather_data(
                weather_queries.current_place_query()
            )
        )
    )


bot.polling()

# Done! Congratulations on your new bot. You will find it at t.me/Weather_4Beth_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 1842123074:AAFjwvOywwR1xDH5G5KfxNBsSvuVJYKKl40
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api
