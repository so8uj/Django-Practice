from django.shortcuts import render, redirect
from django.contrib import messages
from .models  import Student
def index(request):
    students = Student.objects.all()
    return render(request, 'student/index.html', {'students': students})


def add_student(request):
    student = Student(status=True)
    message = {}

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll = request.POST.get('roll')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.status = request.POST.get('status')

        if not student.name or not student.roll or not student.email or not student.age :
            messages.error(request, "All fields are required!")
        else:
            student.save()
            messages.success(request, 'Student created successfully!')
            return redirect('student:index')
            
    return render(request, 'student/add_student.html',{'student':student})
