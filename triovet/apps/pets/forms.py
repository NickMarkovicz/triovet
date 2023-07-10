from django import forms

from triovet.apps.pets.models import PET_CHOICES


class NewPetForm(forms.Form):
    pet_name = forms.CharField(max_length=64)
    type = forms.ChoiceField(choices=PET_CHOICES)
