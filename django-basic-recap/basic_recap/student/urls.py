from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>',views.edit_student,name='edit_student'),
    path('student-status/<int:pk>',views.toggle_status,name='toggle_status'),
    path('delete/<int:pk>',views.delete_student,name='delete_student'),
]