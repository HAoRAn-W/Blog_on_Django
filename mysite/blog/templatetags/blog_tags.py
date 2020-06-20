from ..models import Blog, Category
from django import template

register = template.Library()


@register.simple_tag
def get_recent_blog(num=5):
    return Blog.objects.all().order_by('-publish_time')[:num]


@register.simple_tag
def archives():
    return Blog.objects.dates('publish_time', 'month', order='DESC')


@register.simple_tag
def get_category():
    return Category.objects.all()
