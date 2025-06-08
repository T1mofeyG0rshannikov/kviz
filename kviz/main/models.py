from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    messanger_name = models.CharField(max_length=50)
    messanger = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

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
