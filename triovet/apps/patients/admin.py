from django.contrib import admin

from .models import Patient
from ..pets.models import Pet


class PetAdminInline(admin.TabularInline):
    model = Pet


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name", "address", "phone",)
    search_fields = ("name",)
    inlines = (PetAdminInline,)
