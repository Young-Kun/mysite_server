from rest_framework.viewsets import ModelViewSet
from .models import UserProfile, VerifyCode
from .serializers import UserProfileSerializer, VerifyCodeSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class VerifyCodeViewSet(ModelViewSet):
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodeSerializer
