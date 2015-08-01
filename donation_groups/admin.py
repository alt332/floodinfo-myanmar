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
    readonly_fields = ('spam_report_count',)
    fieldsets = [
        (None, {'fields': [
            'show_hide',
            'spam_report_count',
            'title',
            'description',
        ]}),
    ]


admin.site.register(DonationGroup, DonationGroupAdmin)
admin.site.register(Newsfeed, NewsfeedAdmin)
