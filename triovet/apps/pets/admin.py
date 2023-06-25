from django.contrib import admin

from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("patient_name", "name", "type",)
    fields = ("patient", "name", "type",)
    search_fields = ("name", "type",)

    def patient_name(self, obj):
        return obj.patient.name
