from django.forms import widgets
from rest_framework import serializers
from .models import DonationGroup


class DonationGroupSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['title'] = strip_tags(validated_data['title'])
        validated_data['description'] = strip_tags(validated_data['description'])
        return DonationGroup.objects.create(**validated_data)


    class Meta:
        model = DonationGroup
