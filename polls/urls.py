from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^create_order/$', views.create_order, name='create_order'),
    url(r'^(?P<order_id>[0-9]+)/$', views.detail, name='detail'),
]