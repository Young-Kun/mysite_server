"""mysite_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from .settings import MEDIA_ROOT
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
# 引入视图
from blogs.views import BlogCategoryViewSet, BlogTagViewSet, ArticleViewSet
from courses.views import CourseCategoryViewSet, CourseViewSet
from orgs.views import SchoolViewSet, TeacherViewSet
from users.views import UserProfileViewSet, VerifyCodeViewSet

# 注册视图
router = DefaultRouter()
router.register(r'blog-categories', BlogCategoryViewSet)
router.register(r'blog-tags', BlogTagViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'course-categories', CourseCategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'verify-codes', VerifyCodeViewSet)

urlpatterns = [
    # 后台系统
    path('admin/', admin.site.urls),
    # 媒体文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # api登录视图
    path('', include('rest_framework.urls')),
    # api路由
    path('', include(router.urls)),
    # Token
    path('token/', obtain_auth_token),
]
