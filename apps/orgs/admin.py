from django.contrib import admin
from .models import School, Teacher


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'introduction', 'add_time']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'school', 'features', 'add_time']
