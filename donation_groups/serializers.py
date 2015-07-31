from django.forms import widgets
from rest_framework import serializers
from .models import DonationGroup, Newsfeed


class DonationGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationGroup
        ordering = ['title']


class NewsfeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsfeed
        ordering = ['title']
