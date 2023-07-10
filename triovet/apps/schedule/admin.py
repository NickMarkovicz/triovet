from django.contrib import admin

from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("day", "time", "status",)
    fields = ("day", "time", "phone", "patient", "status",)
    search_fields = ("day", "status",)
