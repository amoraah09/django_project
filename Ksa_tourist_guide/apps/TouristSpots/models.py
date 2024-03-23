from django.db import models

class Spot(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
