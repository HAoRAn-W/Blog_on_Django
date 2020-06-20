from django.shortcuts import get_object_or_404, render
from .comment import *
from .models import *
import markdown


def index(request):
    latest_blog_list = Blog.objects.order_by('-publish_time')[:5]
    return render(request, 'blog/index.html', {'latest_blog_list': latest_blog_list})


def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.content = markdown.markdown(blog.content, extensions=['markdown.extensions.extra',
                                                               'markdown.extensions.codehilite',
                                                               'markdown.extensions.toc'])
    return render(request, 'blog/detail.html', {'blog': blog})


def archives(request, year, month):
    blog_list = Blog.objects.filter(
                                    publish_time__month=month
                                    ).order_by('-publish_time')
    return render(request, 'blog/index.html', {'blog_list': blog_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    blog_list = Blog.objects.filter(category=cate).order_by('-publish_time')
    return render(request, 'blog/index.html', {'blog_list': blog_list})
