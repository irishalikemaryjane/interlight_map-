import os
import telebot
import requests

TOKEN = os.getenv("BOT_TOKEN")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

GROUP_ID = -1002150987101

bot = telebot.TeleBot(TOKEN)


headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}


def in_group(user_id):
    try:
        chat_member = bot.get_chat_member(GROUP_ID, user_id)
        return chat_member.status in ["member", "administrator", "creator"]
    except:
        return False


def save_user(user, city):
    data = {
        "telegram_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "city": city
    }

    requests.post(
        f"{SUPABASE_URL}/rest/v1/users",
        json=data,
        headers=headers
    )


def update_city(city):
    # проверяем есть ли город
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/cities?city=eq.{city}",
        headers=headers
    )

    if r.json():
        count = r.json()[0]["count"] + 1
        requests.patch(
            f"{SUPABASE_URL}/rest/v1/cities?city=eq.{city}",
            json={"count": count},
            headers=headers
        )
    else:
        requests.post(
            f"{SUPABASE_URL}/rest/v1/cities",
            json={"city": city, "count": 1},
            headers=headers
        )


@bot.message_handler(commands=["start"])
def start(message):
    if not in_group(message.from_user.id):
        bot.send_message(message.chat.id, "❌ Доступ только для участников INTERLIGHT.")
        return

    bot.send_message(message.chat.id, "📍 Напиши свой город:")


@bot.message_handler(func=lambda m: True)
def city_handler(message):
    if not in_group(message.from_user.id):
        return

    city = message.text.strip().lower()

    save_user(message.from_user, city)
    update_city(city)

    bot.send_message(message.chat.id, f"✅ Город сохранён: {city}")


bot.polling()
