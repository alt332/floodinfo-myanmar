from django.contrib import admin
from .models import DonationGroup


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


admin.site.register(DonationGroup, DonationGroupAdmin)
