from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
    url(r'^search/$', views.search, name='search'),
    url(r'^searchStudent/$', views.searchStudent, name='searchStudent'),
]
