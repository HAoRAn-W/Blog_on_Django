from django.shortcuts import render, get_object_or_404, redirect
from mysite.blog.models import Blog

from .models import Comment
from .forms import CommentForm


# Create your views here.

def blog_comment(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect(blog)
        else:
            comment_list = blog.comment_set.all()
            context = {'blog': blog,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context)
