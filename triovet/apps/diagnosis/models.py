from django.conf import settings
from django.db import models


class Diagnosis(models.Model):
    schedule = models.OneToOneField("schedule.Schedule", on_delete=models.CASCADE)
    title = models.CharField(max_length=64, default=None)
    note = models.TextField(default=None)

    def __str__(self):
        return self.title
