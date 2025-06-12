from django.db import models


class Client(models.Model):
    username = models.CharField(max_length=50, null=True)
    messanger_name = models.CharField(max_length=50)
    messanger = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username if self.username else "username"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Kviz(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    count = models.SmallIntegerField(default=1)

    name = models.CharField(max_length=50, null=True, verbose_name="Имя, которое указал пользователь")
    phone = models.CharField(max_length=50, null=True, verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    interes = models.CharField(max_length=50, null=True, verbose_name="Что интересует")
    profession = models.CharField(max_length=50, null=True, verbose_name="Профессия")
    work_experience = models.CharField(max_length=50, null=True, verbose_name="Опыт работы")
    birth_year = models.CharField(max_length=50, null=True, verbose_name="Год рождения")
    min_zp = models.CharField(max_length=15, null=True, verbose_name="Минимальная зарплата")
    citizenship = models.CharField(max_length=50, null=True, verbose_name="Гражданство")
    residence = models.CharField(max_length=50, null=True, verbose_name="Место жительства")
    skills = models.CharField(max_length=200, null=True, verbose_name="О своих профессиональных навыках")
    responsible = models.BooleanField(null=True, verbose_name="Ответственный")
    instrument = models.BooleanField(null=True, verbose_name="Инструмент")
    partner = models.BooleanField(null=True, verbose_name="Есть напарник")
    brigada = models.BooleanField(null=True, verbose_name="Бригада")
    car = models.BooleanField(null=True, verbose_name="Авто")
    rate_work = models.BooleanField(null=True, verbose_name="Оценка объекта")
    have_ip = models.BooleanField(null=True, verbose_name="СЗ/ИП")
    
    permanent_job = models.BooleanField(null=True, verbose_name="Интересует постоянная работа")
    temporary_job = models.BooleanField(null=True, verbose_name="Интересует временная работа")
    job_without_registration = models.BooleanField(null=True, verbose_name="Интересует работа без оформления")
    schedulefivetwo = models.BooleanField(null=True, verbose_name="Интересует график 5/2")
    shift_schedule = models.BooleanField(null=True, verbose_name="Интересует сменный график") 
    dayly_pay = models.BooleanField(null=True, verbose_name="Интересует ежедневная оплата")
    piecework_payment = models.BooleanField(null=True, verbose_name="Интересует сдельная оплата")
    any_job = models.BooleanField(null=True, verbose_name="Интересует любая работа")
    work_another = models.CharField(null=True, max_length=200, verbose_name="Какая работа Вас интересует? (Другое)")

    another_skills = models.CharField(null=True, max_length=200, verbose_name="Другие преимущества")
    
    NAKCT = models.BooleanField(null=True, verbose_name="НАКСТ")

    installation_window_frame = models.BooleanField(null=True, verbose_name="Монтаж окожушки")
    installation_foil_cylinders = models.BooleanField(null=True, verbose_name="Монтаж фольг. цилиндров")
    installation_kflex = models.BooleanField(null=True, verbose_name="Монтаж K-Flex")
    installation_PPU_shell = models.BooleanField(null=True, verbose_name="Монтаж ППУ скорлупы")
    foam_glass_installation = models.BooleanField(null=True, verbose_name="Монтаж пеностекла")
    manufacture_shell = models.BooleanField(null=True, verbose_name="Изготовление окожушки")
    spraying_PPU = models.BooleanField(null=True, verbose_name="Напыление ППУ")
    another_insulator_skills = models.CharField(null=True, max_length=200, verbose_name="Другие навыки")

    pipelines = models.BooleanField(null=True, verbose_name="Трубопроводы")
    airducts = models.BooleanField(null=True, verbose_name="Воздуховоды")
    reservoirs = models.BooleanField(null=True, verbose_name="Резервуары")
    equipment = models.BooleanField(null=True, verbose_name="Оборудование")
    another_can_installer_skills = models.CharField(null=True, max_length=200, verbose_name="Что другое умеет изолировать")

    manual_electric_arc = models.BooleanField(null=True, verbose_name="Ручная электродуговая")
    semiautomatic = models.BooleanField(null=True, verbose_name="Полуавтоматическая")
    argon = models.BooleanField(null=True, verbose_name="Аргоновая")
    gasfired = models.BooleanField(null=True, verbose_name="Газовая")
    plasma = models.BooleanField(null=True, verbose_name="Плазменная")
    welding_gas_environment = models.BooleanField(null=True, verbose_name="Сварка в среде газа")
    another_welding = models.CharField(null=True, max_length=200, verbose_name="Другие виды сварки")

    can_weld_simple_constructions = models.BooleanField(null=True, verbose_name="Простые конструкции")
    can_weld_building_frames = models.BooleanField(null=True, verbose_name="Каркасы зданий")
    can_weld_columns = models.BooleanField(null=True, verbose_name="Балки, колонны")
    can_weld_pipelines = models.BooleanField(null=True, verbose_name="Трубопроводы")
    can_weld_energy_boilers = models.BooleanField(null=True, verbose_name="Энергетические котлы")
    can_weld_equipment = models.BooleanField(null=True, verbose_name="Оборудование")
    can_weld_another = models.CharField(null=True, max_length=200, verbose_name="Другие конструкции")

    read_drawings_diagrams = models.BooleanField(null=True, verbose_name="Читаю чертежи и схемы")
    know_norms_standards = models.BooleanField(null=True, verbose_name="Знаю нормы и стандарты")
    conducting_hydrotests = models.BooleanField(null=True, verbose_name="Провожу гидроиспытания")
    organizational_skills = models.BooleanField(null=True, verbose_name="Организаторские навыки")
    working_with_tools = models.BooleanField(null=True, verbose_name="Работа с инструментами")
    another_installer_skills = models.CharField(null=True, max_length=200, verbose_name="Другие навыки")

    OPF = models.CharField(null=True, max_length=3, verbose_name="ОПФ")

    activity_direction = models.CharField(null=True, max_length=200, verbose_name="Направление деятельности")
    activity_region = models.CharField(null=True, max_length=200, verbose_name="Регион/Город")

    contract_price = models.CharField(null=True, max_length=200, verbose_name="Цена контрактов")
    ceh_count = models.CharField(null=True, max_length=200, verbose_name="Численность персонала")

    interest_professions = models.CharField(null=True, max_length=200, verbose_name="Интересуют специалисты")
    region_professions = models.CharField(null=True, max_length=200, verbose_name="Специалисты в регоне")

    organization_form2 = models.CharField(null=True, max_length=200, verbose_name="Организация Форма 2")
    email_form2 = models.CharField(null=True, max_length=200, verbose_name="e-mai Форма 2")
    message_form2 = models.CharField(null=True, max_length=200, verbose_name="Сообщение Форма 2")

    has_work = models.CharField(null=True, max_length=200, verbose_name="Есть основная работа")
    has_work_another = models.CharField(null=True, max_length=200, verbose_name="Есть основная работа (Другое)")

    call = models.BooleanField(null=True, verbose_name="Звонок")
    vk = models.BooleanField(null=True, verbose_name="Вконтакте")
    tg = models.BooleanField(null=True, verbose_name="Телеграм")
    whatsapp = models.BooleanField(null=True, verbose_name="Ватсап")

    object_region = models.CharField(null=True, max_length=200, verbose_name="регион объекта")
    another_object_region = models.CharField(null=True, max_length=200, verbose_name="регион объекта (Другое)")

    plastering_works = models.BooleanField(null=True, verbose_name="Штукатурные работы")
    painting_work = models.BooleanField(null=True, verbose_name="Малярные работы")
    laying_tiles = models.BooleanField(null=True, verbose_name="Укладка плитки")
    installation_drywall = models.BooleanField(null=True, verbose_name="Монтаж гипсокартона")
    wallpapering = models.BooleanField(null=True, verbose_name="Оклейка обоями")
    installation_doors_and_windows = models.BooleanField(null=True, verbose_name="Установка дверей и окон")
    ceiling_installation = models.BooleanField(null=True, verbose_name="Монтаж потолков")
    comprehensive_finishing = models.BooleanField(null=True, verbose_name="Комплексная отделка")

    metro = models.CharField(null=True, max_length=200, verbose_name="Метро")

    @property
    def created_at_tag(self):
        return self.created_at.strftime("%Y.%m.%d %H.%M")

    @property
    def user_id(self):
        return self.client.id

    @property
    def nickname(self):
        return self.client.nickname

    @property
    def messanger(self):
        return self.client.messanger
    
    @property
    def unique_key(self):
        return f"{self.client.id}-{self.count}"
    
    @property
    def messanger_name(self):
        return self.client.messanger_name

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Form(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя")
    title = models.CharField(max_length=150, verbose_name="заголовок")
    type = models.CharField(max_length=10, choices=[("radio", "radio"), ("checkbox", "checkbox"), ("text", "text")])
    
    next = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    another_field = models.CharField(max_length=50, null=True, blank=True)
    show_next = models.BooleanField(default=False, verbose_name="Показывать следующее")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Форма"
        verbose_name_plural = "Формы"
        ordering = ['title']

class Option(models.Model):
    text = models.CharField(max_length=50, verbose_name="текст")
    next = models.ForeignKey(Form, on_delete=models.SET_NULL, null=True, blank=True)
    field = models.CharField(max_length=50, verbose_name='поле', null=True, blank=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="options")