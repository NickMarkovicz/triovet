from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponse

from triovet.apps.patients.models import Patient
from triovet.apps.users.forms import SignUpForm, SignInForm
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            if User.objects.filter(email=request.POST.get("email")):
                exists = True
                form = SignUpForm()
                return render(request, "sign_up.html", {"form": form, "exists": exists})
            else:
                user = User(
                    email=form.cleaned_data["email"],
                )
                user.set_password(form.cleaned_data["password"])
                user.save()

                patient = Patient(user_id=user.id, name=form.cleaned_data["name"], address=form.cleaned_data["address"])
                patient.save()
                return redirect("sign_in")
    else:
        form = SignUpForm()
    return render(request, "sign_up.html", {"form": form})


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is None:
                bad_login = True
                return render(request, "sign_in.html", {"form": form, "bad_login": bad_login})
            login(request, user)
            return redirect("index")
    else:
        form = SignInForm()
    return render(request, "sign_in.html", {"form": form})


def sign_out(request):
    logout(request)
    return redirect("index")
