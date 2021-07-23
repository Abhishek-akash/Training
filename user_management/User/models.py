from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=512)

class Teacher(models.Model):
    name = models.CharField(max_length=512)

class Student(models.Model):
    name = models.CharField(max_length=512)
    sub = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
