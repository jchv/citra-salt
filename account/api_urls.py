from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'account.views.api.account_root', name='root'),
    url(r'^users/$', 'account.views.api.user.List', name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', 'account.views.api.user.Detail', name='user-detail'),
    url(r'^login/$', 'account.views.api.user.Login', name='login'),
    url(r'^logout/$', 'account.views.api.user.Logout', name='logout')
]
