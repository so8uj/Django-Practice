from django.shortcuts import render

from .froms import TeacherForm

def index(request):

    form = TeacherForm()

    return render(request, 'index.html', {'form': form})