from django.db import models

# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=50, verbose_name="Название жанра")
    description=models.TextField (blank=True, null=True, verbose_name="Описание жанра")

    def __str__(self):
        return self.name