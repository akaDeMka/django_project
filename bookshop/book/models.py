from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100, verbose_name="Название книги")
    description=models.TextField (blank=True, null=True, verbose_name="Описание книги")
    
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (BYN)")
    date_pub=models.DateField(blank=True, null=True, verbose_name="Год издания")
    pages=models.IntegerField(blank=True, null=True, verbose_name="Страниц")
    binding=models.CharField(blank=True, null=True, max_length=100, verbose_name="Переплет")
    isbn=models.IntegerField(blank=True, null=True, unique=True, verbose_name='ISDN')
    weight=models.IntegerField(blank=True, null=True, verbose_name="Вес (гр)")
    age_rating=models.IntegerField(blank=True, null=True, verbose_name='Возрастные ограничения')

    quantity=models.IntegerField(default=0, verbose_name='Количество книг в наличии')
    active=models.BooleanField(default=False, verbose_name="Активный (доступен для заказа, Да/Нет)")
    rating=models.IntegerField(blank=True, null=True, verbose_name='Рейтинг (0 - 10)')
    ent_date=models.DateTimeField(editable=False, verbose_name='Дата внесения в каталог')
    change_date=models.DateTimeField(editable=False, verbose_name='Дата последнего изменения')

    

    def __str__(self):
        return self.name