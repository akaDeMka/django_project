# Generated by Django 3.0.6 on 2020-07-08 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='button',
            field=models.CharField(default='Подробнее ...', max_length=50, verbose_name='Название перехода'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='link',
            field=models.CharField(max_length=100, verbose_name='Ссылка перехода'),
        ),
    ]