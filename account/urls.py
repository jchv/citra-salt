from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', 'account.views.user.login', name='login'),
    url(r'^register/$', 'account.views.user.register', name='register'),
]
