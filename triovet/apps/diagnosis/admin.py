from django.contrib import admin

from .models import Diagnosis


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ("schedule", "title",)
    fields = ("schedule", "title", "note",)
    search_fields = ("schedule", "title", "patients_name")
