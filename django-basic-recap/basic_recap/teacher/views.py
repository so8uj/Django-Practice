from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .models import Teacher
from .forms import teacherForm
def index(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/index.html' , {'teachers':teachers})

def create_teacher(request):

    teacherform = teacherForm()
    if request.method == 'POST':
        teacherform = teacherForm(request.POST)
        if teacherform.is_valid:
            teacherform.save()
            teacherform = teacherForm(request.POST)
            messages.success(request,"Teacher Added!")
            return redirect('teacher:index')
        
    return render(request, 'teacher/create_teacher.html', {'teacherform':teacherform})


def update_teacher(request,pk):

    teacher = get_object_or_404(Teacher,pk=pk)
    teacherform = teacherForm(instance=teacher)

    if request.method == 'POST':
        teacherform = teacherForm(request.POST, instance=teacher)
        
        if teacherform.is_valid():
            teacherform.save()
            messages.success(request,"Teacher Updated!")
            return redirect('teacher:index')


    return render(request, 'teacher/update_teacher.html', {'teacherform':teacherform})