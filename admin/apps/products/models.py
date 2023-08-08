from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
