from django.forms import widgets
from rest_framework import serializers
from .models import DonationGroup, PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('name', 'phone')


class DonationGroupSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)

    class Meta:
        model = DonationGroup
        ordering = ['title']
