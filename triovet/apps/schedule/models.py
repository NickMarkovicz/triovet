from datetime import datetime, timedelta, date
from django.utils import timezone

from django.conf import settings
from django.db import models

SCHEDULE_CHOICES = (
    ("08.00", "08.00"),
    ("08.30", "08.30"),
    ("09.00", "09.00"),
    ("09.30", "09.30"),
    ("10.00", "10.00"),
    ("10.30", "10.30"),
    ("11.00", "11.00"),
    ("11.30", "11.30"),
    ("12.00", "12.00"),
    ("12.30", "12.30"),
    ("13.00", "13.00"),
    ("13.30", "13.30"),
    ("14.00", "14.00"),
    ("14.30", "14.30"),
    ("15.00", "15.00"),
    ("15.30", "15.30"),
    ("16.00", "16.00"),
    ("16.30", "16.30"),
    ("17.00", "17.00"),
    ("17.30", "17.30"),
    ("18.00", "18.00"),
)


class Schedule(models.Model):
    time = models.CharField(max_length=64, choices=SCHEDULE_CHOICES, blank=True, null=True, unique=True)
    day = models.DateField(blank=True, null=True)
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, related_name="patients")
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE, related_name="doctors")

    def __str__(self):
        return f"Appointment: {self.time} / Patient: {self.patient} / Doctor: {self.doctor}"
