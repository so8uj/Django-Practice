from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    