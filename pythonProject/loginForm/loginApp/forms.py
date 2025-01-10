from django import forms
from django.core import validators


class loginRegistration(forms.Form):
    userName = forms.CharField(validators=[validators.MaxLengthValidator(15)])
    password = forms.CharField(widget=forms.PasswordInput,
                               validators=[validators.MinLengthValidator(5)])
    
    def clean_password(self):
        inputPassword = self.cleaned_data['password']
        if not any(char.isupper() for char in inputPassword):
            raise forms.ValidationError("The password must contain at least one uppercase letter.")
        return inputPassword