from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    likes = models.PositiveIntegerField(default=0)
    image = models.CharField(max_length=200) 