from django.db import models
from django.urls import reverse


class Category(models.Model):
    # blog category
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    # blog tag
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=32)  # 标题
    author = models.CharField(max_length=16)  # 作者
    content = models.TextField()  # 正文
    publish_time = models.DateTimeField(auto_now_add=True)  # 发布时间
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 分类
    tags = models.ManyToManyField(Tag, blank=True)  # 标签
    abstract = models.CharField(max_length=200, blank=True)  # 摘要

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    visitor_name = models.CharField(max_length=16)
    email = models.EmailField()
    comments = models.CharField(max_length=480)
    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comments
