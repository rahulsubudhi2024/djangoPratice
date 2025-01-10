from django.contrib import admin
from passengerApp.models import Passenger

# Register your models here.

class PassengerAdmin(admin.ModelAdmin):
    list_display=['firstName','lastName','email','rewardPoints']

admin.site.register(Passenger,PassengerAdmin)
