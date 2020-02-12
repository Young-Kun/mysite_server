from django.contrib import admin
from .models import BlogCategory, BlogTag, Article


@admin.register(BlogCategory)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'add_time']


@admin.register(BlogTag)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'add_time']


@admin.register(Article)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'tags', 'user', 'title', 'add_time']
