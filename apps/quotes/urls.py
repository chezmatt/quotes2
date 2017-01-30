from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', views.index),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.logout),
    url(r'^postreview/$', views.logout),
    # url(r'^/en/(?P<id>\d+)$', views.show),
    # url(r'^$', [name='contacts-list']),
]
