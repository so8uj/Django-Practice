from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.index, name='index'),
    path('create',views.create_teacher,name='create_teacher'),
    path('update/<int:pk>',views.update_teacher,name='update_teacher')
]