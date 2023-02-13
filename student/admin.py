from django.contrib import admin

from student.models import Course, Session_Year, Student

# Register your models here.

admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)

