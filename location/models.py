from django.db import models

class Location(models.Model):
    district = models.CharField(max_length=255)
    township = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.district
