from django.db import models


class DonationGroup(models.Model):
    title = models.CharField(max_length=255, blank=False)
    email = models.EmailField()
    description = models.TextField(blank=True)
    facebook_url = models.CharField(max_length=255, blank=True)
    donation_location = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #Python 3.3 is __str__
        return self.email


class PhoneNumber(models.Model):
    donation_group = models.ForeignKey(DonationGroup, related_name='phone_numbers')
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=False)
