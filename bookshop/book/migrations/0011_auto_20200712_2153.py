# Generated by Django 3.0.6 on 2020-07-12 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]