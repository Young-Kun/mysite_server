from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins

from custom.utils import send_verify_code_by_email, generate_code
from mysite_server.settings import CODE_LENGTH
from .models import UserProfile, VerifyCode
from .serializers import UserRegisterSerializer, VerifyCodeSerializer
from rest_framework.response import Response
from rest_framework import status


class VerifyCodeViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    短信或邮箱验证码
    """
    serializer_class = VerifyCodeSerializer


class UserRegisterViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    用户注册
    """
    serializer_class = UserRegisterSerializer
