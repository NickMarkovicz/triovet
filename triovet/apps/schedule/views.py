from django.shortcuts import render, redirect
from django.http import HttpResponse

from triovet.apps.schedule.models import Schedule, DATE_CHOICES
from triovet.apps.schedule.forms import NewAppointmentForm
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def appointments(request):
    if request.method == "GET":
        if request.GET.get("status") is not None:
            status = request.GET.get("status")
            appointments = Schedule.objects.filter(status=request.GET.get("status"))
            return render(request, "appointments.html", {"appointments": appointments, "status": status})
        else:
            appointments = Schedule.objects.all()
            return render(request, "appointments.html", {"appointments": appointments})
    else:
        return redirect("appointments")


def delete_appointment(request, appointment_id):
    if request.method == "POST":
        Schedule.objects.filter(id=appointment_id).delete()
        return redirect("appointments")


def approve_appointment(request, appointment_id):
    if request.method == "POST":
        Schedule.objects.filter(id=appointment_id).update(status="APPROVED")
        return redirect("appointments")


def new_appointment(request):
    dates = DATE_CHOICES
    if request.method == "POST":
        form = NewAppointmentForm(request.POST)
        if form.is_valid():
            day = request.POST.get("day")
            time = request.POST.get("time")
            phone = request.POST.get("phone")
            Schedule.objects.get_or_create(day=day, time=time,
                                           phone=phone)
            form = NewAppointmentForm()
            return render(request, "new_appointment.html", {"form": form, "day": day, "time": time, "phone": phone})
        else:
            form = NewAppointmentForm(request.POST)
    else:
        form = NewAppointmentForm()
    return render(request, "new_appointment.html", {"form": form, "dates": dates})
