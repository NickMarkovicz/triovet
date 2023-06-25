from datetime import date, datetime, timedelta
from django.utils import timezone

from django.shortcuts import render

from triovet.apps.schedule.models import Schedule


def calculate_current_week():
    start_date = datetime.now()
    end_date = start_date + timedelta(days=7)
    items = [start_date]
    week_str = []

    while start_date < end_date:
        start_date += timedelta(days=1)
        items.append(start_date)

    for date in items:
        week_str.append(date.strftime("%B %d, %A"))

    return week_str


def appointments(request):
    current_appointments = Schedule.objects.filter(day__range=[date.today(), date.today() + timedelta(days=7)])
    current_week = calculate_current_week()
    return render(request, "appointments.html", {"current_appointments": current_appointments, "current_week": current_week})


def confirm_appointment(request):
    return render(request, "confirm_appointment.html")
