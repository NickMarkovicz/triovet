from django.shortcuts import render, redirect

from triovet.apps.diagnosis.models import Diagnosis
from triovet.apps.diagnosis.forms import NewDiagnosisForm


def new_diagnosis(request):
    if request.method == "POST":
        form = NewDiagnosisForm(request.POST)
        if form.is_valid():
            title = request.POST.get("title")
            note = request.POST.get("note")
            Diagnosis.objects.create(schedule_id=request.GET.get("appointment_id"), title=title, note=note)
            return render(request, "appointments.html")
    else:
        form = NewDiagnosisForm()
        return render(request, "new_diagnosis.html", {"form": form})
