from django.shortcuts import get_object_or_404, render
from .forms import StudentForm
from .models import Student

def student_add(request):

    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()

            context = {
                'success_message': 'Student added successfully!',
                'success_details': 'The student has been added to the database.'
            }

            return render(request,'student_success.html', context)

    return render(request,'student_form.html' , {'form':form,'form_type':'add'})


def student_list(request):
    students = Student.objects.all()
    return render(request,'student_list.html',{'students':students})


def student_detail(request,pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request,'student_detail.html',{'student':student})

def student_edit(request,pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return render(request,'student_success.html', {'success_message': 'Student updated successfully!', 'success_details': 'The student has been updated in the database.'})
   
    return render(request,'student_form.html',{'form':form,'form_type':'edit'})



def student_delete(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return render(request,'student_success.html', {'success_message': 'Student deleted successfully!', 'success_details': 'The student has been deleted from the database.'})
    return render(request,'student_confirm_delete.html',{'student':student})
