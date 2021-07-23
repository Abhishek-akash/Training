from django.contrib import admin

# Register your models here.
from django.contrib import admin
from User.models import Teacher, Subject, Student

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Student)
