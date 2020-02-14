from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class ArticlePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class BlogTagPagination(LimitOffsetPagination):
    pass
