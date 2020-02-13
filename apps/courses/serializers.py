from rest_framework.serializers import HyperlinkedModelSerializer
from .models import CourseCategory, Course


class CourseCategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['url', 'id', 'name', 'code', 'category_type', 'parent', 'add_time']


class CourseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'id', 'title', 'category', 'school', 'teacher', 'degree', 'introduction', 'description',
                  'cover', 'recommend', 'click_num', 'favor_num', 'comment_num', 'add_time']
