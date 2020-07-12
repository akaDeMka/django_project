from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=150, verbose_name="ФИО автора")
    description=models.TextField (blank=True, null=True, verbose_name="Об авторе")

    def __str__(self):
        return self.name