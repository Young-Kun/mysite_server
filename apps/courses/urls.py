from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseCategoryViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'coursecategries', CourseCategoryViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls))
]