from rest_framework.serializers import ModelSerializer

from custom.textfilter.filter import DFAFilter, keyword_path
from .models import BlogCategory, BlogTag, BlogArticle
from rest_framework import serializers


class BlogCategorySerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'add_time']


class BlogTagSerializer(ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ['id', 'name', 'add_time']


class BlogArticleSimpleSerializer(ModelSerializer):
    class Meta:
        model = BlogArticle
        fields = ['url', 'id', 'title', 'category', 'tags', 'user', 'brief', 'cover', 'click_num',
                  'favor_num', 'comment_num', 'add_time', 'modify_time']
        depth = 1


class BlogArticleDetailSerializer(ModelSerializer):
    class Meta:
        model = BlogArticle
        fields = ['id', 'title', 'category', 'tags', 'user', 'brief', 'cover', 'content', 'click_num',
                  'favor_num', 'comment_num', 'add_time', 'modify_time']
        depth = 1


class BlogArticleCreateSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BlogArticle
        fields = ['id', 'category', 'tags', 'user', 'title', 'brief', 'cover', 'content', 'add_time']

    def validate(self, attrs):
        tf = DFAFilter()
        tf.parse(keyword_path)
        for field in ('title', 'brief', 'content'):
            attrs[field] = tf.filter(attrs[field])
        return attrs
