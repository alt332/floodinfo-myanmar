from django.forms import widgets
from rest_framework import serializers
from .models import DonationGroup


class DonationGroupSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return DonationGroup.objects.create(**validated_data)


    class Meta:
        model = DonationGroup
