from django import forms


class NewDiagnosisForm(forms.Form):
    title = forms.CharField(max_length=64)
    note = forms.CharField(max_length=1000, widget=forms.Textarea)