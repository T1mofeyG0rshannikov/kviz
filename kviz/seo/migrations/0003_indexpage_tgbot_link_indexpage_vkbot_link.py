# Generated by Django 5.1.6 on 2025-06-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0002_alter_indexpage_enable_running_line_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='tgbot_link',
            field=models.CharField(max_length=100, null=True, verbose_name='ссылка на бота в tg'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='vkbot_link',
            field=models.CharField(max_length=100, null=True, verbose_name='ссылка на бота в vk'),
        ),
    ]
