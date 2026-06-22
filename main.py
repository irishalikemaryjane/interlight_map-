import os
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("NO TOKEN")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает!")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

print("BOT STARTED")

bot.infinity_polling(skip_pending=True)
