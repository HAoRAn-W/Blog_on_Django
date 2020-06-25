from blog.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentForm


@require_POST
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    # django 将用户提交的数据封装在 request.POST 中，这是一个类字典对象。
    # 我们利用这些数据构造了 CommentForm 的实例，这样就生成了一个绑定了用户提交数据的表单。
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(post)

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'comments/preview.html', context=context)
