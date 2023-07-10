from django.shortcuts import render
from django.contrib.auth import get_user_model

from triovet.apps.patients.models import Patient
from triovet.apps.pets.forms import NewPetForm
from triovet.apps.pets.models import Pet

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def new_pet(request):
    if request.method == "POST":
        form = NewPetForm(request.POST)
        if form.is_valid():
            patient = Patient.objects.get(user=request.user)
            pet_name = request.POST.get("pet_name")
            type = request.POST.get("type")
            Pet.objects.create(patient_id=patient.id, name=pet_name, type=type)
            form = NewPetForm()
            return render(request, "new_pet.html", {"form": form, "pet_name": pet_name, "type": type})
        else:
            form = NewPetForm()
            return render(request, "new_pet.html", {"form": form})
    else:
        form = NewPetForm()
        return render(request, "new_pet.html", {"form": form})
