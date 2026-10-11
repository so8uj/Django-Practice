from os import name

from django.http import request, HttpResponse
from django.shortcuts import redirect, render , get_object_or_404

from .models import Todo

def index(request):

    todos = Todo.objects.all()

    return render(request,'todos.html', {'todos': todos})

def create_todo(request,type):

    context = {
        'type': type,
        'name': '',
        'description': '',
        'status': 0
    }

    return render(request,'manage_todo.html', context)

def submit_todo(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        status = bool(int(request.POST.get('status', 0)))
        form_type = request.POST.get('form_type')

        # return HttpResponse(f"requst data: {request.POST.dict()}, status: {status}, form_type: {form_type}")
        
        if(form_type == 'edit'):
            todo_id = request.POST.get('todo_id')
            todo = get_object_or_404(Todo, id=todo_id)
            todo.title = title
            todo.description = description
            todo.status = status
            todo.save()
        else:
            Todo.objects.create(title=title, description=description, status=status)

        return redirect('todo_index')
    
    return render(request,'create_todo.html')
    

def update_todo(request,type,id):

    todo = get_object_or_404(Todo, id=id)

    context = {
        'id': id,
        'type': type,
        'name': todo.title,
        'description': todo.description,
        'status': int(todo.status)
    }
    return render(request,'manage_todo.html', context) 

def toggle_status(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.status = not todo.status
    todo.save()
    return redirect('todo_index')

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_index')