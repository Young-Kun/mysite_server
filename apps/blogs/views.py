from custom.paginations import BlogTagPagination, ArticlePagination
from .models import BlogCategory, BlogTag, Article
from .serializers import BlogCategorySerializer, BlogTagSerializer, ArticleSimpleSerializer, ArticleDetailSerializer, \
    ArticleCreateSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet, mixins

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


class BlogCategoryViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogTagViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer
    pagination_class = BlogTagPagination


class ArticleListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    获取文章列表
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSimpleSerializer
    pagination_class = ArticlePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category', 'tags']
    ordering_fields = ['add_time', 'modify_time', 'click_num', 'favor_num', 'comment_num', 'user', 'title']


class ArticleRetrieveViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    获取单个文章
    """
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer


class ArticleCreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = ArticleCreateSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
