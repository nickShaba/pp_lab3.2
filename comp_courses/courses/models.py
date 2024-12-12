from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
