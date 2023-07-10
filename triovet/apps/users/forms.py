from django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    name = forms.CharField(max_length=64)
    address = forms.CharField(max_length=128)


class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
