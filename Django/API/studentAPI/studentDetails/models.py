from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    course = models.CharField(max_length=300)
    college = models.CharField(max_length=300)

    def __str__(self):
        return self.name


