from django.db import models

class TouristSpots(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
