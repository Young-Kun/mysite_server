from django.contrib import admin
from .models import BlogCategory, BlogTag, Article


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'add_time']


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'add_time']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'user', 'click_num', 'add_time', 'modify_time']
