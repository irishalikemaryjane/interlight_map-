import os
import telebot

# ====== TOKEN (ОБЯЗАТЕЛЬНО через ENV) ======
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

print("BOT STARTED")

# ====== СТАБИЛЬНЫЙ ЗАПУСК (ВАЖНО ДЛЯ RENDER) ======
while True:
    try:
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print("ERROR:", e)
