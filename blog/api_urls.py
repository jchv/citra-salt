from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'blog.views.api.blog_root', name='root'),
    url(r'^posts/$', 'blog.views.api.post.List', name='post-list'),
    url(r'^posts/(?P<pk>\d+)/$', 'blog.views.api.post.Detail', name='post-detail'),
    url(r'^posts/(?P<pk>\d+)/authors/$', 'blog.views.api.post.AuthorList', name='author-list'),
    url(r'^posts/(?P<pk>\d+)/authors/(?P<user_pk>\d+)$', 'blog.views.api.post.AuthorDetail', name='author-detail'),
    url(r'^tags/$', 'blog.views.api.tag.List', name='tag-list'),
    url(r'^tags/(?P<title>[-a-zA-Z0-9_]+)/$', 'blog.views.api.tag.Detail', name='tag-detail'),
]
