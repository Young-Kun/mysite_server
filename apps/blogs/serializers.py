from rest_framework.serializers import HyperlinkedModelSerializer
from .models import BlogCategory, BlogTag, Article


class BlogCategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['url', 'id', 'name', 'add_time']


class BlogTagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BlogTag
        fields = ['url', 'id', 'name', 'add_time']


class ArticleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['url', 'id', 'title', 'category', 'tags', 'user', 'brief', 'cover', 'content', 'click_num',
                  'favor_num', 'comment_num', 'add_time']
        depth = 1
