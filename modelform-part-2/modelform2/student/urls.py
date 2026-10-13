from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.student_add, name="student_add"),
    path('list/', views.student_list, name="student_list"),
    path('view/<int:pk>/', views.student_detail, name="student_detail"),
    path('edit/<int:pk>/', views.student_edit, name="student_edit"),
    path('delete/<int:pk>/', views.student_delete, name="student_delete"),
]