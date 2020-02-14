from rest_framework.viewsets import ModelViewSet
from custom.pagination import BlogTagPagination, ArticlePagination
from .models import BlogCategory, BlogTag, Article
from .serializers import BlogCategorySerializer, BlogTagSerializer, ArticleSerializer

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
