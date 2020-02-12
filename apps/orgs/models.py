from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class School(models.Model):
    """
    学校
    """
    name = models.CharField(max_length=50, verbose_name='学校名字')
    cover = models.ImageField(upload_to='orgs/schools/covers/', default='', max_length=255, verbose_name='学校封面')
    introduction = models.CharField(max_length=255, default='这个学校没有简介', verbose_name='学校简介')
    description = RichTextUploadingField(default='这个学校没有详情介绍', verbose_name='学校详情')
    click_num = models.IntegerField(default=0, verbose_name='点击量')
    favor_num = models.IntegerField(default=0, verbose_name='收藏量')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '学校'
        verbose_name_plural = '学校'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """
    教师
    """
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='签约学校')
    name = models.CharField(max_length=25, verbose_name='教师名字')
    avatar = models.ImageField(upload_to='orgs/teachers/avatars/', default='', max_length=255, verbose_name='教师头像')
    features = models.CharField(max_length=255, default='诙谐幽默，严谨求实', verbose_name='教学特色')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = '教师'

    def __str__(self):
        return self.name
