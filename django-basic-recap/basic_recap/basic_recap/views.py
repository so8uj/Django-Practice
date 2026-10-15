from django.shortcuts import render
from student.models import Student

def home(request):
    context = {
        'total_students': Student.objects.count(),
    }
    return render(request, 'home.html', context)