from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins
from .models import UserProfile, VerifyCode
from .serializers import UserProfileSerializer, VerifyCodeSerializer
from rest_framework.response import Response
from rest_framework import status


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class VerifyCodeViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    短信或邮箱验证码
    """
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
