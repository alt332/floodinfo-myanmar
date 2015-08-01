from django.forms import widgets
from rest_framework import serializers
from .models import DonationGroup, Newsfeed


class DonationGroupSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return DonationGroup.objects.create(**validated_data)


    class Meta:
        model = DonationGroup


class NewsfeedSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Newsfeed.objects.create(**validated_data)


    class Meta:
        model = Newsfeed
