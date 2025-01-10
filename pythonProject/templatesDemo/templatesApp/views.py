from django.shortcuts import render


def rendertemplate(request):
    mydict = {"name":"django"}
    return render(request,'templatesApp/firstTemplate.html',context=mydict)

def renderEmployee(request):
    emp = {"id":"102","name":"Rex","salary":1000}
    return render(request,'templatesApp/employeTemplate.html',emp)

# Create your views here.
