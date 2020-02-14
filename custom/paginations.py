from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class ArticlePagination(PageNumberPagination):
    page_size = 5


class BlogTagPagination(LimitOffsetPagination):
    pass
