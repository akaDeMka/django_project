# Generated by Django 3.0.6 on 2020-07-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200712_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='image',
            field=models.ImageField(upload_to='features/', verbose_name='Изображение'),
        ),
    ]
