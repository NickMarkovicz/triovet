from datetime import datetime, timedelta

from django.db import models


def get_current_week():
    start_date = datetime.now()
    end_date = start_date + timedelta(days=6)
    datetime_objects = [start_date]
    date_objects = []
    date_choices = ()

    while start_date < end_date:
        start_date += timedelta(days=1)
        datetime_objects.append(start_date)

    for datetime_obj in datetime_objects:
        date_obj = datetime_obj.date()
        date_objects.append(date_obj)

    for obj in date_objects:
        date = (f"{obj.strftime('%d/%m/%Y')}", f"{obj.strftime('%B %-d, %A')}")
        date_choices_temp = list(date_choices)
        date_choices_temp.append(date)
        date_choices = tuple(date_choices_temp)

    return date_choices


TIME_CHOICES = (
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

DATE_CHOICES = get_current_week()

STATUS_CHOICES = (("PENDING", "Pending"), ("APPROVED", "Approved"), ("HELD", "Held"),)


class Schedule(models.Model):
    day = models.CharField(max_length=10, choices=DATE_CHOICES, blank=True, null=True)
    time = models.CharField(max_length=64, choices=TIME_CHOICES, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="PENDING")
    # patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, related_name="patients")
    # doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE, related_name="doctors")

    def __str__(self):
        return f"Day: {self.day} / Time: {self.time}"
