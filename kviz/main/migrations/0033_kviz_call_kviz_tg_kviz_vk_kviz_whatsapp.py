# Generated by Django 5.0 on 2025-06-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_kviz_work_another'),
    ]

    operations = [
        migrations.AddField(
            model_name='kviz',
            name='call',
            field=models.BooleanField(null=True, verbose_name='Звонок'),
        ),
        migrations.AddField(
            model_name='kviz',
            name='tg',
            field=models.BooleanField(null=True, verbose_name='Телеграм'),
        ),
        migrations.AddField(
            model_name='kviz',
            name='vk',
            field=models.BooleanField(null=True, verbose_name='Вконтакте'),
        ),
        migrations.AddField(
            model_name='kviz',
            name='whatsapp',
            field=models.BooleanField(null=True, verbose_name='Ватсап'),
        ),
    ]
