import telebot
from telebot import types  # Добавляем импорт types
import requests

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = '7572740935:AAEYWglRKGGPOww-L-DwM5ZKYrwHIyUyJN4'

# Ссылка на ваше Telegram-приложение
TELEGRAM_APP_LINK = 'https://t.me/your_telegram_app'  # Замените!
APP_URL = "http://127.0.0.1:8000"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    """Обработчик команды /start."""
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    # Формируем сообщение с данными пользователя
    user_info = f"Привет!\n"
    user_info += f"ID: {user_id}\n"
    user_info += f"Username: @{username}\n"  # Добавляем @ перед username
    user_info += f"Имя: {first_name}\n"
    user_info += f"Фамилия: {last_name}\n"

    kviz = requests.post(APP_URL + "/kviz", data={"username": username, "messanger": "tg"})
    kviz = kviz.json()
    print(kviz)
    kviz = kviz["kviz"]

    # Создаем Inline Keyboard
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Открыть приложение", url=TELEGRAM_APP_LINK + "?kviz={kviz}")
    keyboard.add(url_button)

    web_app_button = telebot.types.InlineKeyboardButton(
        text="Открыть приложение",
        web_app=telebot.types.WebAppInfo(url=APP_URL)
    )

    keyboard.add(web_app_button)
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы открыть приложение:", reply_markup=keyboard)


if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()