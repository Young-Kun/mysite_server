from django.contrib import admin
from .models import School, Teacher


@admin.register(School)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'introduction', 'add_time']


@admin.register(Teacher)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'name', 'features', 'add_time']
