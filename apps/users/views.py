from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from .serializers import UserRegisterSerializer, VerifyCodeSerializer


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
