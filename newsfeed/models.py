# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from converter import is_zawgyi, zg12uni51


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

    def save(self, *args, **kwargs):
        if is_zawgyi(self.title):
            self.title = zg12uni51(self.title)
        if is_zawgyi(self.description):
            self.description = zg12uni51(self.description)
        super(Newsfeed, self).save(*args, **kwargs)
