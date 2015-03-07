from django.shortcuts import render, get_object_or_404

from citraweb.paginator import Paginator, InvalidPage
from blog.models import Post


def view(request, slug):
    return render(request, 'blog/post-view.html',
                  context={'post': get_object_or_404(Post, slug=slug)})


def list(request):
    posts = Post.objects.order_by('-date_published').prefetch_related('authors', 'tags')
    try:
        page = Paginator(posts).page(request.GET.get('page', 1))
    except InvalidPage:
        page = Paginator(posts).page(1)

    return render(request, 'blog/post-list.html',
                  context={'posts': page})
