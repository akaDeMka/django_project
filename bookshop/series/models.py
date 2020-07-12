from django.db import models

# Create your models here.
class Series(models.Model):
    name=models.CharField(max_length=50, verbose_name="Название серии")

    def __str__(self):
        return self.name