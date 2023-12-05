from django.contrib import admin
from .models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description_short')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date'  # This adds a date drill down navigation by date hierarchy

    # This is a method to display a shortened description in the admin list view
    def description_short(self, obj):
        return obj.description[:75] + '...' if len(obj.description) > 75 else obj.description
    description_short.short_description = 'Description'


admin.site.register(Activity, ActivityAdmin)
