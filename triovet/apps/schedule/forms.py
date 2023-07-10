from django import forms

from triovet.apps.schedule.models import DATE_CHOICES, TIME_CHOICES


def phone_number_validation(number):
    if number[0:3] == "375":
        if number[3:5] == "17" or number[3:5] == "29" or number[3:5] == "33" or number[3:5] == "44":
            if len(number) == 12:
                pass
            else:
                raise forms.ValidationError("Number is too long!")
        else:
            raise forms.ValidationError("Enter correct number!")
    else:
        raise forms.ValidationError("Enter correct number!")


class NewAppointmentForm(forms.Form):
    day = forms.ChoiceField(choices=DATE_CHOICES)
    time = forms.ChoiceField(choices=TIME_CHOICES)
    phone = forms.CharField(max_length=13, validators=[phone_number_validation])
