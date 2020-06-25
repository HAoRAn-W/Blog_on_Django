from django.shortcuts import get_object_or_404, render
from comments.forms import CommentForm
from .models import *
import markdown


def index(request):
    post_list = Post.objects.order_by('-created_time')
    return render(request, 'blog/index.html', {'post_list': post_list})
    # render函数‘ ’内用于表示需要渲染的HTML文件，第三个参数{}用于将需要的参数传递给HTML文件，将对应的{{}}换成对应的值


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=['markdown.extensions.extra',
                                       'markdown.extensions.codehilite',
                                       'markdown.extensions.toc'])
    post.content = md.convert(post.content)
    post.toc = md.toc

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list}
    return render(request, 'blog/detail.html', context)


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
