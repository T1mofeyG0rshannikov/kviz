from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, null=True)
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
    communication_methods = models.CharField(max_length=10, null=True)
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
