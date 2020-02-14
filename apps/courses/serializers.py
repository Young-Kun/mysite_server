from rest_framework.serializers import ModelSerializer
from .models import CourseCategory, Course


class CourseCategorySerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id', 'name', 'code', 'category_type', 'parent', 'add_time']


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'category', 'school', 'teacher', 'degree', 'introduction', 'description',
                  'cover', 'recommend', 'click_num', 'favor_num', 'comment_num', 'add_time']
