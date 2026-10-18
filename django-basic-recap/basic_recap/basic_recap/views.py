from django.shortcuts import render
from student.models import Student
from teacher.models import Teacher

def home(request):
    context = {
        'total_students': Student.objects.count(),
        'total_teachers': Teacher.objects.count()
    }
    return render(request, 'home.html', context)