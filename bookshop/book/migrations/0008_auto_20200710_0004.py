# Generated by Django 3.0.6 on 2020-07-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20200708_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='30478-3261.jpg', null=True, upload_to='books_images/', verbose_name='Фото обложки'),
        ),
    ]