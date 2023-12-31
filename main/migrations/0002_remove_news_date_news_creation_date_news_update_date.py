# Generated by Django 4.2.8 on 2023-12-16 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
        migrations.AddField(
            model_name='news',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
