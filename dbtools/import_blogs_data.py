import os
import sys
from random import randint, choice

import django

# django环境配置
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite_server.settings')
django.setup()
# 导入模型，注意，要在环境配置之后再导入
from blog.models import BlogCategory, BlogTag, BlogArticle
from django.contrib.auth import get_user_model

# 标签数据
tags_data = ['python', 'java', 'nodejs', 'html', 'css', 'c++', 'nginx']
# 类别数据
categories_data = ['Web开发', '人工智能', '财税金融', '动物世界', '道德观察']
# 文章
articles = {
    'python爬虫实践': 'Python爬虫是最流行的dsafsafafdas',
    'django开发实战': 'Django是一个开放源代码的Web应用框架，由Python写成',
    '马是怎么睡觉的': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章1': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章2': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章3': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章4': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章5': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章6': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章7': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章8': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章9': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章10': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章11': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章12': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章13': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章14': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
    '文章15': '马是站着睡觉的。这是从它们的祖先——野马沿袭下来的习性。',
}

for tag_name in tags_data:
    if not BlogTag.objects.filter(name=tag_name).exists():
        tag = BlogTag(name=tag_name)
        tag.save()
        print(tag.id, '--', tag.name)
    else:
        print(tag_name, '已存在！')

for ctg_name in categories_data:
    if not BlogCategory.objects.filter(name=ctg_name).exists():
        category = BlogCategory(name=ctg_name)
        category.save()
        print(category.id, '--', category.name)
    else:
        print(ctg_name, '已存在！')

for title in articles:
    if BlogArticle.objects.filter(title=title).exists():
        article = BlogArticle.objects.filter(title=title).first()
        article.content = articles[title]
    else:
        article = BlogArticle(title=title, content=articles[title])
    article.click_num = randint(10, 100)
    article.favor_num = randint(10, 100)
    article.comment_num = randint(10, 100)
    article.category = choice(BlogCategory.objects.all())
    article.user = choice(get_user_model().objects.all())
    article.cover = 'blog/articles/covers/' + str(randint(0, 5)) + '.jpg'
    article.save()
    article.tags.add(choice(BlogTag.objects.all()))
    article.tags.add(choice(BlogTag.objects.all()))
    article.tags.add(choice(BlogTag.objects.all()))
    article.save()
    print(article.id, '--', article.title)
