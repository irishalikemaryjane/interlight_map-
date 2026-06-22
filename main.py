import os
import telebot

# ====== TOKEN ======
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise Exception("Нет TELEGRAM_TOKEN в переменных окружения")

bot = telebot.TeleBot(TOKEN, threaded=False)

# ====== START ======
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ Бот работает!")

# ====== ECHO ======
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, f"Ты написал: {message.text}")

# ====== RUN ======
if __name__ == "__main__":
    print("BOT STARTED")
    bot.infinity_polling(skip_pending=True)
