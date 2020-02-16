import re

from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mysite_server.settings import REGEX_MOBILE, REGEX_EMAIL
from .models import UserProfile, VerifyCode

User = get_user_model()


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'is_staff', 'is_active', 'nickname', 'mobile', 'introduction',
                  'avatar', 'address', 'birthday', 'date_joined']


class VerifyCodeSerializer(ModelSerializer):
    def validate(self, attrs):
        account_type = attrs['account_type']
        account = attrs['account']
        # 账号是否已存在
        if User.objects.filter(Q(mobile=account) | Q(email=account)).exists():
            raise serializers.ValidationError('用户已被注册')
        # 验证手机号格式
        if account_type == 'mobile':
            if not re.match(REGEX_MOBILE, account):
                raise serializers.ValidationError('手机号码格式错误')
        # 验证邮箱格式
        else:
            if not re.match(REGEX_EMAIL, account):
                raise serializers.ValidationError('邮箱格式错误')
        return attrs

    class Meta:
        model = VerifyCode
        fields = ['account', 'account_type']
