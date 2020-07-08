from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from genre.models import Genre
# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100, verbose_name="Название книги")
    image = models.ImageField(upload_to='books_images/', blank=True, null=True, verbose_name="Фото обложки")
    #author=models.CharField(max_length=100, verbose_name="Автор")
    description=models.TextField (blank=True, null=True, verbose_name="Описание книги")
    genres=models.ForeignKey('genre.Genre', on_delete=models.PROTECT)
    
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (BYN)")
    year = models.PositiveIntegerField(
               validators=[
                   MinValueValidator(1900), 
                   MaxValueValidator(datetime.now().year)],
               help_text="Используйте формат: <YYYY>", default=datetime.now().year, blank=True, null=True, verbose_name="Год издания")
    
    pages=models.PositiveIntegerField(blank=True, null=True, verbose_name="Количество страниц")
    binding=models.CharField(blank=True, null=True, max_length=100, verbose_name="Переплет")
    isbn=models.CharField(blank=True, null=True, unique=True, max_length=17, verbose_name='ISBN')
    weight=models.PositiveIntegerField(blank=True, null=True, verbose_name="Вес (гр)")
    age_rating=models.PositiveIntegerField(blank=True, null=True, verbose_name='Возрастные ограничения')

    quantity=models.PositiveIntegerField(default=0, verbose_name='Количество книг в наличии')
    active=models.BooleanField(default=False, verbose_name="Активный (доступен для заказа, Да/Нет)")
    rating=models.PositiveIntegerField(blank=True, null=True, verbose_name='Рейтинг (0 - 10)')
    created=models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата внесения в каталог')
    modified=models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name