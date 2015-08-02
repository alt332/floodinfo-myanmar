from django.contrib import admin
from .models import Newsfeed


@admin.register(Newsfeed)
class NewsfeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'spam_report_count', 'posted_time')
    readonly_fields = ('spam_report_count', )
    fieldsets = [
        (None, {'fields': [
            'show_hide',
            'spam_report_count',
            'title',
            'description',
            'dam_condition',
            'river_condition',
            'posted_time'
        ]}),
    ]
