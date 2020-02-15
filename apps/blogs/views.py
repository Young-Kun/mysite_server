from rest_framework.viewsets import ModelViewSet
from custom.paginations import BlogTagPagination, ArticlePagination
from .models import BlogCategory, BlogTag, Article
from .serializers import BlogCategorySerializer, BlogTagSerializer, ArticleSimpleSerializer, ArticleDetailSerializer
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
    pagination_class = ArticlePagination
    # serializer_class = ArticleSimpleSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category', 'tags']
    ordering_fields = ['add_time', 'modify_time', 'click_num', 'favor_num', 'comment_num', 'user', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSimpleSerializer
        if self.action == 'retrieve':
            return ArticleDetailSerializer
        return ArticleSimpleSerializer
