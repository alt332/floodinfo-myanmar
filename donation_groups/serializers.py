from django.forms import widgets
from rest_framework import serializers
from .models import DonationGroup


# class PhoneNumberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PhoneNumber
#         fields = ('name', 'phone')


class DonationGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationGroup
        ordering = ['title']
