from django.shortcuts import get_object_or_404, render
from .comment import *
from .models import *


def index(request):
    latest_blog_list = Blog.objects.order_by('-publish_time')[:5]
    return render(request, 'blog/index.html', {'latest_blog_list': latest_blog_list})


def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})

