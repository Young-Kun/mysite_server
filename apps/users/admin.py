from django.contrib import admin
from .models import UserProfile, VerifyCode


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'nickname', 'mobile', 'is_staff', 'is_active']


@admin.register(VerifyCode)
class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'mobile', 'add_time']
