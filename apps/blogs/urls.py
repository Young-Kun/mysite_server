from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogCategoryViewSet, BlogTagViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'blogcategries', BlogCategoryViewSet)
router.register(r'blogtags', BlogTagViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls))
]