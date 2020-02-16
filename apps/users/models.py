from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from mysite_server.settings import MAX_ACCOUNT_LENGTH

ACCOUNT_TYPE = (
    ('email', '邮箱'),
    ('mobile', '手机'),
)


class UserProfile(AbstractUser):
    """
    用户
    """
    nickname = models.CharField(max_length=20, null=True, blank=True, verbose_name='昵称')
    mobile = models.CharField(max_length=11, null=True, blank=True, unique=True, verbose_name='手机号码')
    email = models.CharField(max_length=MAX_ACCOUNT_LENGTH, null=True, blank=True, unique=True, verbose_name='邮箱')
    introduction = models.TextField(null=True, blank=True, default='该用户很懒，啥也没写...', verbose_name='简介')
    avatar = models.ImageField(upload_to='users/avatars/', null=True, blank=True, default='', verbose_name='头像')
    address = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name='地址')
    birthday = models.DateField(null=True, blank=True, default=timezone.now, verbose_name='生日')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['-date_joined']

    def __str__(self):
        return self.username

    def get_profile_name(self):
        return self.nickname if self.nickname else self.username


class VerifyCode(models.Model):
    """
    短信或邮箱验证码
    """
    code = models.CharField(max_length=10, verbose_name='验证码')
    account = models.CharField(max_length=MAX_ACCOUNT_LENGTH, default='', verbose_name='账号')
    account_type = models.CharField(max_length=6, choices=ACCOUNT_TYPE, default='email', verbose_name='账号类型')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = '验证码'
        ordering = ['-add_time']

    def __str__(self):
        return self.code
