from django.db import models
from django.utils import timezone
# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100, verbose_name="Название книги")
    description=models.TextField (blank=True, null=True, verbose_name="Описание книги")
    
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (BYN)")
    date_pub=models.DateField(blank=True, null=True, verbose_name="Год издания")
    pages=models.IntegerField(blank=True, null=True, verbose_name="Страниц")
    binding=models.CharField(blank=True, null=True, max_length=100, verbose_name="Переплет")
    isbn=models.CharField(blank=True, null=True, unique=True, max_length=17, verbose_name='ISBN')
    weight=models.IntegerField(blank=True, null=True, verbose_name="Вес (гр)")
    age_rating=models.IntegerField(blank=True, null=True, verbose_name='Возрастные ограничения')

    quantity=models.IntegerField(default=0, verbose_name='Количество книг в наличии')
    active=models.BooleanField(default=False, verbose_name="Активный (доступен для заказа, Да/Нет)")
    rating=models.IntegerField(blank=True, null=True, verbose_name='Рейтинг (0 - 10)')
    created=models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата внесения в каталог')
    modified=models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата последнего изменения')

    #def save(self, *args, **kwargs):
    #    ''' On save, update timestamps '''
    #    if not self.id:
    #        self.created = timezone.now()
    #    self.modified = timezone.now()
    #    return super(self).save(*args, **kwargs)
    

    def __str__(self):
        return self.name