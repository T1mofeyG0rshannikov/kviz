import telebot
from telebot import types
import requests
import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
APP_URL = os.getenv('APP_URL')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    nickname = message.from_user.username
    messsanger_name = message.from_user.first_name
    id = message.from_user.id

    response = requests.post(APP_URL + "/client", data={"user_id": id, "nickname": nickname, "messanger": "tg", "messanger_name": messsanger_name})
    print(response.status_code)
    client = response.json()
    client = client["client"]
    print(client)

    keyboard = types.InlineKeyboardMarkup()

    web_app_button = telebot.types.InlineKeyboardButton(
        text="Открыть приложение",
        web_app=telebot.types.WebAppInfo(url=APP_URL + f"/kviz?client={client}")
    )

    keyboard.add(web_app_button)
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы открыть приложение:", reply_markup=keyboard)

user_states = {}

draft_data = {}

@bot.message_handler(commands=['rassilka'])
def handle_rassilka_start(message: types.Message):
    chat_id = message.chat.id
    user_states[chat_id] = 'auth'
   # user_states[chat_id] = 'awaiting_user_ids'

    bot.send_message(chat_id, "Пришлите логи и пароль через запятую:")


@bot.message_handler(content_types=['text', 'photo', 'document'])
def handle_message(message: types.Message):
    chat_id = message.chat.id
    state = user_states.get(chat_id)

    if state == 'auth':
        login, password = message.text.split(",")
        response = requests.post(APP_URL + "/login", data={"username": login, "password": password})
        print(response.status_code)
        if response.status_code == 200:
            user_states[chat_id] = 'awaiting_user_ids'
            bot.send_message(chat_id, "Пожалуйста, пришлите список user_id через запятую или построчно:")
        else:
            bot.send_message(chat_id, "Ошибка авторизации, попробуйте ещё раз:")

    elif state == 'awaiting_user_ids':
        user_ids_text = message.text.strip()
        user_ids = []

        if ',' in user_ids_text:
            parts = user_ids_text.split(',')
        else:
            parts = user_ids_text.splitlines()

        for part in parts:
            uid = part.strip()
            if uid.isdigit():
                user_ids.append(int(uid))

        draft_data['user_ids'] = user_ids
        user_states[chat_id] = 'awaiting_broadcast_text'
        bot.send_message(chat_id, "Теперь пришлите текст сообщения для рассылки:")

    elif state == 'awaiting_broadcast_text':
        draft_data['message_text'] = message.text
        user_states[chat_id] = 'awaiting_files'
        bot.send_message(chat_id, "Теперь пришлите файлы (если есть). Если файлов нет, отправьте любое сообщение, например, 'Нет файлов'.")

    elif state == 'awaiting_files':
        documents = [message.document] if message.document else []
        photos = [message.photo[-1]] if message.photo else []

        draft_data['photos'] = draft_data.get('photos', []) + photos
        draft_data['documents'] = draft_data.get('documents', []) + documents

        if message.content_type == 'text':
            bot.send_message(chat_id, "Обработка рассылки начнется. Отправляю сообщения...")

            user_ids = draft_data.get('user_ids', [])
            message_text = draft_data.get('message_text', '')
            photos = draft_data.get('photos', [])
            documents = draft_data.get('documents', [])

            document_files = []
            photo_files = []

            for doc in documents:
                file_id = doc.file_id
                file_info = bot.get_file(file_id)
                
                downloaded_file = bot.download_file(file_info.file_path)
                document_files.append({"file": downloaded_file, "name": doc.file_name})

            for photo in photos:
                file_id = photo.file_id
                file_info = bot.get_file(file_id)
                
                downloaded_file = bot.download_file(file_info.file_path)
                photo_files.append(downloaded_file)

            for user_id in user_ids:
                bot.send_message(user_id, message_text)

                for doc in document_files:
                    bot.send_document(user_id, doc["file"], visible_file_name=doc["name"])
                for photo in photo_files:
                    bot.send_photo(user_id, photo)


            bot.send_message(chat_id, "Рассылка завершена.")
            user_states.pop(chat_id, None)
            draft_data.clear()


if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()