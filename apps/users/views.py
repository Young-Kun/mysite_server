from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token = ''
        ret_data = {'username': user.username, 'userid': user.id, 'token': token}
        return Response(ret_data, status=status.HTTP_201_CREATED, headers=headers)
