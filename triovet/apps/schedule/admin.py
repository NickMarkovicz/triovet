from django.contrib import admin

from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("time", "day",)
    fields = ("time", "day", "patient", "doctor",)
    search_fields = ("day", "patient", "doctor",)