# Generated by Django 3.0.6 on 2020-07-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='ФИО автора')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Об авторе')),
            ],
        ),
    ]
