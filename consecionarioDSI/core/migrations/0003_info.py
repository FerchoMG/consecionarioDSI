# Generated by Django 3.0.7 on 2023-08-21 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230819_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id_info', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200, verbose_name='email')),
                ('message', models.CharField(max_length=15, verbose_name='Mensaje')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
            ],
        ),
    ]
