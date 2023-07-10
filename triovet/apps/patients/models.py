from django.conf import settings
from django.db import models


class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name
