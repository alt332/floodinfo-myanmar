from django.contrib import admin
from .models import DonationGroup, PhoneNumber


class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 1


class DonationGroupAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberInline]


admin.site.register(DonationGroup, DonationGroupAdmin)
