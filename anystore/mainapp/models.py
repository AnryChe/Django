from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='название категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)

    def __str__(self):
        return self.name