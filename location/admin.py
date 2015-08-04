from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('state', 'township', 'district')
    fieldsets = [
        (None, {'fields': [
            'district',
            'township',
            'latitude',
            'longitude',
            'state',
            'description',
            'total_male',
            'total_female',
            'urban_total_male',
            'urban_total_female',
            'rural_total_male',
            'rural_total_female',
        ]}),
    ]

admin.site.register(Location, LocationAdmin)

