from rest_framework.serializers import ModelSerializer
from .models import UserProfile, VerifyCode


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'is_staff', 'is_active', 'nickname', 'mobile', 'introduction',
                  'avatar', 'address', 'birthday', 'date_joined']


class VerifyCodeSerializer(ModelSerializer):
    class Meta:
        model = VerifyCode
        fields = ['id', 'code', 'mobile', 'add_time']
