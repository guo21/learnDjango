from django.shortcuts import render, get_object_or_404

from comments.forms import CommentForm
from .models import Post, Category
import markdown
# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={
        'title': '21\'s blog',
        'welcome': 'welcome to my blog!',
        'post_list': post_list
    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()

    comment_list = post.comment_set.all()

    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    post_list = Post.objects.filter(time_created__year=year,
                                    time_created__month=month
                                    )
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)

    post_list = cate.post_set.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})