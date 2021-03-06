# Generated by Django 3.0.6 on 2020-07-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200712_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст для отображения')),
                ('image', models.ImageField(height_field=500, upload_to='features/', verbose_name='Изображение', width_field=500)),
                ('link', models.CharField(max_length=100, verbose_name='Ссылка перехода')),
            ],
        ),
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст для отображения')),
                ('image', models.ImageField(height_field=140, upload_to='marketing/', verbose_name='Изображение', width_field=140)),
                ('link', models.CharField(max_length=100, verbose_name='Ссылка перехода')),
                ('button', models.CharField(blank=True, default='Подробнее >>', max_length=50, null=True, verbose_name='Название перехода')),
            ],
        ),
        migrations.AlterField(
            model_name='carousel',
            name='button',
            field=models.CharField(blank=True, default='Подробнее >>', max_length=50, null=True, verbose_name='Название перехода'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='link',
            field=models.CharField(default='/books/', max_length=100, verbose_name='Ссылка перехода'),
            preserve_default=False,
        ),
    ]
