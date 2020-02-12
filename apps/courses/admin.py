from django.contrib import admin
from .models import Course, CourseCategory


@admin.register(CourseCategory)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'category_type', 'parent', 'add_time']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'school', 'teacher', 'title', 'introduction', 'add_time']
