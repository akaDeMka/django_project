from django.db import models

# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=50, verbose_name="Название издательства")
    description=models.TextField (blank=True, null=True, verbose_name="О издательстве")

    def __str__(self):
        return self.name