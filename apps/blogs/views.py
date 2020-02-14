from rest_framework.viewsets import ModelViewSet
from custom.paginations import BlogTagPagination, ArticlePagination
from .models import BlogCategory, BlogTag, Article
from .serializers import BlogCategorySerializer, BlogTagSerializer, ArticleSerializer
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend


class BlogCategoryViewSet(ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogTagViewSet(ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer
    pagination_class = BlogTagPagination


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category', 'tags']
    ordering_fields = ['add_time', 'click_num', 'favor_num', 'comment_num', 'user']
