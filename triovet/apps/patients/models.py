from django.conf import settings
from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
