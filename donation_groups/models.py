from django.db import models


class DonationGroup(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    facebook_url = models.CharField(max_length=255, blank=True)
    phone_numbers = models.TextField(blank=True)
    donation_location = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title


class Newsfeed(models.Model):
    condition_choices = (
        (0, 'Unknown'),
        (1, 'Normal'),
        (2, 'Bad'),
        (3, 'Very Bad'),
    )

    title = models.CharField(max_length=255, blank=False)
    show_hide = models.BooleanField(default=False, verbose_name="Hide")
    description = models.TextField(blank=True)
    spam_report_count = models.IntegerField(default=0)
    dam_condition = models.IntegerField(default=0, choices=condition_choices)
    river_condition = models.IntegerField(default=0, choices=condition_choices)

    def __unicode__(self):
        return self.title
