from rest_framework.viewsets import ModelViewSet
from .models import BlogCategory, BlogTag, Article
from .serializers import BlogCategorySerializer, BlogTagSerializer, ArticleSerializer
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class BlogCategoryViewSet(ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogTagViewSet(ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer
    pagination_class = LimitOffsetPagination


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = PageNumberPagination
