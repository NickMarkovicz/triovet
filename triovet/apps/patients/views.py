from django.shortcuts import render

from triovet.apps.patients.models import Patient
from triovet.apps.schedule.models import Schedule
from triovet.apps.pets.models import Pet

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def profile(request):
    if request.method == "GET":
        pet_list = Pet.objects.filter(patient__user__id=request.GET.get("user_id"))
        patient = Patient.objects.get(user=request.user)
        appointments = Schedule.objects.filter(patient_id=patient.id)
        return render(request, "patient_profile.html", {"pet_list": pet_list, "appointments": appointments})
