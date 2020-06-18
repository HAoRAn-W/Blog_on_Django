from django.db import models


# Create your models here.
class Category(models.Model):
    # blog category
    name = models.CharField('name', max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    # blog tag
    name = models.CharField('name', max_length=16)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('title', max_length=32)  # 标题
    author = models.CharField('author', max_length=16)  # 标题
    content = models.CharField('content', max_length=2048)  # 正文
    publish_time = models.DateTimeField('publish_time', auto_now_add=True)  # 发布时间
    category = models.CharField(Category, max_length=30)  # 分类
    tags = models.ManyToManyField(Tag)  # 标签

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    visitor_name = models.CharField('visitor_name', max_length=16)
    email = models.EmailField('email')
    comments = models.CharField('comments', max_length=480)
    publish_time = models.DateTimeField('publish_time', auto_now_add=True)

    def __str__(self):
        return self.comments
