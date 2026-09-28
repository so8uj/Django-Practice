from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('home-pip/', views.index_pip,name="index_pip"),
    path('home-tailwind/', views.index_tailwind,name="index_tailwind"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
]
