from django.shortcuts import render
from passengerApp.models import Passenger

# Create your views here.
def passengerdata(request):
    passengers=Passenger.objects.all()
    passDict={'passengers':passengers}
    return render(request,'passenger.html',passDict)