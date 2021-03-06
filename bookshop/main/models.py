from django.db import models

# Create your models here.
class Carousel(models.Model):
    name=models.CharField(max_length=50, verbose_name="Название слайда")
    text=models.TextField (blank=True, null=True, verbose_name="Текст для отображения")
    image=models.ImageField(upload_to='carousel/', blank=True, null=True, verbose_name="картинка карусели")
    link = models.CharField(max_length=100, verbose_name="Ссылка перехода" )
    button = models.CharField(max_length=50, verbose_name="Название перехода", blank=True, null=True, default = 'Подробнее >>')

    def __str__(self):
        return self.name

class Marketing(models.Model):
    name=models.CharField(max_length=50, verbose_name="Название")
    text=models.TextField (verbose_name="Текст для отображения")
    image=models.ImageField(upload_to='marketing/', verbose_name="Изображение")
    link = models.CharField(max_length=100, verbose_name="Ссылка перехода")
    button = models.CharField(max_length=50, verbose_name="Название перехода", blank=True, null=True, default = 'Подробнее >>')
    def __str__(self):
        return self.name


