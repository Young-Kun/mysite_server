from rest_framework.viewsets import ModelViewSet, GenericViewSet, mixins

from custom.utils import send_verify_code_by_email, generate_code
from mysite_server.settings import CODE_LENGTH
from .models import UserProfile, VerifyCode
from .serializers import UserProfileSerializer, VerifyCodeSerializer
from rest_framework.response import Response
from rest_framework import status


class VerifyCodeViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    短信或邮箱验证码
    """
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.validated_data['account']
        account_type = serializer.validated_data['account_type']
        verify_code = generate_code(CODE_LENGTH)
        headers = self.get_success_headers(serializer.validated_data)
        if account_type == 'email':
            send_status = send_verify_code_by_email(verify_code, [account, ])
            if send_status:
                # self.perform_create(serializer)
                vcode = VerifyCode(code=verify_code, account=account, account_type=account_type)
                vcode.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response('验证码发送失败', status=status.HTTP_400_BAD_REQUEST, headers=headers)
        if account_type == 'mobile':
            return Response(0)
        return Response('账号必须是手机或邮箱！', status=status.HTTP_400_BAD_REQUEST, headers=headers)


class UserRegisterViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
