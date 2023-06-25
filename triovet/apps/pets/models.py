from django.conf import settings
from django.db import models

PET_CHOICES = (("CAT", "Cat"), ("DOG", "Dog"), ("CAPYBARA", "Capybara"))


class Pet(models.Model):
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, related_name="pets")
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=16, choices=PET_CHOICES, default=None)

    def __str__(self):
        return f"{self.name} ({self.type.capitalize()})"
