from rest_framework.serializers import ModelSerializer
from .models import BlogCategory, BlogTag, Article


class BlogCategorySerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'add_time']


class BlogTagSerializer(ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ['id', 'name', 'add_time']


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'category', 'tags', 'user', 'brief', 'cover', 'content', 'click_num',
                  'favor_num', 'comment_num', 'add_time']
        depth = 1
