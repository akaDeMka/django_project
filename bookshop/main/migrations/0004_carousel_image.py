# Generated by Django 3.0.6 on 2020-07-12 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_carousel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='carousel/', verbose_name='картинка карусели'),
        ),
    ]
