from django.forms import widgets
from django.utils.html import strip_tags
from rest_framework import serializers
from .models import Newsfeed


class NewsfeedSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['title'] = strip_tags(validated_data['title'])
        validated_data['description'] = strip_tags(validated_data['description'])
        return Newsfeed.objects.create(**validated_data)


    class Meta:
        model = Newsfeed
