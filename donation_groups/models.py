from django.db import models
from newsfeed.converter import is_zawgyi, zg12uni51


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

    def save(self, *args, **kwargs):
        if is_zawgyi(self.title):
            self.title = zg12uni51(self.title)
        if is_zawgyi(self.description):
            self.description = zg12uni51(self.description)
        if is_zawgyi(self.donation_location):
            self.donation_location = zg12uni51(self.donation_location)
        super(DonationGroup, self).save(*args, **kwargs)
