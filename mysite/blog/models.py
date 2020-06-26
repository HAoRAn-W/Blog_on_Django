from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=32)  # 标题
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 作者
    content = models.TextField()  # 正文
    created_time = models.DateTimeField()  # 发布时间
    modified_time = models.DateTimeField()  # 修改时间
    abstract = models.CharField(max_length=200, blank=True)  # 摘要
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 分类
    tags = models.ManyToManyField(Tag, blank=True)  # 标签
    views = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


