# Generated by Django 3.0.6 on 2020-07-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
        ('book', '0012_book_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ManyToManyField(to='series.Series'),
        ),
    ]
