from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название слайда')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст для отображения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='carousel_images/', verbose_name='Картинка слайда')),
                ('link', models.CharField(max_length=100, verbose_name='Ссфлка перехода')),
            ],
        ),
    ]