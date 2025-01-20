from django.shortcuts import redirect, render
from fbvApp.models import Student
from fbvApp.forms import StudentForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import logout as auth_logout
# Create your views here.

@login_required
def getStudents(request):
    students = Student.objects.all()
    return render(request,'index.html',{'students':students})

@login_required
def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'create.html',{"form":form})

@login_required
@permission_required('fbvApp.delete_student')
def deleteStudent(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')

@login_required
def updateStudent(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update.html',{'form':form})

def logout(request):
    return redirect('/')