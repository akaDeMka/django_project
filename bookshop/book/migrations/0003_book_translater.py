# Generated by Django 3.0.6 on 2020-07-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200706_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='translater',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Переводчик'),
        ),
    ]
