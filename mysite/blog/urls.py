from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('archives/<int:year>/<int:month>', views.archives, name='archives'),
    path('category/<int:pk>', views.category, name='category'),
    path('<int:pk>/detail', views.detail, name='detail'),


]
