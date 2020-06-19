from django.shortcuts import get_object_or_404, render
from .comment import *
from .models import *


def index(request):
    latest_blog_list = Blog.objects.order_by('-publish_time')[:5]
    return render(request, 'blog/index.html', {'latest_blog_list': latest_blog_list})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.creat(**cleaned_data)

    return render(request, 'blog/detail.html', {'blog': blog, 'comments': blog.comment_set.all().order_by('-created')})

