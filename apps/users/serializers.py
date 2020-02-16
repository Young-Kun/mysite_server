import re
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from custom.textfilter.filter import DFAFilter, keyword_path
from custom.utils import generate_code, send_verify_code_by_email
from mysite_server.settings import REGEX_MOBILE, REGEX_EMAIL, MAX_ACCOUNT_LENGTH, CODE_LENGTH, CODE_EXPIRES
from .models import UserProfile, VerifyCode, ACCOUNT_TYPE

User = get_user_model()


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'is_staff', 'is_active', 'nickname', 'mobile', 'introduction',
                  'avatar', 'address', 'birthday', 'date_joined']


class VerifyCodeSerializer(ModelSerializer):
    class Meta:
        model = VerifyCode
        fields = ['account', 'account_type']

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
        # 生成验证码并加入validated_data
        verify_code = generate_code(CODE_LENGTH)
        if account_type == 'mobile':
            raise serializers.ValidationError('手机发短信要收费，暂不支持，求赞助')
        else:
            send_status = send_verify_code_by_email(verify_code, [account, ])
            if send_status:
                attrs['code'] = verify_code
            else:
                raise serializers.ValidationError('验证码发送失败')
        return attrs


class UserRegisterSerializer(ModelSerializer):
    """
    用户注册
    """
    account_type = serializers.ChoiceField(required=True, write_only=True, choices=ACCOUNT_TYPE, label='账号类型')
    account = serializers.CharField(required=True, write_only=True, max_length=MAX_ACCOUNT_LENGTH, label='账号')
    code = serializers.CharField(required=True, write_only=True, label='验证码')

    class Meta:
        model = UserProfile
        fields = ['account_type', 'account', 'code', 'username', 'password']

    def validate_code(self, code):
        account_type = self.initial_data['account_type']
        account = self.initial_data['account']
        codes = VerifyCode.objects.filter(account_type=account_type, account=account)
        if codes.exists():
            newest_code = codes.order_by('-add_time').first()
            five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=CODE_EXPIRES, seconds=0)
            if newest_code.code != code:
                raise serializers.ValidationError('验证码错误')
            if five_minutes_ago > newest_code.add_time:
                raise serializers.ValidationError('验证码已过期，请重新发送')
            # 验证通过
            return 1
        else:
            raise serializers.ValidationError('验证码不存在，请先发送验证码')

    def validate_username(self, username):
        tf = DFAFilter()
        tf.parse(keyword_path)
        filtered_username = tf.filter(username)
        if '*' in filtered_username:
            is_sensitive = True
        else:
            is_sensitive = False
        print(is_sensitive, filtered_username)
        if is_sensitive:
            raise serializers.ValidationError('用户名含有敏感字符：' + filtered_username)
        else:
            return username

    def validate(self, attrs):
        account_type = attrs['account_type']
        if account_type == 'email':
            attrs['email'] = attrs['account']
        if account_type == 'mobile':
            attrs['mobile'] = attrs['account']
        attrs['nickname'] = attrs['username']
        del attrs['code']
        del attrs['account_type']
        del attrs['account']
        attrs['password'] = make_password(attrs['password'])
        return attrs
