from django.contrib import admin
from .models import DonationGroup


# class PhoneNumberInline(admin.StackedInline):
#     model = PhoneNumber
#     extra = 1


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
    # inlines = [PhoneNumberInline]


admin.site.register(DonationGroup, DonationGroupAdmin)
