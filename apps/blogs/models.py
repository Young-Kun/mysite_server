from django.db import models
from django.contrib.auth import get_user_model


class BlogCategory(models.Model):
    """
    类别
    """
    name = models.CharField(max_length=30, help_text='类别名', editable=False, verbose_name='类别名')
    add_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'
        ordering = ['-add_time']

    def __str__(self):
        return self.name


class BlogTag(models.Model):
    """
       博客分类标签
    """
    name = models.CharField(max_length=25, editable=False, verbose_name='标签名')
    add_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        ordering = ['-add_time']

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(BlogCategory, null=True, on_delete=models.SET_NULL, verbose_name='文章类别')
    tags = models.ManyToManyField(BlogTag, blank=True, verbose_name='文章标签')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='文章作者')
    title = models.CharField(max_length=150, verbose_name='文章标题')
    brief = models.CharField(max_length=255, default='这篇文章没有摘要', blank=True, verbose_name='文章摘要')
    cover = models.ImageField(upload_to='blogs/articles/covers/', max_length=255, null=True, blank=True)
    content = models.TextField(verbose_name='文章内容')
    click_num = models.IntegerField(default=0, verbose_name='点击量')
    favor_num = models.IntegerField(default=0, verbose_name='收藏量')
    comment_num = models.IntegerField(default=0, verbose_name='评论量')
    add_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now_add=True, verbose_name='最后修改')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-modify_time']

    def __str__(self):
        return self.title
