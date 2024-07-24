from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.CharField(max_length=150, default=None)
    colors = models.ManyToManyField(to=Color)
