from django.utils import timezone
from django.db import models


class Newsfeed(models.Model):
    condition_choices = (
        (0, 'Unknown'),
        (1, 'Normal'),
        (2, 'Bad'),
        (3, 'Very Bad')
    )

    title = models.CharField(max_length=255, blank=False)
    show_hide = models.BooleanField(default=False, verbose_name='Hide')
    description = models.TextField(blank=False)
    spam_report_count = models.IntegerField(default=0)
    dam_condition = models.IntegerField(default=0, choices=condition_choices)
    river_condition = models.IntegerField(default=0, choices=condition_choices)
    posted_time = models.DateTimeField(default=timezone.now, blank=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    township = models.CharField(max_length=255, blank=True, null=True)


    def __unicode__(self):
        return self.title
