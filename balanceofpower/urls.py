# coding=utf-8
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^formfill/$', views.formfill, name='formfill'),
    url(r'^results/$', views.results, name='results'),
    url(r'^test/$', views.test, name='test'),
]