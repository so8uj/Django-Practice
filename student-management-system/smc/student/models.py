from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    department = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)
    address = models.TextField(max_length=300)
    enrolled_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department