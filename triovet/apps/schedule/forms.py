from django import forms

from triovet.apps.schedule.models import DATE_CHOICES, TIME_CHOICES


class NewAppointmentForm(forms.Form):
    day = forms.ChoiceField(choices=DATE_CHOICES)
    time = forms.ChoiceField(choices=TIME_CHOICES)
    phone = forms.CharField(max_length=13)
