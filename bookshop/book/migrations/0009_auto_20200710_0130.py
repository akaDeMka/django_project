# Generated by Django 3.0.6 on 2020-07-09 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0001_initial'),
        ('book', '0008_auto_20200710_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genres',
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='genre.Genre'),
        ),
    ]
