from rest_framework.viewsets import ModelViewSet
from .models import CourseCategory, Course
from .serializers import CourseCategorySerializer, CourseSerializer


class CourseCategoryViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
