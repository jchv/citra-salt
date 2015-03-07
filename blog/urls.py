from django.conf.urls import url

urlpatterns = [
    url(r'^rss/$', 'blog.feeds.rss', name='rss-feed'),
    url(r'^atom/$', 'blog.feeds.atom', name='atom-feed'),
    url(r'^posts/$', 'blog.views.post.list', name='post-list'),
    url(r'^posts/(?P<slug>[-a-zA-Z0-9_]+)/$', 'blog.views.post.view', name='post-view'),
    url(r'^tag/(?P<title>[-a-zA-Z0-9_]+)/$', 'blog.views.tag.view', name='tag-view'),
]
