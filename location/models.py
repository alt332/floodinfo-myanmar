from django.db import models

class Location(models.Model):
    district = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    township = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    total_male = models.IntegerField(default=0)
    total_female = models.IntegerField(default=0)
    urban_total_male = models.IntegerField(default=0)
    urban_total_female = models.IntegerField(default=0)
    rural_total_male = models.IntegerField(default=0)
    rural_total_female = models.IntegerField(default=0)

    def __str__(self):
        return self.district
