from django.shortcuts import render, get_object_or_404

from citraweb.paginator import Paginator, InvalidPage
from blog.models import Post, Tag


def view(request, title):
    tag = get_object_or_404(Tag, title=title)
    posts = Post.objects.order_by('-date_published').prefetch_related('authors', 'tags').filter(tags__in=[tag])
    try:
        page = Paginator(posts).page(request.GET.get('page', 1))
    except InvalidPage:
        page = Paginator(posts).page(1)

    return render(request, 'blog/tag-view.html',
                  context={'posts': page, 'tag': tag})
