from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    User._meta.get_field('email').blank = False
    phone = PhoneNumberField(verbose_name="Телефон",default='+12125552368' )
    country=models.CharField(max_length=30, null=True, blank=True, verbose_name="Страна")
    city=models.CharField(max_length=30, null=True, blank=True, verbose_name="Город")
    index=models.CharField(max_length=15, null=True, blank=True, verbose_name="Индекс")
    address1=models.CharField(max_length=150, null=True, blank=True, verbose_name="Адрес1")
    address2=models.CharField(max_length=150, null=True, blank=True, verbose_name="Адрес2")
    notes = models.TextField(null=True, blank=True, verbose_name="Дополнительная информация")


