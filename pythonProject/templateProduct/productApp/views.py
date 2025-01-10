from django.shortcuts import render

# Create your views here.

def eletronics(request):
    dict = {
        "product1": "iphone",
        "product2": "mac",
        "product3": "dell"
    }
    return render(request,'products.html',dict)

def toys(request):
    dict = {
        "product1": "drone",
        "product2": "lego",
        "product3": "popit"
    }
    return render(request,'products.html',dict)

def shoes(request):
    dict = {
        "product1": "lv",
        "product2": "nike",
        "product3": "addidas"
    }
    return render(request,'products.html',dict)

def index(request):
    return render(request,'index.html')