from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'district',
            'township',
            'latitude',
            'longitude',
            'type',
        ]}),
    ]

admin.site.register(Location, LocationAdmin)

