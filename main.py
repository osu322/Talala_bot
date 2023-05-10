import telebot
import config

bot = telebot.TeleBot(config.BOT_CONFIG)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет")
bot.infinity_polling()