from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(max_length=10)
    email = models.EmailField(unique=True)