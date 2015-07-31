from django.forms import widgets
from rest_framework import serializers
from .models import DonationGroup


class DonationGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationGroup
        ordering = ['title']
