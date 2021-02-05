from django.db import models

# Create your models here.
class Frequency(models.Model):
    url = models.URLField(max_length = 400)

class Store(models.Model):
    count = models.IntegerField()
    streengs = models.CharField(max_length = 100)
    url = models.URLField(max_length = 400)