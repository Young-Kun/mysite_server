from django.contrib import admin
from .models import Course, CourseCategory


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'category_type', 'parent', 'add_time']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'school', 'teacher', 'introduction', 'add_time']
