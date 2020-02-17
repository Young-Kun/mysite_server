from rest_framework.serializers import ModelSerializer
from .models import BlogCategory, BlogTag, Article
from rest_framework import serializers


class BlogCategorySerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'add_time']


class BlogTagSerializer(ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ['id', 'name', 'add_time']


class ArticleSimpleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['url', 'id', 'title', 'category', 'tags', 'user', 'brief', 'cover', 'click_num',
                  'favor_num', 'comment_num', 'add_time', 'modify_time']
        depth = 1


class ArticleDetailSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'category', 'tags', 'user', 'brief', 'cover', 'content', 'click_num',
                  'favor_num', 'comment_num', 'add_time', 'modify_time']
        depth = 1


class ArticleCreateSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ['id', 'category', 'tags', 'user', 'title', 'brief', 'cover', 'content', 'add_time']
