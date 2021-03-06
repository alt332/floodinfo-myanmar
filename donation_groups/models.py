from django.utils import timezone
from django.db import models


class DonationGroup(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    facebook_url = models.CharField(max_length=255, blank=True)
    phone_numbers = models.TextField(blank=True)
    donation_location = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title
