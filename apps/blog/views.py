from custom.paginations import ArticlePagination
from .models import BlogCategory, BlogTag, BlogArticle
from .serializers import BlogCategorySerializer, BlogTagSerializer, BlogArticleSimpleSerializer, \
    BlogArticleDetailSerializer, BlogArticleCreateSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet, mixins

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class BlogCategoryViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogTagViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer


class BlogArticlesViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    获取文章列表
    """
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSimpleSerializer
    pagination_class = ArticlePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category', 'tags', 'user']
    ordering_fields = ['add_time', 'modify_time', 'click_num', 'favor_num', 'comment_num', 'user', 'title']


class BlogArticleDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    获取单个文章
    """
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleDetailSerializer


class BlogArticleCreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    创建文章
    """
    serializer_class = BlogArticleCreateSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
