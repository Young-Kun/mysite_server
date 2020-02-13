from rest_framework.serializers import HyperlinkedModelSerializer
from .models import School, Teacher


class SchoolSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['url', 'id', 'name', 'cover', 'introduction', 'description', 'click_num', 'favor_num', 'add_time']


class TeacherSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ['url', 'id', 'name', 'school', 'avatar', 'features', 'add_time']
