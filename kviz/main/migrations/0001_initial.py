# Generated by Django 5.0 on 2025-06-07 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_key', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('messanger_name', models.CharField(max_length=50)),
                ('messanger', models.CharField(max_length=50)),
                ('communication_methods', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.client')),
            ],
        ),
    ]
