from django.contrib import admin
from .models import DonationGroup, Newsfeed


class DonationGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'title',
            'description',
            'phone_numbers',
            'facebook_url',
            'donation_location',
        ]}),
    ]


class NewsfeedAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'title',
            'description',
        ]}),
    ]


admin.site.register(DonationGroup, DonationGroupAdmin)
admin.site.register(Newsfeed, NewsfeedAdmin)
