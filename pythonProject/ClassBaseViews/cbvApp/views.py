from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class Greetigview(View):
    greetingMessage = "firstview"
    def get(self,request):
        return HttpResponse(self.greetingMessage)