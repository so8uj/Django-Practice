from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('load-student-form/<str:action>/<int:id>', views.load_student_form, name='load_student_form'),
    path('create-sudent', views.create_student,name='create_student'),
    path('update-sudent/<int:id>', views.update_student,name='update_student'),
    path('delete-student/<int:id>', views.delete_student, name='delete_student')
]