import telebot
import time

TOKEN = "ТВОЙ_ТОКЕН_СЮДА"

bot = telebot.TeleBot(TOKEN)

# пример проверки группы (оставь свою функцию если есть)
def in_group(user_id):
    return True


@bot.message_handler(func=lambda message: True)
def handle_city(message):
    if not in_group(message.from_user.id):
        bot.send_message(message.chat.id, "❌ Только для группы")
        return

    city = message.text.strip().lower()

    # тут твои функции
    # save_user(...)
    # update_city(...)

    bot.send_message(message.chat.id, f"✅ Сохранено: {city}")


# СТАБИЛЬНЫЙ ЗАПУСК ДЛЯ RENDER
if __name__ == "__main__":
    print("BOT STARTED")

    while True:
        try:
            bot.remove_webhook()
            bot.infinity_polling(skip_pending=True)
        except Exception as e:
            print("ERROR:", e)
            time.sleep(5)
