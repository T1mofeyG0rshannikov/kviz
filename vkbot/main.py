# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = '7572740935:AAEYWglRKGGPOww-L-DwM5ZKYrwHIyUyJN4'

# Ссылка на ваше Telegram-приложение
APP_URL = "https://kviz111.pythonanywhere.com"

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# Замените на свои данные
VK_TOKEN = 'vk1.a.xJ8_KkEWENR740l1Lm6KFqbS6BQjGOhJabEmXdaEzp6KYCSL2088K_yNYZHa-obehkc0U-aO3NwEYky5IKDPeZSdpUM9wXg767TXTxO-lVC7bS-ICRkm0O6nN-Fbe5-Y4awX2MhkYdaNzaYtKY6mOfhtNKq3GodNvPhVOTMHvc61tm_PyrXHEjPwmsAPh_C4tMRtGDxlDuoT1fgK5e1dsg'  # Токен сообщества VK
GROUP_ID = 230803417  # ID вашего сообщества VK
APP_URL = 'https://vk.com/app52695395'  # URL вашего мини-приложения (HTTPS)
YOUR_VK_APP_ID = 'https://vk.com/app52695395'

vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, GROUP_ID)


def main():
    print("VK Бот запущен...")
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:

            if event.obj.message['text'].lower() == 'старт':  # Обрабатываем команду "старт"
                user_id = event.obj.message['from_id']  # ID пользователя, отправившего сообщение


                # Создаем кнопку для открытия мини-приложения
                keyboard = {
                    "one_time": True,  # Кнопка исчезнет после нажатия
                    "buttons": [
                        [
                            {
                                "action": {
                                    "type": "open_app",
                                    "app_id": YOUR_VK_APP_ID,  # ID вашего приложения VK (замените!)
                                    "owner_id": -GROUP_ID,  # ID сообщества с минусом
                                    "label": "Открыть приложение", # Текст на кнопке
                                    "hash": "" # Дополнительные параметры (можно оставить пустым)
                                },
                                "color": "primary"  # Цвет кнопки (primary, secondary, negative, positive)
                            }
                        ]
                    ]
                }

                # Отправляем сообщение с кнопкой
                try:
                    vk.messages.send(
                        user_id=user_id,
                        message=f"Вот ссылка на приложение: {APP_URL}",
                        random_id=0
                    )
                except Exception as e:
                    print(f"Ошибка отправки сообщения: {e}")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Произошла ошибка: {e}")