from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=5000, null=True)
    address = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)
