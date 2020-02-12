import os
import sys
import django
from django.contrib.auth.hashers import make_password

# django环境配置
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + '../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite_server.settings')
django.setup()
# 导入模型，注意，要在环境配置之后再导入
from users.models import UserProfile

# 用户数据
users_data = [
    {
        'username': 'kun',
        'nickname': '管理员',
        'email': 'youngkunzhu@163.com',
        'avatar': 'users/avatars/0.jpg',
        'is_superuser': True,
        'is_staff': True,
        'is_active': True
    },
    {
        'username': 'zhangsan',
        'nickname': '张三',
        'avatar': 'users/avatars/1.jpg',
        'is_superuser': False,
        'is_staff': False,
        'is_active': True
    },
    {
        'username': 'lisi',
        'nickname': '李四',
        'avatar': 'users/avatars/2.jpg',
        'is_superuser': False,
        'is_staff': False,
        'is_active': True
    },
    {
        'username': 'wangwu',
        'nickname': '王五',
        'avatar': 'users/avatars/3.jpg',
        'is_superuser': False,
        'is_staff': False,
        'is_active': True
    },
]

for item in users_data:
    if not UserProfile.objects.filter(username=item['username']).exists():
        user = UserProfile(**item)
        user.password = make_password('123')
        user.save()
        print(user.id, '--', user.username, '--', user.password)
    else:
        print(item['username'], '用户名已存在！')
