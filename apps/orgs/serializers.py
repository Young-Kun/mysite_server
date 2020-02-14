from rest_framework.serializers import ModelSerializer
from .models import School, Teacher


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'cover', 'introduction', 'description', 'click_num', 'favor_num', 'add_time']


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'school', 'avatar', 'features', 'add_time']
