# Generated by Django 5.0 on 2025-06-07 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_kviz_alter_client_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kviz',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.client'),
        ),
    ]
