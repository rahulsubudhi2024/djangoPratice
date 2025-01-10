from django.shortcuts import render
from . import forms

# Create your views here.

def loginRegistrationView(request):
    login = forms.loginRegistration()
    if request.method == "POST":
        login = forms.loginRegistration(request.POST)
        if login.is_valid():
            print("login is Valid")
            print("User Name",login.cleaned_data['userName'])
            print("Password",login.cleaned_data['password'])
    return render(request,'loginRegistration.html',{'login':login})            

