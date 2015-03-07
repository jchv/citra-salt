from django.conf.urls import include, url

apipatterns = [
    url(r'^$', 'citraweb.api_views.api_root', name='root'),
    url(r'^blog/', include('blog.api_urls', namespace='blog')),
    url(r'^account/', include('account.api_urls', namespace='account')),
]

adminpatterns = [
    url(r'^$', 'citraweb.admin_views.admin_index', name='home'),
    url(r'^blog/', include('blog.admin_urls', namespace='blog')),
]

urlpatterns = [
    url(r'^$', 'citraweb.views.home', name='site-home'),
    url(r'^api/', include(apipatterns, namespace='api')),
    url(r'^admin/', include(adminpatterns, namespace='admin')),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^account/', include('account.urls', namespace='account', app_name='account')),
]
