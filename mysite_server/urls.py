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
from rest_framework_jwt.views import obtain_jwt_token

from .settings import MEDIA_ROOT
from rest_framework.routers import DefaultRouter
# 引入视图
from blogs import views as blog_views
from users import views as user_views

# 注册视图
# blogs.urls
router = DefaultRouter()
router.register(r'blog-categories', blog_views.BlogCategoryViewSet)
router.register(r'blog-tags', blog_views.BlogTagViewSet)
router.register(r'articles', blog_views.ArticleListViewSet)
router.register(r'article/detail', blog_views.ArticleRetrieveViewSet)
router.register(r'article/create', blog_views.ArticleCreateViewSet, basename='article-create')
# users.urls
router.register(r'register', user_views.UserRegisterViewSet, basename='register')
router.register(r'verify-codes', user_views.VerifyCodeViewSet, basename='verifycode')

urlpatterns = [
    # 后台系统
    path('admin/', admin.site.urls),
    # 媒体文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # api登录视图
    path('', include('rest_framework.urls')),
    # api路由
    path('', include(router.urls)),
    # JWT 认证
    path('jwt-token-auth/', obtain_jwt_token),
]
