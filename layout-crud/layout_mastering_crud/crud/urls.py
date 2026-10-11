from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='todo_index'),
    path('manage/todos/<str:type>/', views.create_todo, name='create_todo'),
    path('manage/todos/<str:type>/<int:id>/', views.update_todo, name='update_todo'),
    path('submit/todo', views.submit_todo, name='submit_todo'),
    path('manage/toggle-status/<int:id>/', views.toggle_status, name='toggle_status'),
    path('manage/delete-todo/<int:id>/', views.delete_todo, name='delete_todo'),
]