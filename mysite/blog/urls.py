from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^blog/(?P<pk>[0-9]+)$', views.detail, name='detail'),
    ]