from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models  import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'student/index.html', {'students': students})


def add_student(request):
    student = Student(roll='',age='',status=True)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll = request.POST.get('roll')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.status = bool(int(request.POST.get('status')))

        if not student.name or not student.roll or not student.email or not student.age :
            messages.error(request, "All fields are required!")
        else:
            student.save()
            messages.success(request, 'Student created successfully!')
            return redirect('student:index')
            
    return render(request, 'student/add_student.html',{'student':student})



def edit_student(request, pk):

    student = get_object_or_404(Student,pk=pk)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll = request.POST.get('roll')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.status = bool(int(request.POST.get('status')))

        if not student.name or not student.roll or not student.email or not student.age :
            messages.error(request, "All fields are required!")
        else:
            student.save()
            messages.success(request, 'Student Edited successfully!')
            return redirect('student:index')


    return render(request, 'student/edit_student.html',{'student':student})

def toggle_status(request,pk):
    student = get_object_or_404(Student,pk=pk)
    student.status = not student.status
    student.save()
    messages.success(request, 'Student Status Updated successfully!')
    return redirect('student:index')


def delete_student(request, pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.error(request, 'Student Deleted!')
        return redirect('student:index')

    return render(request,'student/delete_student.html',{'student':student})