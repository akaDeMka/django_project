# Generated by Django 3.0.6 on 2020-07-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
        ('book', '0014_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.ManyToManyField(blank=True, null=True, to='series.Series'),
        ),
    ]
