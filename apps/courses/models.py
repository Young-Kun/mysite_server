from django.db import models
from django.utils import timezone

from orgs.models import School, Teacher


class CourseCategory(models.Model):
    """
    课程类别
    """
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )
    name = models.CharField(max_length=30, help_text='类别名称', verbose_name='类别名称')
    code = models.CharField(max_length=30, help_text='类别代码', verbose_name='类别代码')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, help_text='类目级别', verbose_name='类目级别')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE,
                               help_text='父级类目', verbose_name='父级类目')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程类别'
        verbose_name_plural = '课程类别'

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    课程
    """
    DEGREE = (
        ('cj', '初级'),
        ('zj', '中级'),
        ('gj', '高级'),
    )
    RECOMMEND = (
        ('yes', '推荐到首页'),
        ('no', '不推荐到首页'),
    )
    category = models.ForeignKey(CourseCategory, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='课程类别')
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='授课机构')
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='授课教师')
    title = models.CharField(max_length=125, verbose_name='课程名称')
    degree = models.CharField(choices=DEGREE, max_length=2, verbose_name='课程难度')
    introduction = models.CharField(max_length=255, default='这个课程没有简介', verbose_name='课程简介')
    description = models.TextField(verbose_name='课程描述')
    cover = models.ImageField(upload_to='courses/courses/covers/', max_length=255, null=True, blank=True,
                              verbose_name='课程封面')
    recommend = models.CharField(choices=RECOMMEND, max_length=3, verbose_name='推荐')
    click_num = models.IntegerField(default=0, verbose_name='点击量')
    favor_num = models.IntegerField(default=0, verbose_name='收藏')
    comment_num = models.IntegerField(default=0, verbose_name='评论量')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'

    def __str__(self):
        return self.title
