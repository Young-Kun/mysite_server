from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

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
        # 生成token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        ret_data = {'nickname': user.nickname, 'userid': user.id, 'token': token}
        ret_data.update(serializer.data)
        return Response(ret_data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()  # 返回创建的UserProfile实例
