from rest_framework.serializers import HyperlinkedModelSerializer
from .models import UserProfile, VerifyCode


class UserProfileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['url', 'id', 'username', 'email', 'is_staff', 'is_active', 'nickname', 'mobile', 'introduction',
                  'avatar', 'address', 'birthday', 'date_joined']


class VerifyCodeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = VerifyCode
        fields = ['url', 'id', 'code', 'mobile', 'add_time']
