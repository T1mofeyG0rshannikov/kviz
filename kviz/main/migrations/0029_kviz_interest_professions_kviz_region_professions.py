# Generated by Django 5.0 on 2025-06-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_kviz_ceh_count_kviz_contract_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='kviz',
            name='interest_professions',
            field=models.CharField(max_length=200, null=True, verbose_name='Интересуют специалисты'),
        ),
        migrations.AddField(
            model_name='kviz',
            name='region_professions',
            field=models.CharField(max_length=200, null=True, verbose_name='Специалисты в регоне'),
        ),
    ]
