from django.contrib import admin
from main.models import Client, Kviz


class KvizAdmin(admin.ModelAdmin):
    [
        "Другие преимущества" "НАКСТ", "Монтаж окожушки",
        "Монтаж фольг.", "Цилиндров", "Монтаж K-Flex", "Монтаж ППУ скорлупы", "Монтаж пеностекла", 
        "Изготовление окожушки", "Напыление ППУ",	"Другие навыки", "Трубопроводы", "Воздуховоды", 
        "Резервуары", "Оборудование", "Что другое умеет изолировать", "Ручная электродуговая", 
        "Полуавтоматическая", "Аргоновая", "Газовая", "Плазменная", "Сварка в среде газа",
        "Другие виды сварки", "Простые конструкции", "Каркасы зданий", "Балки, колонны",
        "Трубопроводы", "Котлы", "Оборудование", "Другие конструкции", "Читаю чертежи и схемы", 
        "Знаю нормы и стандарты", "Провожу гидроиспытания", "Организаторские навыки",
        "Работа с инструментами", "Другие навыки", "ОПФ", "Направление деятельности", "Регион/Город",
        "Цена контрактов", "Численность персонала", "Интересуют специалисты", "Организация Форма 2",
        "e-mai Форма 2", "Сообщение Форма 2", "Есть основная работа", "пятидневка",
        "Есть основная работа, сменный график", "Свободный график",	"Нет работы, только подработки",
        "Нет основной работы", "У вас есть основная работа? (Другое)",	"Интересует постоянная работа",
        "Интересует временная работа", "Интересует работа без оформления", "Интересует график 5/2",
        "Интересует сменный график", "Интересует ежедневная оплата", "Интересует сдельная оплата",
        "Интересует любая работа", "Какая работа Вас интересует? (Другое)", "Звонок", "Ватсап",
        "Телеграм", "Вконтакте"
    ]

    list_display = [
        "messanger", "messanger_name", "name", "nickname", "user_id",
        "phone", "unique_key", "created_at_tag", "interes", 
        "profession", "work_experience", "birth_year", "min_zp",
        "citizenship", "residence", "skills", "responsible", "instrument",
        "partner", "brigada", "car", "rate_work", "have_ip", "permanent_job",
        "temporary_job", "job_without_registration", "schedulefivetwo",
        "shift_schedule", "dayly_pay", "piecework_payment", "any_job"
    ]

    @admin.display(description="Дата и время")
    def created_at_tag(self, obj):
        return obj.created_at.strftime("%Y.%m.%d %H.%M")

    @admin.display(description="User ID")
    def user_id(self, obj):
        return obj.client.id

    @admin.display(description="Никнейм")
    def nickname(self, obj):
        return obj.client.nickname

    @admin.display(description="Имя, которое указал пользователь")
    def name(self, obj):
        return obj.client.name

    @admin.display(description="ТГ/ВК")
    def messanger(self, obj):
        return obj.client.messanger
    
    @admin.display(description="Уникальный ключ")
    def unique_key(self, obj):
        return f"{obj.client.id}-{obj.count}"
    
    @admin.display(description="Имя в ТГ/ВК")
    def messanger_name(self, obj):
        return obj.client.messanger_name

admin.site.register(Client)
admin.site.register(Kviz, KvizAdmin)