from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.contrib import messages
from .models import Student


def index(requst):

    students = Student.objects.all()

    return render(requst,'index.html',{'students':students})


def load_student_form(request,action,id=0):

    student = {}
    if action == 'edit' or action == 'delete':
        student = student = get_object_or_404(Student, id=id)
        if action == 'delete':
            return render(request,'include/student_delete_form.html',{'student':student})

    return render(request,'include/student_form.html',{'action':action,'student':student})

def create_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        email = request.POST.get('email')

        if name and roll and email:

            Student.objects.create(
                name = name,
                roll = roll,
                email = email
            )
            messages.success(request, f"Student {name} saved to database.")
            return redirect('index')
        
        messages.error(request, "All Fields are required!")
        return redirect('index')
   
    return HttpResponse(f"Get Method is not Supported for the route!", 405)

def update_student(request,id):
    if request.method == 'POST':

        student = get_object_or_404(Student,pk=id)

        name = request.POST.get('name')
        roll = request.POST.get('roll')
        email = request.POST.get('email')

        if name and roll and email:

            student.name = name
            student.roll = roll
            student.email = email
            student.save()
            messages.success(request, f"Student {name} updated to database.")
            return redirect('index')
        
        messages.error(request, "All Fields are required!")
        return redirect('index')
   
    return HttpResponse(f"Get Method is not Supported for the route!", 405)


def delete_student(request,id):
    if request.method == 'POST':
        student = get_object_or_404(Student,pk=id)
        student.delete()
        messages.success(request, "Student deleted.")
        return redirect('index')
    
    return HttpResponse(f"Get Method is not Supported for the route!", 405)