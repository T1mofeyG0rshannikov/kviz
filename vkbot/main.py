import os
from dotenv import load_dotenv
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests


load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")
GROUP_ID = os.getenv('GROUP_ID')
APP_URL = os.getenv('APP_URL')
SITE_URL = os.getenv('SITE_URL')
YOUR_VK_APP_ID = os.getenv('YOUR_VK_APP_ID')

vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, GROUP_ID)


def download_file(url, filename):
    """Скачивает файл по URL и сохраняет его локально."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Проверка на ошибки HTTP

        with open("files/" + filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании файла: {e}")
        return False


def send_message(user_id, message, attachment=None):
    """Отправляет сообщение пользователю с возможностью прикрепления вложения."""
    try:
        vk.messages.send(
            user_id=user_id,
            message=message,
            random_id=vk_api.utils.get_random_id(),
            attachment=attachment
        )
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")


def main():
    print("VK Бот запущен...")
    user_states = {}

    draft_data = {}

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            user_id = event.obj.message['from_id']
            state = user_states.get(user_id)
            message = event.obj.message['text']
            attachments = event.obj.message.get('attachments')
            content_type = 'document' if attachments else 'text'

            if attachments:
                for attachment in attachments:
                    if attachment['type'] == 'doc':
                        doc = attachment['doc']
                        doc_url = doc['url']
                        doc_title = doc['title']

                        filename = doc_title
                        draft_data['documents'] = draft_data.get('documents', []) + [filename]

                        download_file(doc_url, filename)

            print(user_id)
            if message.lower() == 'старт':
                vk.messages.send(
                    user_id=user_id,
                    message=f"Вот ссылка на приложение: {APP_URL}",
                    random_id=0
                )

            elif message.lower() == "рассылка":
                user_states[user_id] = 'auth'

                vk.messages.send(
                    user_id=user_id,
                    message="Пришлите логи и пароль через запятую:",
                    random_id=0
                )
            else:
                if state == 'auth':
                    login, password = message.split(",")
                    response = requests.post(SITE_URL + "/login", data={"username": login, "password": password})
                    print(response.status_code)
                    if response.status_code == 200:
                        user_states[user_id] = 'awaiting_user_ids'
                        vk.messages.send(
                            user_id=user_id,
                            message="Пожалуйста, пришлите список user_id через запятую или построчно:",
                            random_id=0
                        )
                    else:
                        vk.messages.send(
                            user_id=user_id,
                            message="Ошибка авторизации, попробуйте ещё раз:",
                            random_id=0
                        )

                elif state == 'awaiting_user_ids':
                    user_ids_text = message.strip()
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
                    user_states[user_id] = 'awaiting_broadcast_text'
                    vk.messages.send(
                        user_id=user_id,
                        message="Теперь пришлите текст сообщения для рассылки:",
                        random_id=0
                    )

                elif state == 'awaiting_broadcast_text':
                    draft_data['message_text'] = message
                    user_states[user_id] = 'awaiting_files'
                    vk.messages.send(
                        user_id=user_id,
                        message="Теперь пришлите файлы (если есть). Если файлов нет, отправьте любое сообщение, например, 'Нет файлов'.",
                        random_id=0
                    )

                elif state == 'awaiting_files':
                    if content_type == 'text':
                        vk.messages.send(
                            user_id=user_id,
                            message="Обработка рассылки начнется. Отправляю сообщения...",
                            random_id=0
                        )

                        user_ids = draft_data.get('user_ids', [])
                        message_text = draft_data.get('message_text', '')
                        photos = draft_data.get('photos', [])
                        documents = draft_data.get('documents', [])

                        print(user_ids)
                        print(documents)
                        print(photos)
                        for user_id in user_ids:
                            vk.messages.send(
                                user_id=user_id,
                                message=message_text,
                                random_id=0
                            )

                            for doc in documents:
                                vk.messages.send(
                                    user_id=user_id,
                                    message=doc,
                                    attachment=[f"{SITE_URL}/files/{doc}"],
                                    random_id=0
                                )
                            for photo in photos:
                                vk.messages.send(
                                    user_id=user_id,
                                    message=doc,
                                    attachment=[f"{SITE_URL}/files/{photo}"],
                                    random_id=0
                                )


                        vk.messages.send(
                            user_id=user_id,
                            message="Рассылка завершена.",
                            random_id=0
                        )
                        user_states.pop(user_id, None)
                        draft_data.clear()

if __name__ == '__main__':
    main()
