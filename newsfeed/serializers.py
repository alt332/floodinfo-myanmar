from django.forms import widgets
from rest_framework import serializers
from .models import Newsfeed


class NewsfeedSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Newsfeed.objects.create(**validated_data)


    class Meta:
        model = Newsfeed
