from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def index_pip(request):
    return render(request,'index_pip.html')

def index_tailwind(request):
    return render(request,'index_tailwind.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')