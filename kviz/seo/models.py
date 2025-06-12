from django.db import models


class IndexPage(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    privacy_link = models.CharField(max_length=100, verbose_name="Политика конфиденциальности")
    window_w = models.CharField(max_length=100, verbose_name="Окно W")
    running_line = models.CharField(max_length=200, verbose_name="Бегущая строка")
    enable_running_line = models.BooleanField(default=True, verbose_name="Включить бегущую строку")

    tgbot_link = models.CharField(max_length=100, null=True, verbose_name="ссылка на бота в tg")
    vkbot_link = models.CharField(max_length=100, null=True, verbose_name="ссылка на бота в vk")
    
    class Meta:
        verbose_name = "Настройки главной страницы"

    def __str__(self):
        return "Настройки главной страницы"