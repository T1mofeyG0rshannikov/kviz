# Generated by Django 5.0 on 2025-06-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_kviz_birth_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='kviz',
            name='citizenship',
            field=models.CharField(max_length=50, null=True, verbose_name='Гражданство'),
        ),
        migrations.AddField(
            model_name='kviz',
            name='min_zp',
            field=models.CharField(max_length=15, null=True, verbose_name='Минимальная зарплата'),
        ),
        migrations.AddField(
            model_name='kviz',
            name='residence',
            field=models.CharField(max_length=50, null=True, verbose_name='Место жительства'),
        ),
        migrations.AddField(
            model_name='kviz',
            name='skills',
            field=models.CharField(max_length=200, null=True, verbose_name='О своих профессиональных навыках'),
        ),
    ]
